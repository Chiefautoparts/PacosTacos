# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
import re
from django.db import models

# Create your models here.

class UserManager(models.Manager):
	def registerUser(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		if not postData['name'] or len(postData['name']) < 3:
			results['status'] = False
			results['errors'].append('Enter and name that is more than 3 characters in length')
		if not postData['username'] or len(postData['username']) < 3:
			results['status'] = False
			results['errors'].append('Username must be more than 3 characters')
		if not re.match(r'(^[a-zA_Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', postData['email']):
			results['status'] = False
			results['errors'].append('INVALID EMAIL!!!!!!!!')
		if not postData['password'] or len(postData['password']) < 8:
			results['status'] = False
			results['errors'].append('Password must be more than 8 characters')
		if postData['confPassword'] != postData['password']:
			results['status'] = False
			results['errors'].append('Passwords do not match')

		if results['status'] is False:
			return results
		user = User.objects.filter(email=postData['email'])

		if user:
			results['status'] = False
			results['errors'].append('Failed to register new User')
		if results['status']:
			hashPass = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
			user = User.objects.create(
				name=postData['name'],
				username=postData['username'],
				email=postData['email'],
				password=hashPass)
			user.save()
			results['user'] = user
		return results

	def loginUser(self, postData):
		results = {'status': True, 'errors': [], 'uesr': None}
		user = User.objects.filter(email=postData['email'])
		try:
			user[0]
		except IndexError:
			results['status'] = False
			results['errors'].append('None of this is correct. I give up Just Leave')
			return results
		if user[0]:
			if user[0].password != bcrypt.hashpw(postData['hashPass'].encode(), user[0].password.encode()):
				results['status'] = False
				results['errors'].append('Everything has failed. Everybody Panic and Run!!!!!!!')
			else:
				results['user'] = user[0].id
		else:
			results['status'] = False
		return results

class User(models.Model):
	name = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()