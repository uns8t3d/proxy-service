from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    class Meta:
        db_table = "Users"
    id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=140, default='SOME STRING')
    FirstName = models.CharField(max_length=140, default='SOME STRING')
    LastName = models.CharField(max_length=140, default='SOME STRING')
    Email = models.CharField(max_length=140, default='SOME STRING')
    Password = models.CharField(max_length=140, default='SOME STRING')



