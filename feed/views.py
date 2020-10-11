from django.shortcuts import render, redirect
from .models import Post
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)


@login_required
def feed_view(request):
    if request.method == "POST":
        q_form = CreatePostForm(request.POST)
        q_form.instance.author = request.user
        if q_form.is_valid():
            q_form.save()
            messages.success(
                request, f"Post Created.")
            return redirect('feed-home')
        else:
            messages.warning(request, "Failed to create the post")
    else:
        q_form = CreatePostForm()

    context = {
        'posts': Post.objects.all(),
        'q_form': q_form
    }

    return render(request, 'feed/feed.html', context)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content']

    def get_success_url(self):
        return reverse('feed-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('feed-home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
