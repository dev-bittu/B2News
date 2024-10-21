from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ("id", "email", "is_staff", "is_active")
