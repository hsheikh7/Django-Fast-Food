from django.urls import path 
from . import views 

app_name = 'accounts'

urlpatterns = [
    #singup 
    # path('signup', views.sign_view, name = 'login')
    path('signup', views.signup_view, name = 'signup')


]