from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    task = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': 'title'})


def about(request):
    task = Task.objects.all()
    return render(request, 'main/about.html', {'title': 'Описание', 'tasks': 'task'})


def adds(request):
    task = Task.objects.all()
    return render(request, 'main/adds.html', {'title': 'Дополнительно', 'tasks': 'adds'})
