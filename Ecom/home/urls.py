from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('', views.index, name='index'),
    path('login/',views.loginf, name='loginf'),
    path('register/', views.register,name='register'),
    path('contact/',views.contact,name='contact'),
    #path('logout/',auth_views.logout,name='logout'),
    path('contact/done',views.contact_done,name='contact_done'),

    # here is my urls
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='passwordchange.html'), name='passwordchange'),
    path('password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='password_change_done'),

]
