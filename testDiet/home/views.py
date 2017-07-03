# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'home.html')

def carb(request):
	return render(request, 'carbohydrate.html')

def fruit(request):
	return render(request, 'fruit.html')

def protein(request):
	return render(request, 'protein.html')

def vegetable(request):
	return render(request, 'vegetable.html')

