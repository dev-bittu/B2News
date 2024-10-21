from django.urls import path
from .views import *

app_name = "news"

urlpatterns = [
    path('category/<slug:slug>/', category, name="category"),
]
