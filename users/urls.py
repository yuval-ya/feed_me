from django.urls import path
from users import views as users_views


app = 'profiles'

urlpatterns = [
    path('myprofile/', users_views.my_profile_view, name='myprofile'),
    path('myprofile/update/', users_views.update_profile, name='update_profile'),
]
