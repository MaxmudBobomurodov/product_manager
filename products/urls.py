from django.urls import path

from products.views import products_list

app_name = 'products'

urlpatterns = [
    path('', products_list, name='list'),
    path('add/', products_list, name='add'),
    path('update/<int:product_id>/', products_list, name='update'),
    path('delete/<int:product_id>/', products_list, name='delete')
]