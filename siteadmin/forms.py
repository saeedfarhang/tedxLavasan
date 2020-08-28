from django import forms
from . import models

class SpeakerForm(forms.ModelForm):
    class Meta:
        model = models.Speaker
        fields = '__all__'

class TeamForm(forms.ModelForm):
    class Meta:
        model = models.Team
        fields = '__all__'