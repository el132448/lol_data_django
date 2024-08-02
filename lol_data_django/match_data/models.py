from django.db import models

class Player(models.Model):
    id = models.AutoField(unique=True)  # This will still auto-increment but won't be the primary key
    puuid = models.CharField(max_length=100, primary_key=True)  # Define puuid as the primary key
    summoner_name = models.CharField(max_length=100, unique=True)
    tag_line = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    mass_region = models.CharField(max_length=20)

