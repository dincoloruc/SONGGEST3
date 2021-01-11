from reviews.models import Song


def run():
    Song.objects.all().delete()
    print("Deleted all songs from database.")
