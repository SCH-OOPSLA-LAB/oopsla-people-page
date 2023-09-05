from django.shortcuts import render, redirect
from . import models
import os, shutil
from django.http import FileResponse
from django.conf import settings

# ppt 이미지 전환 모듈 설치
import aspose.slides as slides
import aspose.pydrawing as drawing

# setting 변수 접근
password_const = getattr(settings, 'PASSWORD', None)
ip_addr = getattr(settings, 'IP_ADDRESS', None)

# ppt 목록 페이지
def pptIndexPage(request):
    ppts = models.SeminarPPT.objects.all()[::-1]
    return render(request,"ppt-index.html", {'pptList':ppts, 'ipaddr':ip_addr})


# ppt 업로드 페이지
def pptUploadPage(request):    
    try:
        if request.method == 'POST':
            pptFile = request.FILES['pptFile']
            pptUploader = request.POST['who']
            password = request.POST['password']
            if password == password_const:
                # 모델 저장
                pptFileModel = models.SeminarPPT(people = pptUploader, pptFile = pptFile, pptFileName=pptFile)
                pptFileModel.save()
                print('저장 완료')
                
                # 이미지 전환
                try:
                    pres = slides.Presentation(os.path.join(os.path.abspath("media/ppts/"), str(pptFileModel.pptFile)))
                    desiredX = 1200
                    desiredY = 800
                    scaleX = (float)(1.3 / pres.slide_size.size.width) * desiredX
                    scaleY = (float)(1.3 / pres.slide_size.size.height) * desiredY
                    os.mkdir(str(os.path.abspath('ppt/static/img/ppts/')) + '\\' + str(pptFileModel.id))
                    for index in range(pres.slides.length):
                        slide = pres.slides[index]
                        slide.get_thumbnail(scaleX, scaleY).save((str(os.path.abspath('ppt/static/img/ppts/')) + '\\' + str(pptFileModel.id) + '\\'+str(index+1)+'.png').format(i=index), drawing.imaging.ImageFormat.png)
                except:
                    print("이미지 전환 실패")
                    
                return redirect('http://'+ip_addr+'ppt')
    except:
        print("저장 실패")
        
    return render(request,"ppt-upload.html", {'ipaddr':ip_addr})

# ppt 상세 페이지
def pptViewPage(request, pptid):
    pptFile = models.SeminarPPT.objects.get(id=pptid)
    pres = slides.Presentation(os.path.join(os.path.abspath("media/ppts/"), str(pptFile.pptFile)))
    return render(request,"ppt-view.html", {'pptFile':pptFile, 'pptLength':pres.slides.length, 'ipaddr':ip_addr})

# 파일 다운로드
def pptDownload(request, pptid):
    pptFile = models.SeminarPPT.objects.get(id=pptid)
    file_path = os.path.join(os.path.abspath("media/ppts/"), str(pptFile.pptFile))
    return FileResponse(open(file_path, 'rb'))

# 파일 삭제
def pptDelete(request, pptid):
    ppt = models.SeminarPPT.objects.get(pk=pptid)
    try:
        if request.method == 'POST' and request.POST['password']==password_const:
            os.remove(os.path.join(os.path.abspath("media/ppts/"), str(ppt.pptFile)))
            print(os.path.abspath('ppt/static/img/ppts/'+str(ppt.id)+'/'))
            shutil.rmtree(os.path.abspath('ppt/static/img/ppts/'+str(ppt.id)+'/'))
            ppt.delete()
            print('제거 성공')
            return redirect('http://'+ip_addr+'ppt')
    except:
        pass
    print("제거 실패")
    
    return redirect('http://'+ip_addr+'ppt/'+str(pptid))