from django.contrib.auth.models import User
from django.db import models


class Users(User):
    patronymic = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    def __str__(self):
        return f'координаты: {self.latitude}, {self.longitude}, высота: {self.height}'


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
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.connect.join([self.beauty_title, self.title, self.other_titles])}"


class Photo(models.Model):
    passage = models.ManyToManyField(Passage)
    image = models.ImageField(upload_to="photos", blank=True)
    name = models.CharField(max_length=255)

