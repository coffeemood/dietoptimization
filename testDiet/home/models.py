# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Food(models.Model):
    id = models.IntegerField(primary_key=True)
    foodname = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    satfat = models.DecimalField(max_digits=5, decimal_places=2)
    fibre = models.DecimalField(max_digits=5, decimal_places=2)
    sugar = models.DecimalField(max_digits=5, decimal_places=2)
    sodium = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.foodname

    class Meta:
        managed = False
        db_table = 'food'

class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    energy = models.CharField(max_length=100)
    protein = models.CharField(max_length=100)
    fat = models.CharField(max_length=100)
    sugar = models.CharField(max_length=100)
    fibre = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'data'

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    f1 = models.CharField(db_column='F1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f2 = models.CharField(db_column='F2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f3 = models.CharField(db_column='F3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f4 = models.CharField(db_column='F4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f5 = models.CharField(db_column='F5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f6 = models.CharField(db_column='F6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f7 = models.CharField(db_column='F7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f8 = models.CharField(db_column='F8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    f9 = models.CharField(db_column='F9', max_length=100, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'users'
