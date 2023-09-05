# oopsla-people-page
[OOPSLA] 연구실 부원 개인 페이지(이 모든 영광을 교수님께 바칩니다..)

웁슬라 연구실 부원 홈페이지 입니다.<br>
ppt페이지, 부원 소개 페이지를 제작했습니다.

## Components
- Python
- Django

## App
해당 프로젝트에는 다음과 같은 App이 존재합니다.
- main: 부원 소개 페이지
- ppt: 세미나 ppt 페이지

## 서버 실행 방법
1. 파이썬 설치
2. Django 설치(pip install django)
3. 그 외 패키지 설치... (서버 실행하다 에러나면 에러메시지 보고 설치해주세요)
4. cmd에서 프로젝트 폴더 안의 manage.py 파일이 있는 경로로 이동
5. cmd에 다음 명령어 입력: python manage.py runserver 0.0.0.0:8000

## 부원 추가 방법
1. main/peoples/ 경로에 부원 이름으로 디렉토리를 새로 생성합니다.
2. 생성한 디렉토리 안에 profile.txt파일을 생성합니다.
3. 텍스트 파일에 정보를 기록합니다. 양식은 기존 파일을 참고해서 작성하시면 됩니다.

## 기타 설정 방법
- 비밀번호 설정: oopslaPeoplePage/settings.py 가장 하단의 PASSWORD 변수의 값을 변경
- 서버 ip주소 변경: oopslaPeoplePage/settings.py 가장 하단의 IP_ADRESS 변수의 값을 변경
