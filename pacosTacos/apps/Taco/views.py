# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ..Login.models import User

# Create your views here.
def home(request):
	user = User.objects.get(id=request.session.get('id'))
	contents = {
		'user': user
	}
	render(request, 'Taco/taco.html', contents)