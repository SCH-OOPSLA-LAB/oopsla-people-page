import os
from django.urls import path
from . import views

# 사용자 목록 폴더의 정보를 받아옴, 개개인의 리스트 생성
currentPos = os.path.dirname(__file__)

urlpatterns = [
               path('', views.pptIndexPage),
               path('upload/', views.pptUploadPage),
               path('<int:pptid>/', views.pptViewPage),
               path('<int:pptid>/download/', views.pptDownload),
               path('<int:pptid>/delete/', views.pptDelete),
               ]