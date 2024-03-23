from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False,verbose_name='наименование')
    ser = models.CharField(max_length=50, unique=True, blank=False,verbose_name='серия')
    category = models.ForeignKey(
        'Category',
        null=True,
        verbose_name='категория',
        on_delete=models.SET_NULL
    )
    price = models.FloatField(verbose_name='Цена')
    
    def __str__(self):
        return (
            f'Категория: {self.category}<br>'
            + f'Название и серия: {self.name} {self.ser}'
        )

class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='наименование')
    image = models.ImageField(upload_to='categories', verbose_name='изображение')

    def __str__(self):
        return(
            f'{self.name}'
        )

class Order(models.Model):
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    product = models.ForeignKey(
        'Product',
        null=False,
        on_delete=models.DO_NOTHING
    )