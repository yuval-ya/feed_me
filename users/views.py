from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from feed import views as feed_view


def register(request):
    if request.user.is_authenticated:
        return feed_view.Home(request)
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Account created for {username}, you are now able to login.")
            return redirect('login')
        else:
            messages.warning(request, "Failed to create the account")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form, 'title': 'Register'})


@ login_required
def Profile(request):
    return render(request, 'users/profile.html')
