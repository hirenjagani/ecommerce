from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [

    path('create/', views.order_create, name='order_create'),
    path('myorders/',views.my_orders,name='my_order')
]