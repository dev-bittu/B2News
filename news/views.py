from django.shortcuts import render, get_object_or_404
from .models import News


# Create your views here.
def category(request, slug):
    return render(request, "news/category.html")


def news(request, slug):
    news_obj = get_object_or_404(News, slug=slug, is_active=True)
    ctx = {"news": news_obj}

    if request.GET.get('style', '') == 'fullwidth':
        return render(request, "news/news_fullwidth.html", ctx)
    
    return render(request, 'news/news.html', ctx)
