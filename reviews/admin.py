from django.contrib import admin

from .models import Song, Review, Cluster


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('song', 'rating', 'author',  'date_created')
    list_filter = ['song', 'rating', 'author']
    search_fields = ['song']
    
class SongAdmin(admin.ModelAdmin):
    model = Song 
    list_display = ('name', 'artist', 'genre', 'year', 'average_rating')
    list_filter = ['name', 'genre']
    search_fields = ['name']

class ClusterAdmin(admin.ModelAdmin):
    model = Cluster
    list_display = ['name', 'get_members']

admin.site.register(Song, SongAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Cluster, ClusterAdmin)