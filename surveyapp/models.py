from django.db import models
from django.contrib.auth.models import User
# from otreeutils.surveys import generate_likert_field




# Create your models here.
class Todo(models.Model):
    learningmode = models.CharField(max_length = 32,default='formal')
    learningactivity = models.CharField(max_length=32, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    ambient = models.CharField(max_length=32, blank=True)
    spatial = models.CharField(max_length=32, blank=True)
    ergonomic = models.CharField(max_length=32, blank=True)
    infrastructure = models.CharField(max_length=32, blank=True)
    people = models.CharField(max_length=32, blank=True)
    rules = models.CharField(max_length=32, blank=True)
    individual = models.CharField(max_length=32, blank=True)
    virtual = models.CharField(max_length=32, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

   

    def __str__(self):
        return str(self.created)
