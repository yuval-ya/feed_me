from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)


@login_required
def feed_view(request):

    qs = Post.objects.all()
    profile = request.user.profile
    p_form = CreatePostForm()

    if 'submit_p_form' in request.POST:
        p_form = CreatePostForm(request.POST, request.FILES)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.author = profile
            instance.save()
            p_form = CreatePostForm()
            messages.success(request, "Post Created.")

    context = {
        'posts': qs,
        'p_form': p_form,
    }

    return render(request, 'feed/feed_home.html', context)


@login_required
def post_liked_unliked_view(request, post_id):

    user = request.user

    if request.method == 'POST':
        post_obj = get_object_or_404(Post, id=post_id)
        profile = user.profile

        if profile in post_obj.get_profiles_liked():
            like_obj = Like.objects.get(user=profile, post=post_obj)
            like_obj.delete()
        else:
            like_obj = Like(user=profile, post=post_obj)
            like_obj.save()

    return redirect('feed-home')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['content', 'image']

    def get_success_url(self):
        messages.success(
            self.request, "Post Created.")
        return reverse('feed-home')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author.user:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content', 'image']

    def get_success_url(self):
        messages.success(
            self.request, "Post Updated.")
        return reverse('feed-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def get_success_url(self):
        messages.info(self.request, "Post Deleted")
        return reverse('feed-home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author.user:
            return True
        return False
