from reviews.models import Review


def run():
    Review.objects.all().delete()
    print("Deleted all reviews from database.")
