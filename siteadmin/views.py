from django.shortcuts import render,redirect,get_object_or_404
from . import models
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('siteadmin:adminurl')
    else:
        form = AuthenticationForm()
    return render(request,'siteadmin/login.html',{'form': form})

def logout_view(request):
        logout(request)
        return redirect('home:homeurl')


@login_required(login_url='/siteadmin/')
def admin_view(request):
    speakers = models.Speaker.objects.all()
    args = {'speakers':speakers}
    return render(request,'siteadmin/adminn.html',args)

@login_required(login_url='/siteadmin/')
def editspeakerView(request , speakerid):
    speaker = get_object_or_404(models.Speaker, id = speakerid)
    form = forms.SpeakerForm(request.POST or None,instance = speaker)
    if form.is_valid():
        speaker = form.save(commit = False)
        speaker.save()

    args = {'speaker':speaker , 'form':form}
    return render(request,'siteadmin/editspeaker.html',args)