from django.shortcuts import render


def index(request):
    return render(request, 'js_stuff/index.html')


def blur(request):
    return render(request, 'js_stuff/blur.html')


def battleships(request):
    return render(request, 'js_stuff/battleships.html')
