from django import forms
from . import models
from django.utils.translation import gettext_lazy as _

CHOICES = [(True,'بله'),(False,'خیر')]
class SignupForm(forms.ModelForm):
    tedxExperience = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect())
    class Meta:
        model = models.Signup
        fields = '__all__'
        labels = {
            'name':_('نام و نام خانوادگی'),
            'email':_('ایمیل'),
            'phone_number':_('شماره تماس'),
            'city':_('شهر'),
            'howyouknowus':_('نحوه اشنایی با ما')
        }
        