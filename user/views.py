from django.shortcuts import render
from .models import User
from .forms import LoginForm, RegistrationForm, UserProfileForm
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def sign_in(request):
     if request.method == 'POST':
          form = LoginForm(data=request.POST)
          if form.is_valid():
               username = request.POST['username']
               password = request.POST['password']
               user = auth.authenticate(username=username, password=password)
               if user:
                    auth.login(request,user)
                    print('--------------------------------------')
                    messages.success(request,f'{username} вы успешно авторизовались')
                    return HttpResponseRedirect('/')
     else:
          form = LoginForm()
     context = {'form':form}
     return render(request, 'auth.html', context)

@login_required(login_url='/sing_up/')
def sign_up(request):
     if request.method == 'POST':
          form = RegistrationForm(data=request.POST)
          if form.is_valid():
               form.save()
               return HttpResponseRedirect('/')
     else:
          form=RegistrationForm()
     context = {'form':form}
     return render(request, 'sing_up.html', context)

def logout(request):
     auth.logout(request)
     return HttpResponseRedirect('/')