# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import os

# Create your views here.

@csrf_exempt
def pics_data(request):

    print request.POST

    uploaded_folder = request.FILES['file'].name[:-3]

    # create the folder if it doesn't exist.

    # save the uploaded file inside that folder.

    fout = open('training-images-zip', 'wb+')
    # Iterate through the chunks.
    for chunk in fout.chunks():
        fout.write(chunk)
    fout.close()

    return HttpResponse(200)