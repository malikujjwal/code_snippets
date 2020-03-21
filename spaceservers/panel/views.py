from django.shortcuts import render


def home(request):
    return render(request, 'panel/index.html')


def mods(request):
    return render(request, 'panel/mods.html')
