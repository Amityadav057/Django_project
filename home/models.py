from django.db import models

# Create your models here.
class School(models.Model):
    # name = models.CharField(max_length=50, blank=True, null=True,)
    name = models.CharField(max_length=50, verbose_name="School Name")
    school_unique_code = models.CharField(max_length=20, unique=True, help_text="add unique value", verbose_name="School code")
    address = models.CharField(max_length=30)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f'{self.name}'
    