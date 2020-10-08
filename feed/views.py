from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required


@login_required
def Home(request):
    context = {
        'title': 'Home',
        'posts': Post.objects.all()
    }
    return render(request, 'feed/feed.html', context)
