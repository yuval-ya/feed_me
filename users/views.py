from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from .models import Profile
from feed.models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.generic import (
    DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)


def register(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            if form.cleaned_data.get('image'):
                user.profile.image = form.cleaned_data.get('image')
            username = form.cleaned_data.get('username')
            user.save()
            messages.success(
                request, f"Account created for {username}, you are now able to login.")
            return redirect('login')
        else:
            messages.warning(request, "Failed to create the account")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form, 'title': 'Register'})


@ login_required
def update_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated.")
            return redirect('myprofile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/update_profile.html', context)


@ login_required
def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(author=request.user)
    context = {
        'profile': profile,
        'posts': posts,
    }
    return render(request, 'users/myprofile.html', context)
