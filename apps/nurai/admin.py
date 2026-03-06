from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'city', 'email', 'created_at')
    search_fields = ('name', 'city', 'email')