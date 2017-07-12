# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from home.models import Data

# Create your views here.

def index(request):

	return render(request, 'home.html')

def carb(request):
    carb = Data.objects.filter(type='carbohydrate')
    carb_data = list(carb)
    context = {"carb":carb_data,}
    return render(request, 'carbohydrate.html',context)

def fruit(request):
    fruit = Data.objects.filter(type='fruit')
    fruit_data = list(fruit)
    context = {"fruit":fruit_data,}
    return render(request, 'fruit.html',context)


def protein(request):
    protein = Data.objects.filter(type='protein')
    protein_data = list(protein)
    context = {"protein":protein_data,}
    return render(request, 'protein.html',context)


def vegetable(request):
    vegetable = Data.objects.filter(type='vegtable')
    veg_data = list(vegetable)
    context = {"vegetable":veg_data,}
    return render(request, 'vegetable.html',context)


