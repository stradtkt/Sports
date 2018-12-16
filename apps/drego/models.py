from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import models
import datetime

class UserManager(models.Manager):
    def validate_user(self, postData):
        errors = {}
        # validate first and last name
        if len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
            if len(postData['first_name']) < 2:
                errors['first_len'] = "Your first name needs to be two or more characters"
            if not postData['first_name'].isalpha():
                errors['first_alpha'] = "Your first name needs to be only letters"
        if len(postData['last_name']) < 2 and not postData['last_name'].isalpha():
            if len(postData['last_name']) < 2:
                errors['last_len'] = "Your last name needs to be two or more characters"
            if not postData['last_alpha'].isalpha():
                errors['last_alpha'] = "Your last name needs to be only letters"
        
        #Validate DOB
        if str(postData['DOB']) > str(datetime.datetime.now):
            errors['DOB'] = "The date of birth cannot be in the future"
        elif str(postData['DOB']) == str(datetime.datetime.now):
            errors['DOB'] = "The date of birth cannot be right now"
        # validate email
        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = "Your email is not valid"
        else:
            if User.objects.filter(email=postData['email']):
                errors['email'] = "This email already exists"

        # validate password
        if len(postData['password']) < 8:
            errors['password'] = "Please enter a longer password, needs to be 8 or more characters"
        if postData['password'] != postData['confirm_pass']:
            errors['confirm_pass'] = "Passwords must match"
        return errors
            
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    DOB = models.DateField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return first_name + " " + last_name
