from django.urls import path
from website.views import *
from . import views
from django.contrib.auth import views as auth_views


app_name = 'website'


urlpatterns = [
    path('', index_view, name = 'index'), 
    path('menu.html', menu_view, name = 'menu'), 
    path('about', about_view, name = 'about'),
    
    #path('index.html', contact_view, name = 'contact'), 
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:pk>/', views.product, name='product'),
    path('store/', views.store, name='store'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('to-bank/<int:order_id>/', views.to_bank, name='to_bank'),
    path('callback/', views.callback, name='callback'),
    
    path('test', test_view, name = 'test'),
]
