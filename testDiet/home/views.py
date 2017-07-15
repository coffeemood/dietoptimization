# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from collections import OrderedDict
from home.models import Data, Food
import os, csv, subprocess

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

def diet(request):
    fruit = list(Food.objects.filter(type='fruit').values())
    protein = list(Food.objects.filter(type='protein').values())
    carbohydrate = list(Food.objects.filter(type='fruit').values())
    vegetable = list(Food.objects.filter(type='vegetable').values())
    context = {"fruit":fruit,"protein":protein,"vegetable":vegetable,"carb":carbohydrate}
    return render(request, 'diet.html', context)

def result(request):

    # Delete data file if exists
    try:
        os.remove('DATA.dat')
    except OSError:
        pass

    # Collect all choices
    context = {k: v[0] if len(v) == 1 else v for k, v in request.POST.lists()}
    def removekey(d, key):
        r = dict(d)
        del r[key]
        return r
    if "csrfmiddlewaretoken" in context:
        context = removekey(context, "csrfmiddlewaretoken")

    data = {'foodname':[],'cost':[],'protein':[],'fibre':[],'sugar':[],'satfat':[]}

    for i in context['choice']:
        current = list(Food.objects.filter(foodname=i).values())
        for key in data:
            data[key].append(current[0][key])

    # Pasting content of dictionary to data file in OPL format
    for i in data:
        s1,s2 = '',''
        if i == 'foodname':
            s1 = ','.join(data[i])
            s2 = 'Food = {%s};\n' % s1
            f = open('DATA.dat', 'a')
            f.write(s2)
            f.close()
        else:
            l1 = ['{:.2f}'.format(x) for x in data[i]]
            s1 = ','.join(l1)
            s2 = '%s = [%s];\n' % (i,s1)
            f = open('DATA2.dat', 'a')
            f.write(s2)
            f.close()
    os.system('cat DATA2.dat >> DATA.dat; rm DATA2.dat')

    output = subprocess.check_output("cd /home/ubuntu/dietoptimization/testDiet; /opt/ibm/ILOG/CPLEX_Studio_Community127/opl/bin/x86-64_linux/oplrun -v MODEL.mod DATA.dat | grep -A 2 yAmount | cut -d '[' -f2 | cut -d ']' -f1 | tr -d '\n' | tr -s '[[:space:]]' ' ' > oplresult.csv", shell=True)


    with open('oplresult.csv', 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)

    return render(request, 'result.html', data)


