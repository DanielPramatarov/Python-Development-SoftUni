
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from recipe.models import Item
from django.template import loader
from recipe.forms import ItemForm, DeleteRecipeForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
# from django.contrib.auth import logout
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


def like(request, pk):
    recipe = Item.objects.get(pk=pk)
    if recipe.Dislikes.filter(id=request.user.id).exists():
        recipe.Dislikes.remove(request.user)
    recipe.likes.add(request.user)
    return HttpResponseRedirect(reverse('recipe:detail', args=[str(pk)]))



def dislike(request, pk):
    recipe = Item.objects.get(pk=pk)

    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
    recipe.Dislikes.add(request.user)
    return HttpResponseRedirect(reverse('recipe:detail', args=[str(pk)]))


def create_recipe(request):

    form = ItemForm()

    form.fields['item_name'].widget.attrs.update({
            'placeholder': 'Enter Recipe Name'
        })
    initial_user = {'user_name': request.user}
    form = ItemForm(initial=initial_user)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.fields['user_name'].widget = forms.HiddenInput()

            form.save()

            return redirect('/my_recipe/')


    context = {'form': form, 'initial_user': initial_user['user_name']}
    return render(request, 'create.html', context)



def delete_recipe(request, pk):
    recipe = Item.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'form': DeleteRecipeForm(instance=recipe),
        }

        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('/my_recipe/')



def detail_recipe(request, pk):
    recipe = Item.objects.get(pk=pk)
    # products = Item.ingredients.split(", ")
    # initial_user = {'user_name': request.user}
    likes = recipe.likes.count()
    dislikes  = recipe.Dislikes.count()
    all_recipes = Item.objects.all()
    products = recipe.ingredients.split(", ")

    context = {
            'recipe': recipe,
            'user_name': request.user,
            'products':products,
            'likes': likes,
            'dislikes':dislikes,
        }


    return render(request, 'detail.html', context)




def edit_recipe(request, pk):
    recipe = Item.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'form': ItemForm(instance=recipe),
        }

        return render(request, 'edit.html', context)
    elif request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=recipe)

        if form.is_valid():
            form.save()
            return redirect('/my_recipe/')

        context = {
            'recipe': recipe,
            'form': ItemForm(    instance=recipe),
        }

        return render(request, 'edit.html', context)


def index(request):
    item_list = Item.objects.all()

    context = {
        'item_list': item_list,
    }
    return render(request, "index.html", context)


def user_recipes(request):
    all_recipes = Item.objects.all()
    users_recipes = []

    for recipe in all_recipes:

        if recipe.user_name == request.user:
            users_recipes.append(recipe)
    paginator = Paginator(users_recipes, 6) 

    page_number = request.GET.get('page')
    users_recipes = paginator.get_page(page_number)


    context = {'user_recipes': users_recipes}

 
    return render(request, 'my_recipes.html', context)


def all_recipes(request):
    all_recipes = Item.objects.all()
    


    paginator = Paginator(all_recipes, 6) 

    page_number = request.GET.get('page')
    all_recipes = paginator.get_page(page_number)

    context = {
        'all_recipes': all_recipes,
        # 'page_obj':page_obj,
        }


 
    return render(request, 'all_ricepes.html', context)
