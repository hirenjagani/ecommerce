from django.contrib import admin
from django.urls import path,include
from . import views

from django.conf.urls import url
urlpatterns = [

    path('product/',views.productlist,name='productlist'),
    path('product/<int:pk>/', views.productdetail,name='productdetail'),

]
