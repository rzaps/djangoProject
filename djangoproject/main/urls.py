from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    path('catalog/', views.catalog, name='catalog'),
    path('shop/', views.shop, name='shop'),
]
