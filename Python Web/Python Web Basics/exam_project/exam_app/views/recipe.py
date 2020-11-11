from django.shortcuts import render, redirect
from django.http import HttpResponse
from exam_app.models import  Recipe
from exam_app.froms import  RecipeForm , DeleteRecipeForm



def recipe_index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }


    return render(request, 'index.html', context)




def create_recipe(request):

    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'create.html', context)



def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'form': RecipeForm(instance=recipe),
        }

        return render(request, 'edit.html', context)
    else:
        form = RecipeForm(request.POST, instance=recipe)

        if form.is_valid():
            form.save()
            return redirect('/')

        context = {
            'recipe': recipe,
            'form': form,
        }

        return render(request, 'edit.html', context)

   



def delete_recipe(request,pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'recipe': recipe,
            'form': DeleteRecipeForm(instance=recipe),
        }

        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('/')



def detail_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    products = recipe.ingredients.split(", ")

    context = {
            'recipe': recipe,
            'products':products,
        }


    return render(request, 'details.html', context)



    