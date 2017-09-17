# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import time
import requests
import json
from django.core.files.storage import FileSystemStorage


from app1.models import NewPersonObj

# Create your views here.

@csrf_exempt
def get_person_data(request):

    new_person = NewPersonObj()

    person_pic = request.FILES['first_image']

    timestamp = time.time()

    fs = FileSystemStorage(location='app1/static/open_tickets')
    fs.save(str(timestamp) + '.jpg', person_pic)

    new_person.timestamp = timestamp
    new_person.save()

    openface_app_url = "http://127.0.0.1:3004/pics_data/"


    data = {
        "timestamp" : timestamp,
    }

    files = {
        'zip_file' : request.FILES['image_zip_file'].read()
    }


    r = requests.post(openface_app_url, data=data, files=files)

    if r.status_code == 200:

        print "successfully sent"

    else:

        print "debug step to send data to nodejs"


    return HttpResponse(200)

@csrf_exempt
def enquire_person(request):

    openface_app_url = "http://127.0.0.1:3004/recognize_person/"

    data = {
        "ticket_number": time.time(),
    }

    files = {
        'image': request.FILES['image'].read()
    }

    r = requests.post(openface_app_url, data=data, files=files)

    if r.status_code == 200:

        print "successfully sent"

        print r.text

        return HttpResponse(r.text.split(' ')[:-4])

    else:

        print "debug step to send data to nodejs"