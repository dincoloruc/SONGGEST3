# SONGGEST3: Song Recommender


SongGest is a platform and a recommendation system to share information and get insights on songs you like or dislike.

## Motivation

As a music lover, it is not always easy to find new songs that suits your taste. Genres,moods, acousticness, danceability, popularity... There is a lot to decide.

We hope to make the process easier by building this song-review platform. We have found a song list and people can rate the songs they want.

This is a growing list. If you find a song that is not on our list, please contact us and suggest new songs.

## Machine Learning-based Recommendations

Registered users will get a personalized song recommendation list based on machine learning. We use K-means clustering as a machine learning model that makes use of user similarity in order to provide the recommendations. The recommendation system is built using Python technologies such as Pandas, SciPy, and Scikit-learn.

## Full Featured Django Application

SongGest is built with Django, which powers it to have the following features:

- Relational data models including songs, reviews, users and user clusters (for the recommendation system).
- Search songs by keywords, or filter songs by name, genre, artist...
- Full CRUD features for reviews: users can create new reviews, see reviews, update or delete their own reviews.
- View reviews by user.
- Pagination for all song list and filtered song list.
- User registration, login & logout system.
- Reset password through email if password is forgotten.
- Users can view and update their profile.
- Customized admin page at [/admin].
- Get personalized recommendations based on machine learning algorithm.
