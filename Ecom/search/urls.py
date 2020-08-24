from django.conf.urls import url
from . import views
from django.urls import path
from .views import (
        SearchProductView,

        )

urlpatterns = [
     url(r'^$', SearchProductView.as_view(), name='query'),
    #path('search/', views.index, name='index')
     # path('',views.search_query,name='query')
]
