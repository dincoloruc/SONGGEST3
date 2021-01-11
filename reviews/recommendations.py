from .models import Review, Song, Cluster
from django.contrib.auth.models import User
from sklearn.cluster import KMeans
from scipy.sparse import dok_matrix, csr_matrix
import numpy as np

def update_clusters(is_new_user):
    num_reviews = Review.objects.count()
    update_step = 10
    if num_reviews % update_step == 0 or is_new_user: 
        # Create a sparse matrix from user reviews
        all_users = User.objects.only("username")
        all_reviewed_song_ids = set(map(lambda x: x.song.id, Review.objects.only("song")))
        num_users = len(list(all_users))
        ratings_m = dok_matrix((num_users, max(all_reviewed_song_ids)+1), dtype=np.float32)
        
        for i in range(num_users): # each user corresponds to a row, in the order of all_authors
            user_reviews = Review.objects.filter(author=all_users[i])
            for user_review in user_reviews:
                ratings_m[i,user_review.song.id] = user_review.rating

        # Perform kmeans clustering
        k = int(num_users / 10) + 2
        kmeans = KMeans(n_clusters=k)
        clustering = kmeans.fit(ratings_m.tocsr())
        
        # Update clusters
        Cluster.objects.all().delete()
        new_clusters = {i: Cluster(name=i) for i in range(k)}
        for cluster in new_clusters.values(): # clusters need to be saved before referring to users
            cluster.save()
        for i,cluster_label in enumerate(clustering.labels_):
            new_clusters[cluster_label].users.add(User.objects.get(username=all_users[i].username))