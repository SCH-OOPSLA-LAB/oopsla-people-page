from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    name = (str(request).split("'")[1].split('/')[2])
    print(name)

    return render(request, "people-page.html", {'name':name})