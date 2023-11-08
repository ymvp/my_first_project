from django.shortcuts import render
from django.http import HttpResponse

def vish(request):
    return HttpResponse('<h1><marquee>HI VISH</marquee></h1>')


def verma(request):
    return HttpResponse('<h1><marquee>worth verma worthu<h1><marquee>')
