from django.contrib import admin
from .models import CustomUser
from django.utils.html import format_html
# Register your models here.

class CustomUserModelAdminClass(admin.ModelAdmin):
    list_display = ("Full_Name", "email", "User_Photo")
    list_display_links = ("Full_Name",)

    def Full_Name(self, obj):
        return obj.first_name +" " + obj.last_name

    def User_Photo(self, obj):
        return format_html(f"<img src=http://127.0.0.1:8000/{obj.photo} widht='50' height='50'/>")

admin.site.register(CustomUser, CustomUserModelAdminClass)
