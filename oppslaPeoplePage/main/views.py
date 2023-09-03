from django.shortcuts import render, redirect
from . import models
import os
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage

currentDir = str(os.path.abspath(__file__))[:-8]

# Create your views here.

# 기본 페이지
def peoplePage(request, name):
    urlName = name
    # Get people info
    peopleDir = currentDir + 'peoples\\' + urlName + "\\"
    print(peopleDir)
    file = open(peopleDir + "profile.txt", "r", encoding='UTF-8')

    peopleDict = {'urlName':urlName}

    while True:
        text = file.readline().split('#')[0].strip()
        try:
            category, content = text.split('::')
        except:
            category=''; content=''
            
        if category=='end' and content=='end':
            break
        elif category == '':
            continue
        elif category == 'intro':
            try:
                peopleDict['intro'] += '\n\n'+content
            except:
                peopleDict['intro'] = content
        elif category == 'career':
            try:
                peopleDict['career'] += '\n\n* '+content
            except:
                peopleDict['career'] = '* '+content
        else:
            peopleDict[category]=content
    
    return render(request, "people-page.html", peopleDict)