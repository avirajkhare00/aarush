# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class NewPersonObj(models.Model):

    timestamp = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    father_name = models.CharField(max_length=80, blank=True, null=True)
    aadhar_number = models.CharField(max_length=20, blank=True, null=True)
    is_found = models.BooleanField(default=False)

    def __unicode__(self):

        return self.timestamp