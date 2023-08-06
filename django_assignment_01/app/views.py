from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def platter(request):
    # return HttpResponse('thist is platter page')
    return render(request, './app/index.html')