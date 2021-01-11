from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import numpy as np


class Song(models.Model):
    name = models.CharField(max_length=80)
    artist = models.CharField(max_length=80)
    genre = models.CharField(max_length=80)
    year = models.IntegerField(null=True, blank=True)
    BPM = models.FloatField(null=True, blank=True)
    energy = models.FloatField(null=True, blank=True)
    danceability = models.FloatField(null=True, blank=True)
    loudness = models.FloatField(null=True, blank=True)
    liveness = models.FloatField(null=True, blank=True)
    valance = models.FloatField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    acousticness = models.FloatField(null=True, blank=True)
    speechiness = models.FloatField(null=True, blank=True)
    popularity = models.FloatField(null=True, blank=True)

    
    
    def average_rating(self):
       return self.review_set.aggregate(models.Avg('rating'))['rating__avg']
        
    def __unicode__(self):
        return self.name

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )

    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f'{self.author.username} reviewed {self.song.name}'

    def get_absolute_url(self):
        return reverse('song_detail', kwargs={'pk': self.song.pk})

class Cluster(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def get_members(self):
        return "\n".join([u.username for u in self.users.all()])