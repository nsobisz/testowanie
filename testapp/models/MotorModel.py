from django.db import models

from datetime import datetime, date, timedelta

from django.urls import reverse

# Create your models here.
class Motor(models.Model):
    nameMotor = models.CharField(max_length=255)
    content = models.TextField(default="")
    price = models.PositiveSmallIntegerField(default=1)
    year = models.PositiveSmallIntegerField(default=2000)
    imgMotor = models.ImageField(upload_to='mediacar', blank=True, null = True)
    for_sale = models.BooleanField(default=True)
    color = models.CharField(max_length=100, default="white")

    def __str__(self):
        return self.nameMotor

    def is_cheap(self):
        return self.price < 10000

    def is_old(self):
        return self.year < 2010
    def string_representation(self):
        return  f"{self.nameMotor} for {self.price}"

    def buy(self):
        self.for_sale = False
        self.save()

    def change_color(self, new_color):
        self.color = new_color
        self.save()

    def add_promotion(self, procent):
        self.price = self.price - self.price * (procent * 0.01)
        self.save()


