from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)

class Research(models.Model):
    title = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    abstract = models.TextField()
    document_file = models.CharField(max_length=50)
    date = models.DateField()

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    research = models.ForeignKey(Research, on_delete=models.CASCADE)
    comments = models.TextField()
    date = models.DateField()

class Authors(models.Model):
    research = models.ForeignKey(Research, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
