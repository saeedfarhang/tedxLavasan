from django.shortcuts import render
from . import forms
from . import models
# Create your views here.


def homeview(request):
    speakers = models.Speaker.objects.all()
    introspeakerform = forms.IntroSpeakerForm


    
    args = {'speakers' : speakers , 'introspeakerform' : introspeakerform}
    return render(request, 'home/homepage.html', args)



def signupview(request):

    if request.method == 'POST':
        signupForm = forms.SignupForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            print('save')
    else:
        signupForm = forms.SignupForm()
    
    return render(request, 'home/signup.html' ,{'form':signupForm})