from django.shortcuts import render,redirect,get_object_or_404
from . import models
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('siteadmin:adminurl')
    elif request.method == 'POST':
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
    team = models.Team.objects.all()
    args = {'speakers':speakers,'team':team}
    return render(request,'siteadmin/adminn.html',args)


@login_required(login_url='/siteadmin/')
def editspeakerView(request , speakerid):
    speaker = get_object_or_404(models.Speaker, id = speakerid)
    form = forms.SpeakerForm(request.POST or None,instance = speaker)
    if request.POST.get('delete') == 'true':
        speaker.delete()
        return redirect('siteadmin:adminurl')
    if form.is_valid():
        speaker = form.save(commit = False)
        speaker.save()


    args = {'speaker':speaker ,'form':form}
    return render(request,'siteadmin/editspeaker.html',args)


@login_required(login_url='/siteadmin/')
def addspeakerView(request):
    form = forms.SpeakerForm(request.POST or None)
    if form.is_valid():
        speaker = form.save(commit = False)
        speaker.save()
        return redirect('siteadmin:adminurl')
    args = {'form':form}
    return render(request,'siteadmin/editspeaker.html',args)



@login_required(login_url='/siteadmin/')
def editteamView(request , teamid):
    team = get_object_or_404(models.Team, id = teamid)
    form = forms.TeamForm(request.POST or None,instance = team)
    if request.POST.get('delete') == 'true':
        team.delete()
        return redirect('siteadmin:adminurl')
    if form.is_valid():
        team = form.save(commit = False)
        team.save()
        

    args = {'team':team, 'form':form}
    return render(request,'siteadmin/editteam.html',args)


@login_required(login_url='/siteadmin/')
def addteamView(request):
    form = forms.TeamForm(request.POST or None)
    if form.is_valid():
        team = form.save(commit = False)
        team.save()
        return redirect('siteadmin:adminurl')
    args = {'form':form}
    return render(request,'siteadmin/editteam.html',args)