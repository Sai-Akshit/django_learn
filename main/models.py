from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    gender = models.TextField(
        max_length=10, default="none", blank=False, null=False)
    age = models.IntegerField(default=0, blank=False, null=False)
    email = models.EmailField(max_length=100)
    bloodGroup = models.CharField(max_length=10, default="none")

    def __str__(self):
        return self.name
