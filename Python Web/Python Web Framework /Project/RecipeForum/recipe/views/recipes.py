
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from recipe.models import Item
from django.template import loader
from recipe.forms import ItemForm, DeleteRecipeForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# from django.contrib.auth import logout
from django import forms


def create_recipe(request):

    form = ItemForm()
    form.fields['item_name'].widget.attrs.update({
            'placeholder': 'Enter Recipe Name'
        })
    initial_user = {'user_name': request.user}
    form = ItemForm(initial=initial_user)
    if request.method == 'POST':
        form = ItemForm(request.POST)
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
    all_recipes = Item.objects.all()

    context = {
            'recipe': recipe,
            'user_name': request.user,
            # 'recipe': recipe,
            # 'products':products,
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
        form = ItemForm(request.POST, instance=recipe)

        if form.is_valid():
            form.save()
            return redirect('/my_recipe/')

        context = {
            'recipe': recipe,
            'form': form,
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
        print(recipe.user_name)

        if recipe.user_name == request.user:
            users_recipes.append(recipe)

    context = {'user_recipes': users_recipes}

    for i in users_recipes:
        i.item_time_to_cook
    return render(request, 'my_recipes.html', context)


def all_recipes(request):
    all_recipes = Item.objects.all()


 

    context = {'all_recipes': all_recipes}

 
    return render(request, 'all_ricepes.html', context)
