from . import views
from django.urls import path
 
app_name = 'recipe'  
urlpatterns = [
    # #/food/
    path('',views.index,name='index'),
    # #/food/1
    # path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    # path('item/',views.item,name='item'),
    # # add items
    
   
    # path('add',views.CreateItem.as_view(),name='create_item'),
    # # edit
    # path('update/<int:id>/',views.update_item,name='update_item'),
    # #delete
    # path('delete/<int:id>/',views.delete_item,name='delete_item'),
]    
