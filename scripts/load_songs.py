import pandas as pd
import sys, os 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SONGGEST3.settings")

import django
django.setup()  

from reviews.models import Song, Review

def save_song_from_row(song_row):
    song = Song()
    song.id = song_row.id
    song.name = song_row.title
    song.artist = song_row.artist
    song.genre = song_row.genre
    song.year = song_row.year
    song.BPM = song_row.BPM
    song.energy = song_row.energy
    song.danceability = song_row.danceability
    song.loudness = song_row.loudness
    song.liveness = song_row.liveness
    song.valence = song_row.valence
    song.length = song_row.length
    song.acousticness = song_row.acousticness
    song.speechiness = song_row.speechiness
    song.popularity = song_row.popularity
    song.save()


def run():
    df = pd.read_csv("songsnew1.csv")
    df.apply(save_song_from_row, axis=1)
    print('Saved all song data into database.')