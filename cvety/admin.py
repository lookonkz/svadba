from django.contrib import admin
from .models import Cvety


# Register your models here.
@admin.register(Cvety)
class AdminCvety(admin.ModelAdmin):
    list_display = ["name", "id", "price"]

