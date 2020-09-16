from django.db import models

# Create your models here.


class prediction_new(models.Model):
    pred_date = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=50,unique=True)
    email=models.CharField(max_length=100,unique=True)
    team_name=models.CharField(max_length=100)
    player_name=models.CharField(max_length=100)


class prediction_archive_new(models.Model):
    pred_date = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100,unique=True)
    email=models.CharField(max_length=100,unique=True)
    team_name=models.CharField(max_length=100)
    player_name=models.CharField(max_length=100)