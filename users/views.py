from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def register(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
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
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/update_profile.html', context)


@ login_required
def Profile(request):
    return render(request, 'users/profile.html')
