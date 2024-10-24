from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Category, News


# Register your models here.
@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ("id", "title", "published_at", "is_active")


@admin.register(News)
class NewsAdmin(ImportExportModelAdmin):
    list_display = ("id", "title", "published_at", "is_active")
