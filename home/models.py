from django.db import models
from django.contrib.auth.models import User

class stocks(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100)

    def __str__(self):
        return self.amount