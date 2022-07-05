from django.urls import path
from . import views

app_name = 'ggs_app'
urlpatterns = [
    path('', views.main, name='main'),
    path('shirts/', views.shirts, name='shirts'),
    path('socks/', views.socks, name='socks'),
    path('supplements/', views.supplements, name='supplements'),
    path('cart/', views.cart, name='cart'),
    path('search/', views.search, name='search'),
    path('result/', views.result, name='result'),
]
