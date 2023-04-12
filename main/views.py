from django.shortcuts import render
from .models import Nike, Images, Order, OrderItem
from django.http import HttpResponseRedirect
import uuid
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from services.main import order_data_sender_to_email
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
@login_required(login_url='/carzina/')
def carzina(request):
    total_price = 0
    cart_products= request.session.get('cart_products', [])
    cart_products = Nike.objects.filter(id__in = cart_products)
    for i in cart_products:
         total_price +=i.price
    context = {'products':cart_products, 'amount':cart_products.count,'total_price':total_price}
    return render(request, 'carzina.html', context)

@login_required(login_url='/carzines/')
def carzines(request, id):
     cart_products= request.session.get('cart_products', [])
     cart_products.append(id)
     st=set(cart_products)
     request.session['cart_products'] = list(st)
     nike = Nike.objects.all()
     total_price = 0
     for i in nike:
          total_price +=i.price
     context = {'nike':nike, 'amount':nike.count,'total_price':total_price}
     print(st)
     return render(request, 'index.html', context)

def about_us(request):
     return render(request, 'about_us.html')

# def cart(request, id):
#      cart_products= request.session.get('cart_products', [])
#      cart_products.append(id)
#      st=set(cart_products)
#      request.session['cart_products'] = list(st)
#      nike = Nike.objects.all()
#      total_price = 0
#      for i in nike:
#           total_price +=i.price
#      context = {'nike':nike, 'amount':nike.count,'total_price':total_price}
#      print(st)
#      return render(request, 'cart.html', context)

# def cart_page(request):
#      cart_products= request.session.get('cart_products', [])
#      cart_products = Nike.objects.filter(id__in = cart_products)
#      total_price = 0
#      for i in cart_products:
#           total_price +=i.price
#      context = {'products':cart_products, 'amount':cart_products.count,'total_price':total_price}
#      return render(request, 'cart.html', context)
@login_required(login_url='/order/')

def order(request):
    if request.method =='POST':
          cart_products= request.session.get('cart_products', [])
          cart_products = Nike.objects.filter(id__in = cart_products)

          total_price = 0
          for i in cart_products:
                total_price +=i.price
          
          order = Order.objects.create( 
          user = request.user,
          total_price = total_price,
          phone_number= request.POST.get('phone_number'),
          message= request.POST.get('message'),
          addres=request.POST.get('address'),
          code=uuid.uuid4()
          )
          products=[]
          for i in cart_products:
               item = OrderItem.objects.create(
                    order = order,
                    product = i,

               )
               products.append(i)
          print(products)
          
          order_data_sender_to_email(request.user,request.POST.get("addres"),request.POST.get("phone_number"),request.POST.get("message"),products)
          # send_mail(
          # f'Заказ от {request.user}',
          # f'АдресЖ{request.POST.get("addres")}\nНомер телефона:{request.POST.get("phone_number")}\nСообщение:{request.POST.get("message")}\nТовар:{[i.title for i in products]}',
          # 'ailir.sunny@gmail.com',
          # ['travel1234509876@gmail.com'], 
          # fail_silently=False,
          # )

          cart_products=request.session.get('cart_products',[])
          cart_products=[]
          request.session['cart_products']=cart_products

    return render(request,'order.html')

    