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
    
    name = file.readline().split('//')[0].strip()
    position = file.readline().split('//')[0].strip()
    gitId = file.readline().split('//')[0].strip()
    gitUrl = file.readline().split('//')[0].strip()
    imgPath = 'assets/profileImg/' + file.readline().split('//')[0].strip()
    
    pptList = models.SeminarPPT.objects.all()
    if len(pptList) > 5:
        pptList = pptList[::-1]
        pptList = pptList[0:5]
    
    return render(request, "people-page.html", {'urlName': urlName, 'name':name, 'position': position, 'gitId':gitId, 'gitUrl': gitUrl, 'imgPath': imgPath, 'pptList':pptList})