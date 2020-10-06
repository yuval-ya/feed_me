from django.shortcuts import render
from django.http import HttpResponse


def user_profile(request):
    return HttpResponse('<h1>Profile</h1>')

# Create your views here.
