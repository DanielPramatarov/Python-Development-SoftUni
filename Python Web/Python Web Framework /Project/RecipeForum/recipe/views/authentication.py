
from django.shortcuts import render,redirect, HttpResponse
from django.http import HttpResponse
from recipe.models import Item
from django.template import loader
from recipe.forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout


def loggin_out(request):
    logout(request)
    return render(request, 'logout.html')
