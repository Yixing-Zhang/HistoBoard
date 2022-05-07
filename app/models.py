from django.db import models


class Figures(models.Model):
    name = models.CharField(max_length=255)
    name2 = models.CharField(max_length=255)
    birth = models.CharField(max_length=255)
    death = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    relations = models.CharField(max_length=255)
    # ...
    def __str__(self):
        return self.name


class Emotions(models.Model):
    emotions = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    figures = models.ManyToManyField(Figures)
    # ...
    def __str__(self):
        return self.emotions

class Locations(models.Model):
    locations = models.CharField(max_length=255)
    # ...
    def __str__(self):
        return self.locations


class Events(models.Model):
    description = models.CharField(max_length=255)
    figures = models.ManyToManyField(Figures)
    emotions = models.ManyToManyField(Emotions)
    locations = models.ManyToManyField(Locations)
    # ...
    def __str__(self):
        return self.description