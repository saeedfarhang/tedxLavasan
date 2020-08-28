from django.shortcuts import render ,redirect
from . import forms
from . import models
# Create your views here.


def homeview(request):
    speakers = models.Speaker.objects.all()
    team = models.Team.objects.all()
    # intro speaker form
    if request.method == 'POST':
        if request.POST.get('form_type') == 'introspeakerform':
            introspeakerform = forms.IntroSpeakerForm(request.POST)
            if introspeakerform.is_valid():
                print("intro speakeaker post")
                introspeakerform.save()
                # introspeakerform = forms.IntroSpeakerForm()
                return redirect('home:homeurl')
            else:
                print(introspeakerform.errors)
        
        elif request.POST.get('form_type') == 'addsponsorform':
            addsponsorform = forms.addSponsorForm(request.POST)
            if addsponsorform.is_valid():
                print("add sponser post")
                addsponsorform.save()
                return redirect('home:homeurl')
            else:
                print(addsponsorform.errors)
        
        elif request.POST.get('form_type') == 'volunteerform':
            volunteerform = forms.VolunteerForm(request.POST)
            if volunteerform.is_valid():
                print('add volenteerform')
                volunteerform.save()
                return redirect('home:homeurl')
            else:
                print(volunteerform.errors)
    else:
        introspeakerform = forms.IntroSpeakerForm()
        addsponsorform = forms.addSponsorForm()
        volunteerform = forms.VolunteerForm()

    args = {'speakers' : speakers , 'team' : team , 'introspeakerform' : introspeakerform , 'addsponsorform':addsponsorform , 'volunteerform' : volunteerform}
    return render(request, 'home/homepage.html', args)


