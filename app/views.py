from django.shortcuts import render
from app.models import *

# Create your views here.
from django.http import HttpResponse





def insert_topic(request):
    tn=input('enter topic name')
    T=Topic.objects.get_or_create(Topic_name=tn)[0]
    T.save()
    return HttpResponse('topic is instered successfully')

def insert_webpage(request):
    tn=input('enter topic_name')
    name=input('enter name')
    url=input('enter url')
    T=Topic.objects.get_or_create(Topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(Topic_name=T,name=name,url=url)[0]
    W.save()
    return HttpResponse('webpage data is inserted')

def insert_accessrecords(request):
    tn=input('enter topic_name')
    name=input('enter name')
    url=input('enter url')
    date=input('enter date')
    T=Topic.objects.get_or_create(Topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(Topic_name=T,name=name,url=url)[0]
    W.save()
    A=Access_Records.objects.get_or_create(Topic_name,name=name,date=date)[0]
    A.save()
    return HttpResponse('access is inserted')
