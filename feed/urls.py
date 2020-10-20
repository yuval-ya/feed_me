from django.urls import path
from . import views
from .views import (
    feed_view,
    post_liked_unliked_view,
    PostDetailView,
    PostDeleteView,
    PostUpdateView,
    PostCreateView,
)


urlpatterns = [
    path('', feed_view, name='feed-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:post_id>/like/', post_liked_unliked_view, name='like-post'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
