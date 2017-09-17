# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

import os
import subprocess

# Create your views here.

@csrf_exempt
def pics_data(request):

    print request.POST

    uploaded_zip = request.POST['timestamp'].split('.')[0]

    # create the folder if it doesn't exist.

    # save the uploaded file inside that folder.

    myfile = request.FILES['zip_file']


    fs = FileSystemStorage(location='open_face_app_1/static/')
    fs.save(uploaded_zip + '.zip', myfile)

    os.system('mkdir /root/openface/training-images/' + uploaded_zip + '/')
    os.system('unzip -d /root/openface/training-images/' + uploaded_zip + '/ ' + '/root/openface/aarush/open_face_server/open_face_app_1/static/' + uploaded_zip + '.zip')
    os.system('mv /root/openface/training-images/' + uploaded_zip + '/data/*.jpg ' '/root/openface/training-images/' + uploaded_zip + '/')
    os.system('rm -rf /root/openface/training-images/' + uploaded_zip + '/data/')

    os.system('python /root/openface/trainer_script_django.py')

    return HttpResponse(200)

@csrf_exempt
def recognize_person(request):

    person_pic = request.FILES['image']
    ticket_number = request.POST['ticket_number']

    fs = FileSystemStorage(location='open_face_app_1/static/open_tickets')
    fs.save(ticket_number + '.jpg', person_pic)

    #os.system('cp open_face_app_1/static/open_tickets/' + ticket_number + '.jpg' + '')


    process = subprocess.Popen(["/root/openface/demos/classifier.py infer ./generated-embeddings/classifier.pkl " + "open_face_app_1/static/open_tickets/" + ticket_number + '.jpg'], stdout=subprocess.PIPE)
    result = process.communicate()[0]

    print result

    return HttpResponse(result)
