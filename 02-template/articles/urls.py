from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dinner/', views.dinner),
    path('search/', views.search),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('articles/<int:num>/', views.detail),
]
