from django.shortcuts import render
from .models import User
from .forms import LoginForm, RegistrationForm, UserProfileForm
from django.http import HttpResponseRedirect
# Create your views here.

def Sign_in(request):
     
     return render(request, 'auth.html')

def Sign_up(request):
     if request.method == 'POST':
          form = RegistrationForm(data=request.POST)
          if form.is_valid():
               form.save()
               return HttpResponseRedirect('/')
     else:
          form=RegistrationForm()
     context = {'form':form}
     return render(request, 'sing_up.html', context)