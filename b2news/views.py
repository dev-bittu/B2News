from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def index2(request):
    return render(request, "index.html")


def error404(request):
    return render(request, "404.html")
