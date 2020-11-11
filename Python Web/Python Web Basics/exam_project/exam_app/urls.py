from django.urls import path
from exam_app.views.recipe import  *

urlpatterns = [
    path('', recipe_index, name='index'),
    path('create/', create_recipe, name='create_recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit_recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete_recipe'),
    path('details/<int:pk>/', detail_recipe, name='detail_recipe'),
    
    
]
