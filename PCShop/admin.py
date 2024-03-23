from django.contrib import admin

from .models import Product, Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ser', 'category', 'price']
'''
admin.site.register(Product, ProductAdmin)
'''
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']
'''
admin.site.register(Category, CategoryAdmin)
'''