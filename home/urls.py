from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('' , views.homeview, name = 'homeurl'),
    # path('about' , views.aboutview),
    # path('speakers' , views.speakersview),
    # path('sponsers' , views.sponsersview),
    # path('blog' , views.blogview),
]