from django.urls import path
from . import views
from .views import feed_view, PostDetailView, PostUpdateView, PostDeleteView


urlpatterns = [
    # path('', PostListView.as_view(), name='feed-home'),
    path('', feed_view, name='feed-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]
