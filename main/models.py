from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')

    def __str__(self) -> str: # dunder metod
        return f'{self.title}'


class Nike(models.Model):
    """ """
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField()
    image =models.ImageField(upload_to='products')
    price = models.PositiveIntegerField(verbose_name='цена')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='категория')
    def __str__(self) -> str:
        return f'{self.title}'

class Images(models.Model):
    sneakers = models.ForeignKey(to=Nike, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sneakers_images', verbose_name='изображеие')
    