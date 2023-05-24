from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('index.html', index_view, name = 'index'), 
    path('menu.html', menu_view, name = 'menu'), 
    path('about.html', about_view, name = 'about'),
    # path('contact', contact_view, name = 'contact'),
    # path('test', test_view, name = 'test'),
]
