# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from collections import OrderedDict
from home.models import Data, Food
from django.http import HttpResponse
import os, csv, subprocess

# Create your views here.

def index(request):
#	batcmd = "/opt/ibm/ILOG/CPLEX_Studio_Community127/opl/bin/x86-64_linux/oplrun -v MODEL.mod /var/www/DATA.dat"
 #       output = subprocess.check_output(batcmd, shell=True)
#	context = {'output':output,}
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
    carbohydrate = list(Food.objects.filter(type='carb').values())
    vegetable = list(Food.objects.filter(type='vegetable').values())
    context = {"fruit":fruit,"protein":protein,"vegetable":vegetable,"carb":carbohydrate}
    os.system("echo 'helloooo' > hello.txt")

    return render(request, 'diet.html', context)

def result(request):

    # Delete data file if exists
    try:
        os.remove('DATA.dat')
    except OSError:
        pass

    try:
        os.remove('/var/www/oplresult.csv')
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
    
    foodlist = ['choice1','choice2','choice3','choice4']
    for x in foodlist:
        if x in context:
            for i in context[x]:
                current = list(Food.objects.filter(foodname=i).values())
                for key in data:
                    data[key].append(current[0][key])
        else:
            continue

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

    cmdd = "cd /var/www/html/dietoptimization/testDiet; /opt/ibm/ILOG/CPLEX_Studio_Community127/opl/bin/x86-64_linux/oplrun -v MODEL.mod /var/www/DATA.dat | grep -A 2 yAmount | cut -d '[' -f2 | cut -d ']' -f1 | tr -d '\n' | tr -s '[[:space:]]' ','"
    output = subprocess.check_output(cmdd, shell=True)
    f = open('oplresult.csv', 'a')
    f.write(output)
    f.close()
    with open('oplresult.csv', 'rb') as f:
       reader = csv.reader(f, delimiter=str(u','))
       mylist = list(reader)
    data['opti'] = mylist[0]
    final = zip(data['foodname'],data['opti'])

    return render(request, 'result.html', {'final':final,})


