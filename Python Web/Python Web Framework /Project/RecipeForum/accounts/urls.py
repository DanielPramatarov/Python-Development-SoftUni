from recipe import views
from django.urls import path

from  accounts.views import logOut, register, profiles


app_name = 'accounts'  
urlpatterns = [
    path('logout/',logOut,name='logout'),
    path('register/',register,name='register'),
    path('profiles/',profiles,name='profiles'),

    
    # path('',logOut,name='index'),
   
]    
