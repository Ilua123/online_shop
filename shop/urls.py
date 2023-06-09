"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from shop.settings import MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop, name='home'),
    path('detal/<int:id>', detal, name='detal'),
    path('favorites/<int:id>', faforites, name='favorites'),
    path('favorit/', favorit, name='favorit'),
    path('favorit_delet/<int:id>', delet_favorites, name='favorit_delet'),
    path('carzina/', carzina, name='carzina'),
    path('carzines/<int:id>', carzines, name='carzines'),
    path('about_us/', about_us, name='about_us'),
    path('register/', sign_in, name='sing_in'),
    path('sing_up/', sign_up, name='sing_up'),
    path('logout/', logout, name='logout'),
    path('order/', order, name='order'),
]



urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
