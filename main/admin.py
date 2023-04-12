from django.contrib import admin
from .models import Category, Nike, Images,OrderItem,Order
# Register your models here.

class ImagesInline(admin.TabularInline):
    model = Images

@admin.register(Nike)
class NikeAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]
    list_display = ('title', 'price')

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(Nike)
# admin.site.register(Images)