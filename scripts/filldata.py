import pandas as pd
import sys, os 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SONGGEST3.settings")

import django
django.setup()  

from reviews.models import Song, Review
def run():
    df = pd.read_csv("./data/songsnew.csv")

    df['title'].fillna('missing', inplace=True)
    
    df['artist'].fillna('missing', inplace=True)

    df['genre'].fillna('missing', inplace=True)

    median = df['year'].median()
    df['year'].fillna(median, inplace=True)

    median1 = df['BPM'].median()
    df['BPM'].fillna(median1, inplace=True)

    median2 = df['energy'].median()
    df['energy'].fillna(median2, inplace=True)

    median3 = df['danceability'].median()
    df['danceability'].fillna(median3, inplace=True)

    median4 = df['loudness'].median()
    df['loudness'].fillna(median4, inplace=True)

    median5 = df['liveness'].median()
    df['liveness'].fillna(median5, inplace=True)

    median6 = df['valence'].median()
    df['valence'].fillna(median6, inplace=True)

    median7 = df['length'].median()
    df['length'].fillna(median7, inplace=True)

    median8 = df['acousticness'].median()
    df['acousticness'].fillna(median8, inplace=True)

    median9 = df['speechiness'].median()
    df['speechiness'].fillna(median9, inplace=True)

    median10 = df['popularity'].median()
    df['popularity'].fillna(median10, inplace=True)

    df.drop(['id1'], axis=1, inplace=True)

    df.to_csv('songsnew1.csv')

    print(df)