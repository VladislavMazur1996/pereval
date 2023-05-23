from django.contrib.auth.models import User
from django.db import models


class Users(User):
    patronymic = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Passage(models.Model):
    LVL = (('1a', '1A'),
           ('1b', '1Б'),
           ('2a', '2А'),
           ('2b', '2Б'),
           ('3a', '3А'),
           ('3b', '3Б'),
           )

    STATUS = (('NE', 'new'),
              ('PE', 'pending'),
              ('AC', 'accepted '),
              ('RE', 'rejected'),
              )

    status = models.CharField(max_length=2, choices=STATUS, default='NE')
    winter_lvl = models.CharField(max_length=2, choices=LVL)
    summer_lvl = models.CharField(max_length=2, choices=LVL)
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)


class Photo(models.Model):
    passage = models.ForeignKey(Passage, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    name = models.CharField(max_length=255)

