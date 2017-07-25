# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import Context
import os

# Create your views here.

def index(request):
	return render(request, 'index.html')

def readFile(request):
	import os
	module_dir = os.getcwd()
	f=open('test2.txt','a+')
	f.write("Here's a footprint AT " + module_dir )
	f.close()
	f=open('test2.txt','r+')
	var=f.read()
	context = {"dirz":module_dir, "txtf":var}
	return render(request, 'index.html', context)  # get current directory

	# file_path = os.path.join(module_dir, 'baz.txt')
	#
	# handle=open('file','r+')
	# var=handle.read()
	# print var
