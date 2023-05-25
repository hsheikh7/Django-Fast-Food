from django.urls import path 
from . import views
from accounts.views import *

app_name = 'accounts' 

urlpatterns = [
    # login
    path('login', login_view, name='login'),

    # logout
    path('logout',views.logout_view, name='logout'),
    
    # registration / signup
    path('signup/',views.signup_view, name='signup')
    
]