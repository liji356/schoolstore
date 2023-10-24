from django.db import models

class Form(models.Model):
    name=models.CharField(max_length=250)
    dob=models.TextField()
    age=models.CharField(max_length=250)
    gender= models.CharField(max_length=2, blank=False, null=True)
    phonenumber=models.CharField(max_length=250)
    mailid=models.EmailField(max_length=150)
    address=models.CharField(max_length=250, blank=False, null=True)
    department=models.CharField(max_length=250)
    course=models.CharField(max_length=250)
    material=models.BooleanField(default=True)




    def __str__(self):
        return self.name

# Create your models here.
