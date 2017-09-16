# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def get_person_data(request):

    print request.POST
    print request.data

    return HttpResponse(200)