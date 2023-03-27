from django.shortcuts import render
from .models import Nike
# Create your views here.

def shop(request):
     nike = Nike.objects.all()

     context = {'nike':nike}
     return render(request, 'index.html', context)
def detal(request):
     return render(request, 'qwer.html')