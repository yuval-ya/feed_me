from django.shortcuts import render
from .models import Post


def Home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'feed/feed.html', context)
