from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category
from django.db.models import Q
from django.contrib import messages

# Get the User model
User = get_user_model()


def index(request):
    return render(request, "index.html")


def search(request):
    # Get the search keyword from the query parameters
    keyword = request.GET.get("keyword", "").strip()

    # Check if keyword is provided
    if not keyword:
        messages.info(request, "Please enter a keyword to search.")
        return redirect("index")  # Early return if no keyword

    # Search query logic using Q objects for case-insensitive search in multiple fields
    news_results = News.objects.filter(
        Q(title__icontains=keyword)
        | Q(desc__icontains=keyword)
        | Q(content__icontains=keyword),
        is_active=True  # Only return active news articles
    )

    category_results = Category.objects.filter(
        Q(title__icontains=keyword) | Q(desc__icontains=keyword)
    )

    # Context to pass the results to the template
    ctx = {
        "news": news_results,
        "categories": category_results,
        "keyword": keyword,  # Pass keyword to display in the template if needed
    }
    

    # Render the search results in the 'search.html' template
    return render(request, "search.html", ctx)


def index2(request):
    return render(request, "index.html")


def error404(request):
    return render(request, "404.html")


def author(request, username: str):
    # Use get_object_or_404 for better error handling and simplicity
    author = get_object_or_404(User, username=username, is_author=True)

    ctx = {"author": author}
    return render(request, "author.html", ctx)
