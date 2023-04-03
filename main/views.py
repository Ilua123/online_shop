from django.shortcuts import render
from .models import Nike, Images
from django.http import HttpResponseRedirect
# Create your views here.

def shop(request):
     nike = Nike.objects.all()

     context = {'nike':nike}
     return render(request, 'index.html', context)


def detal(request, id):
     product= Nike.objects.get(id=id)
     images=Images.objects.filter(sneakers=product)
     return render(request, 'qwer.html', {'product':product, 'images':images})

def faforites(request, id):
     favorite_products= request.session.get('favorite_products', [])
     favorite_products.append(id)
     st=set(favorite_products)
     request.session['favorite_products'] = list(st)
     nike = Nike.objects.all()
     context = {'nike':nike}
     return render(request, 'index.html', context)

def favorit(request):
     favorite_products= request.session.get('favorite_products', [])
     favorite_products = Nike.objects.filter(id__in=favorite_products)
     nike = Nike.objects.all()
     context = {'nike':favorite_products}
     return render(request, 'favorit.html', context)

def delet_favorites(request, id):
     favorite_products= request.session.get('favorite_products', [])
     favorite_products = Nike.objects.filter(id__in=favorite_products)
     request.session['favorite_products'] = favorite_products

     # context={'favorite_products':favorite_products}
     return HttpResponseRedirect
     # return render(request, 'favorit.html', context)

def carzina(request):
    carzina= request.session.get('carzina', [])
    carzina = Nike.objects.filter(id__in=carzina)
    context = {'nike':carzina}
    return render(request, 'carzina.html', context)

def carzines(request, id):
     carzina= request.session.get('carzina', [])
     carzina.append(id)
     st=set(carzina)
     request.session['carzina'] = list(st)
     nike = Nike.objects.all()
     context = {'nike':nike}
     return render(request, 'index.html', context)

def about_us(request):
     return render(request, 'about_us.html')