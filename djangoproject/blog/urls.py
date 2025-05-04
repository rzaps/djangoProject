from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog'),
    path('new_post', views.new_post, name='new_post'),
]
