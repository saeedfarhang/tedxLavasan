from django.urls import path
from . import views

urlpatterns = [
    path('' , views.homeview),
    path('signup' , views.signupview , name='signup'),
    # path('about' , views.aboutview),
    # path('speakers' , views.speakersview),
    # path('sponsers' , views.sponsersview),
    # path('blog' , views.blogview),
]