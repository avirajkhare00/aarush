# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

import os

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

    return HttpResponse(200)