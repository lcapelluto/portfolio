from __future__ import unicode_literals

from django.db import models

import datetime


class Company(models.Model):
    class Meta:
        verbose_name_plural = 'companies'

    name = models.CharField(max_length=100)
    logo = models.URLField()
    def __str__(self):
        return self.name


class Experience(models.Model):
    class Meta:
        verbose_name_plural = 'experience'

    company = models.ForeignKey(Company)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.title


class Education(models.Model):
    class Meta:
        verbose_name_plural = 'education'

    school = models.CharField(max_length=100)
    expected_graduation = models.CharField(max_length=20)
    major = models.CharField(max_length=200, blank=True)
    GPA = models.FloatField()
    description = models.CharField(max_length=1000, blank=True)
    clubs = models.CharField(max_length=1000, blank=True)
    societies = models.CharField(max_length=1000, blank=True)
    awards = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return self.school


class Recipe(models.Model):
    name = models.CharField(max_length=70)
    image = models.URLField(max_length=500, blank=True)
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    amount = models.FloatField(verbose_name='Ingredient amount', blank=True)
    unit = models.CharField(max_length=15, blank=True)
    prep = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe)

class Direction(models.Model):
    text = models.TextField(blank=True)
    recipe = models.ForeignKey(Recipe, related_name='directions')
