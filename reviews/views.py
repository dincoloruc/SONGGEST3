from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Review, Song
from .recommendations import update_clusters
from .filters import SongFilter


# Create your views here.

def home_view(request):
    review_list = [Review.objects.first(), Review.objects.last()]
    song_count = Song.objects.count()
    review_count = Review.objects.count()
    context = {
        'review_list': review_list,
        'song_count': song_count,
        'review_count': review_count,
    }
    return render(request, 'reviews/home.html', context)

class ReviewListView(ListView):
    model = Review
    context_object_name = 'review_list'
    ordering = ['-date_created']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Latest Reviews for Songs'
        return context


class ReviewDetailView(DetailView):
    model = Review
    context_object_name = 'review'


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = [ 'rating']

    def get_context_data(self, **kwargs):
        self.song = get_object_or_404(Song, pk=self.kwargs['song_id'])
        context = super().get_context_data(**kwargs)
        context['song'] = self.song
        return context

    def form_valid(self, form):
        self.song = get_object_or_404(Song, pk=self.kwargs['song_id'])
        form.instance.author = self.request.user
        form.instance.song = self.song
        update_clusters(is_new_user=False)
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['rating']
    template_name = 'reviews/update_review.html'

    def get_context_data(self, **kwargs):
        review = self.get_object()
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Review'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    success_url = reverse_lazy("song_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author


class FilteredListView(ListView):
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(
            self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class SongListView(FilteredListView):
    filterset_class = SongFilter
    model = Song
    context_object_name = 'song_list'
    paginate_by = 50


class SongDetailView(DetailView):
    model = Song
    context_object_name = 'song'


class UserReviewListView(ListView):
    model = Review
    template_name = 'reviews/user_reviews.html'
    context_object_name = 'review_list'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Review.objects.filter(author=user).order_by('-date_created')



