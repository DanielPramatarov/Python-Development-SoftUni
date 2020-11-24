from recipe import views
from django.urls import path

from recipe.views.recipes import  index, create_recipe, user_recipes, delete_recipe, edit_recipe , detail_recipe , all_recipes
# from recipe.views.authentication import  loggin_out


app_name = 'recipe'  
urlpatterns = [
    path('',views.index,name='index'),
   
    
    #add Recipe
    path('add/',views.create_recipe, name='create'),
    #Currently logged in user's recipes
    path('my_recipe/',views.user_recipes, name='my_recipe'),
    #List all recipes of all users
    path('all_recipe/',views.all_recipes, name='all_recipe'),

   
    #edit Recipe
    path('edit/<int:pk>/',views.edit_recipe,name='edit'),
    #delete Recipe
    path('delete/<int:pk>/',views.delete_recipe,name='delete'),
    #detail Recipe
    path('detail/<int:pk>/',views.detail_recipe,name='detail'),
]    
