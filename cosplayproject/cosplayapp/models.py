from django.db import models
from django.core.validators import RegexValidator
import re

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$',  'Only alphanumeric characters are allowed.')

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['first_name']) < 2:
            errors['first_name'] = 'Please have at least 2 characters in the show name'
        if len(form['last_name']) < 2:
            errors['last_name'] = 'Please have at least 2 characters in the show name'
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Format'
        
        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email address is already in use'
        if len (form['password']) < 8:
            errors['password'] = 'Password must be at least 5 characters long'
        if form['password'] != form['confirm_pw']:
            errors['password'] = 'Password does not match'
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=45)
    confirm_pw = models.CharField(max_length=45)
    objects = UserManager()

class Login(models.Model):
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
