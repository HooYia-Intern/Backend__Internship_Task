from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.name}"
