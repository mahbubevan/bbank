from django.db import models
from django.urls import reverse

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    blood_group = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    helping_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("user:profile",kwargs={"pk":self.pk})
