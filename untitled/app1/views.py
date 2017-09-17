# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import time
import requests

from app1.models import NewPersonObj

# Create your views here.

@csrf_exempt
def get_person_data(request):

    print request.POST

    new_person = NewPersonObj()

    timestamp = time.time()

    new_person.timestamp = timestamp
    new_person.save()

    nodejs_url = "http://127.0.0.1:3004/pics_data"

    data = {
        "timestamp" : timestamp,
        "image_data" : request.POST
    }

    r = requests.post(nodejs_url, data=data)

    if r.status_code == 200:

        print "successfully sent"

    else:

        print "debug step to send data to nodejs"


    return HttpResponse(200)
