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
    introIdx = 1
    careerIdx = -1

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
            peopleDict[introIdx] = content
            introIdx += 1
        elif category == 'career':
            peopleDict[careerIdx] = content
            careerIdx -= 1
        else:
            peopleDict[category]=content

    peopleDict['introNums'] = introIdx - 1
    peopleDict['careerIdx'] = careerIdx + 1
    print(peopleDict)
    
    return render(request, "people-page.html", peopleDict)