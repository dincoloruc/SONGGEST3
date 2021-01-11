from .models import Song
import django_filters


class SongFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label="Serach song by name ")
    genre = django_filters.AllValuesFilter()
    year = django_filters.NumberFilter()
    artist = django_filters.CharFilter(lookup_expr='icontains', label="Search for Artist")

    class Meta:
        model = Song
        fields = [
            'genre',
            'year',
            'name',
            'artist',
        ]