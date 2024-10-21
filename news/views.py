from django.shortcuts import render


# Create your views here.
def category(request, slug):
    return render(request, "news/category.html")
