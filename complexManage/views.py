# from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(resquest):
	# template = loader.get_template('complexManage/index.html')
	return render(resquest, 'complexManage/index.html')

# Create your views here.
