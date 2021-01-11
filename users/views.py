from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.models import User
from random import sample
from reviews.models import Review, Song, Cluster
from reviews.recommendations import update_clusters


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Thank you for joining SongGest, {username}! Please login now.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Sign Up'})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
    context = {'user_form': user_form}
    return render(request, 'users/profile.html', context)


@login_required
def recommendation(request):
    # 1. Get current user's reviews
    user_reviews = Review.objects.filter(
        author=request.user).prefetch_related('song')
    user_reviews_song_ids = set(map(lambda x: x.song.id, user_reviews))

    # 2. Get this user's cluster name
    try:
        user_cluster_name = User.objects.get(
            username=request.user.username).cluster_set.first().name
    except:
        # If this user does not belong to any cluster, update the clusters.
        update_clusters(is_new_user=True)
        user_cluster_name = User.objects.get(
            username=request.user.username).cluster_set.first().name

    # 3. Get other members in this cluster
    other_cluster_members = Cluster.objects.get(
        name=user_cluster_name).users.exclude(username=request.user.username).all()

    # 4. Get reviews by other members, excluding songs reviewed by the current user
    other_members_reviews = Review.objects.filter(
        author__in=other_cluster_members).exclude(song__id__in=user_reviews_song_ids)
    other_members_reviews_song_ids = set(
        map(lambda x: x.song.id, other_members_reviews))

    # 5. Create a song list including the above song ids, order by rating
    song_list = sorted(
        list(Song.objects.filter(id__in=other_members_reviews_song_ids)),
        key=Song.average_rating,
        reverse=True
    )

    # 6. If there are less than 10 recommendations, fill in the rest slots with random picked songs that have not been rated by the user
    if len(song_list) < 10:
        num_needed = 10-len(song_list)
        rest_song_ids = Song.objects.exclude(
            id__in=user_reviews_song_ids).exclude(id__in=other_members_reviews_song_ids).values_list('id', flat=True)
        random_song_id_list = sample(list(rest_song_ids), num_needed)
        song_list += Song.objects.filter(id__in=random_song_id_list)

    context = {'user': request.user, 'song_list': song_list}
    return render(request, 'users/recommendation.html', context)


@login_required
def more_recommendation(request):
    # Naive recommendation approach: recommend 10 random song that the user has not reviewed
    user_reviews = Review.objects.filter(
        author=request.user).prefetch_related('song')
    user_reviews_song_ids = set(map(lambda x: x.song.id, user_reviews))
    id_list = Song.objects.exclude(
        id__in=user_reviews_song_ids).values_list('id', flat=True)
    random_id_list = sample(list(id_list), 10)
    song_list = Song.objects.filter(id__in=random_id_list)

    context = {'user': request.user, 'song_list': song_list}
    return render(request, 'users/recommendation.html', context)
