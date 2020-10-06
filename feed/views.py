from django.shortcuts import render

posts = [
    {
        'author': 'Yuval',
        'content': 'some content',
        'date_posted': 'October 05, 2020',
        'likes': 3
    },
    {
        'author': 'Oded',
        'content': 'some other content',
        'date_posted': 'October 06, 2020',
        'likes': 10
    }

]


def Home(request):
    context = {
        'posts': posts
    }
    return render(request, 'feed/feed_temp.html', context)
