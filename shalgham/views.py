import datetime

from django.http import HttpResponse
from django.shortcuts import render
from shalgham.models import VisitTime


def ping(request):
    time = str(datetime.datetime.now())
    VisitTime.objects.create(time=time)
    return HttpResponse(time)


def visit_list(request):
    visits = VisitTime.objects.all()
    response = ""
    for visit in visits:
        response += visit.time + "|"
    return HttpResponse(response)
