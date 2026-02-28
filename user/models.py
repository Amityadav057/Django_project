from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userbalance1(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, unique=True)
    balance = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username

    # class Meta:
    #     unique_together = ['user','balance']


class Userbalance2(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    balance = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username