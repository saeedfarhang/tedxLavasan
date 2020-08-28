from django import forms
from . import models
from django.utils.translation import gettext_lazy as _


class IntroSpeakerForm(forms.ModelForm):
    class Meta:
        model = models.IntroSpeaker
        fields = '__all__'
        # city = forms.Select(attrs={})
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
            'phone_number':forms.TextInput(attrs={'placeholder': 'شماره تماس' }),
            'work':forms.TextInput(attrs={'placeholder': 'شغل'}),
            'why' : forms.Textarea(attrs={'placeholder':'دلایل معرفی فرد مورد نظر را بنویسید'}),
            'yourname':forms.TextInput(attrs={'placeholder':'نام و نام خانوادگی'}),
            'youremail': forms.EmailInput(attrs={'placeholder': ' ایمیل'}),
            'yourphone_number':forms.TextInput(attrs={'placeholder': 'شماره تماس'}),
        }
        
class addSponsorForm(forms.ModelForm):
    class Meta:
        model = models.Sponsor
        fields = '__all__'
        widgets = {
            'companyname' : forms.TextInput(attrs={'placeholder':'نام شرکت'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
            'phone_number':forms.TextInput(attrs={'placeholder': 'شماره تماس' }),
            'activity':forms.TextInput(attrs={'placeholder': 'حوزه فعالیت' }),
            'description':forms.Textarea(attrs={'placeholder': 'توضیحات' }),
        }

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = models.WorkWithUs
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
            'phone_number':forms.TextInput(attrs={'placeholder': 'شماره تماس' }),
            'field':forms.Textarea(attrs={'placeholder': 'در چه زمینه ای میتوانید به ما کمک کنید؟' }),
    }
