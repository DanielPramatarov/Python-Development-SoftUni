from recipe import views
from django.urls import path

from  accounts.views import logOut, register, profiles, User_Profile,edit_profile, SignUp, detailProfile , userRecipes


app_name = 'accounts'  
urlpatterns = [
    path('logout/',logOut,name='logout'),
    path('login/', SignUp, name="login"),  
    path('register/',register,name='register'),
    path('profiles/',profiles,name='profiles'),
    path('profile/',User_Profile,name='User_Profile'),
    path('editProfile/',edit_profile,name='edit_profile'),
    # path('detailProfile/pk/',detailProfile,name='detail_profile'),
    # path('profile/(?P<username>[a-zA-Z0-9]+)$', detailProfile, name='detail_profile'),
    path('viewProfile/<int:pk>/',detailProfile,name='detail_profile'),
    path('MyRiceps/<int:pk>/',userRecipes,name='user_recipes'),


    
    # path('',logOut,name='index'),
   
]    
