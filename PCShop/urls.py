from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path('product/<int:id>', views.product, name='product'),
    path('cat/', views.not_cat),
    path('', views.index, name='home'),
    path('<int:product_id>/buy/', views.make_order,name='make_order')
]
