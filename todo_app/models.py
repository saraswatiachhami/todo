from django.db import models

# Create your models here.

#python manage.py makemigrations
#python manage.py migrate

class Todo(models.Model): #PascalCase
    title = models.CharField(max_length=200)  #Varchar char

    def __str__(self):
        return self.title