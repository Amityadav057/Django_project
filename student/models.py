from django.db import models
from home.models import School

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    student_id = models.IntegerField(unique=True)
    number = models.PositiveBigIntegerField(default=0)
    school  = models.ForeignKey(School, on_delete=models.SET_NULL ,null=True)


    def __str__(self):
        return f'{self.name}'


# on delete
'''
CASCADE
SET_NULL
Restrict
'''