from django.contrib import admin
from .models import Category, Nike, Images
# Register your models here.

class ImagesInline(admin.TabularInline):
    model = Images

@admin.register(Nike)
class NikeAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]
    list_display = ('title', 'price')

admin.site.register(Category)
# admin.site.register(Nike)
# admin.site.register(Images)