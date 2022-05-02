from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def task_list(request):
    return HttpResponse("<h1>To do list app<h1>")
