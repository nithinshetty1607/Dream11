from django.db import models

# Create your models here.


class prediction(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    player_name=models.CharField(max_length=100)