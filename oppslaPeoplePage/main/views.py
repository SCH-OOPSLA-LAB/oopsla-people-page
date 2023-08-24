from django.shortcuts import render
import os

currentDir = str(os.path.abspath(__file__))[:-8]

# Create your views here.
def test(request):
    urlName = (str(request).split("'")[1].split('/')[2])
    
    # Get people info
    peopleDir = currentDir + 'peoples\\' + urlName + "\\"
    file = open(peopleDir + "profile.txt", "r", encoding='UTF-8')
    
    name = file.readline().split('//')[0].strip()
    position = file.readline().split('//')[0].strip()
    gitId = file.readline().split('//')[0].strip()
    gitUrl = file.readline().split('//')[0].strip()
    imgPath = 'assets/profileImg/' + file.readline().split('//')[0].strip()

    print(imgPath)
    
    return render(request, "people-page.html", {'name':name, 'position': position, 'gitId':gitId, 'gitUrl': gitUrl, 'imgPath': imgPath})