from django import forms
from . import models
from django.utils.translation import gettext_lazy as _


class IntroSpeakerForm(forms.ModelForm):
    class Meta:
        model = models.IntroSpeaker
        fields = '__all__'