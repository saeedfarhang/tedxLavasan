from django.shortcuts import render
from . import form
# Create your views here.
def homeview(request):
    return render(request, 'home/homepage.html')

def signupview(request):

    if request.method == 'POST':
        signupForm = form.SignupForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            print('save')
    else:
        signupForm = form.SignupForm()
    
    return render(request, 'home/signup.html' ,{'form':signupForm})