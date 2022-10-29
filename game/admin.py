from atexit import register
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'level', 'description')


admin.site.register(Level)
# admin.site.register(WordAdmin, Word)