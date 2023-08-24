from django.shortcuts import render
from . import models
import os

currentDir = str(os.path.abspath(__file__))[:-8]

# Create your views here.
def peoplePage(request, name):
    urlName = name
    
    # Get people info
    peopleDir = currentDir + 'peoples\\' + urlName + "\\"
    file = open(peopleDir + "profile.txt", "r", encoding='UTF-8')
    
    name = file.readline().split('//')[0].strip()
    position = file.readline().split('//')[0].strip()
    gitId = file.readline().split('//')[0].strip()
    gitUrl = file.readline().split('//')[0].strip()
    imgPath = 'assets/profileImg/' + file.readline().split('//')[0].strip()
    
    return render(request, "people-page.html", {'urlName': urlName, 'name':name, 'position': position, 'gitId':gitId, 'gitUrl': gitUrl, 'imgPath': imgPath})

def pptIndexPage(request, name):
    
    urlName = name
    
    # Get people info
    peopleDir = currentDir + 'peoples\\' + urlName + "\\"
    file = open(peopleDir + "profile.txt", "r", encoding='UTF-8')
    
    name = file.readline().split('//')[0].strip()
    position = file.readline().split('//')[0].strip()
    gitId = file.readline().split('//')[0].strip()
    gitUrl = file.readline().split('//')[0].strip()
    imgPath = 'assets/profileImg/' + file.readline().split('//')[0].strip()
    
    ppts = models.SeminarPPT.objects.all()
    print(len(ppts))
    
    return render(request,"ppt-index.html", {'urlName': urlName, 'name':name, 'position': position, 'gitId':gitId, 'gitUrl': gitUrl, 'imgPath': imgPath, 'pptList':ppts})