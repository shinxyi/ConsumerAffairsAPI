from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
import re, bcrypt, uuid

class UserManager(models.Manager):
    def register(self, username, first_name, last_name, email, password, confirm_password):
        if password != confirm_password:
            return {'error': 'Password match error.'}
        else:
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = {
                'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': pw_hash,
                'auth_token': uuid.uuid4()
            }
            return {'user': user}

    def login(self, email, password):
        valid=True
        errors=[]
        pattern = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(email) < 1:
            errors.append("Email field cannot be empty!")
            valid=False
        elif not pattern.match(email):
            errors.append("Invalid Email Format!")
            valid=False

        user = User.userManager.filter(email=email)
        if len(user)<1:
            errors.append("Invalid Email")
            valid=False
        elif bcrypt.hashpw(password.encode(), user[0].password.encode()) == user[0].password.encode():
            return {'user': user[0].auth_token}
        else:
            errors.append("Invalid email/password combination.")
        return {'errors': errors }

def validateName(value):
    if len(value)< 3:
        raise ValidationError(
          '{} must be longer than 2 characters'.format(value)
          )
    elif not value.isalpha():
        raise ValidationError(
          '{} can only contain letters'.format(value)
          )

def validatePasswordLength(value):
    if len(value)< 8:
        raise ValidationError(
          '{} must be longer than 8 characters'.format(value)
          )

class User(models.Model):
    username = models.CharField(max_length=45,unique=True)
    first_name = models.CharField(max_length=45, validators = [validateName])
    last_name = models.CharField(max_length=45, validators = [validateName])
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=100, validators = [validatePasswordLength])
    confirm_password=models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    auth_token= models.CharField(max_length=100, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    userManager = UserManager()
