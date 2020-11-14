from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
# Create your views here.





# def create_item(request):
#     form = ItemForm(request.POST or None)
 
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
 
#     return render(request,'food/item-form.html',{'form':form})




# def detail(request,item_id):
#     item = Item.objects.get(pk=item_id)
#     context ={
#         'item':item,
#     }
 
#     return render(request,'food/detail.html',context)
 

#  def delete_item(request,id):
#         item = Item.objects.get(id=id)
 
#     if request.method == 'POST':
#         item.delete()
#         return redirect('food:index')
 
#     return render(request,'food/item-delete.html',{'item':item})

#  def update_item(request,id):
#         item = Item.objects.get(id=id)
#     form = ItemForm(request.POST or None, instance=item)
 
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
 
#     return render(request,'food/item-form.html',{'form':form,'item':item})
 