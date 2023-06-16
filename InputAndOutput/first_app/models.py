from django.db import models

# Create your models here.
class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    class_name = models.CharField(max_length=10)
    address = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    