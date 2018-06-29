from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return 'User(%s %s %s %s)' % (User.email, User.password, User.name, User.gender)