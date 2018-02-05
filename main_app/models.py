# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Snippet(models.Model):

    title = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    #value = models.DecimalField(max_digits=10,
    #                            decimal_places=2)

    def __str__(self):
        return self.title

