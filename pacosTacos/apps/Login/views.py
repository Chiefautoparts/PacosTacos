# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import  User

# Create your views here.
def index(request):
	print '**Login Index**' * 250
	return render(request, 'Login/index.html')

def register(request):
	print '**Register User**' * 250
	results = User.objects.registerUser(request.POST)
	if not results['status']:
		for error in reults['errors']:
			messages.error(request, error)
		return redirect('login:index')
	request.session['id'] = reults['user'].id
	return redirect('login:success')


def login(request):
	print '**Login User**' * 250
	results = User.objects.loginUser(request.POST)
	if not results['status']:
		for error in results['errors']:
			messages.error(request, error)
		return redirect('login:index')
	request.session['id'] = results['user'].id
	return redirect('login:success')

def success(request):
	# user = User.objects.get(id=request.session.get('id'))
	# contents = {
	# 	'user': user
	# }
	return redirect('taco:home')