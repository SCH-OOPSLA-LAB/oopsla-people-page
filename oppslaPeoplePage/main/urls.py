import os
from django.urls import path

from . import views

# 사용자 목록 폴더의 정보를 받아옴, 개개인의 리스트 생성
currentPos = os.path.dirname(__file__)
peopleList = os.listdir(currentPos+'\\peoples')
# pathList = [path(name, views.test, name=name) for name in peopleList]

urlpatterns = [
               path('<str:name>/', views.peoplePage),
               path('<str:name>/ppts/', views.pptIndexPage),
               path('<str:name>/ppts/upload/', views.pptUploadPage),
               
               ]