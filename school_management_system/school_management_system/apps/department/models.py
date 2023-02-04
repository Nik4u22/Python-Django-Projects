from django.db import models

# Create your models here.

# Create Department Model
class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

# To show department name in url
def __str__(self):
    return self.name

