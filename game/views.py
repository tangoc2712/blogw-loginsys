from django.shortcuts import render
from .models import *
# Create your views here.

def levels(request):
    levels = Level.objects.all()
    contexts = {
        "levels": levels,
    }
    return render(request, "game/levels.html", contexts)

def level_detail(request, level_id):
    level = Level.objects.filter(level=level_id).first()
    words = Word.objects.filter(level=level)
    contexts = {
        "words": words,
    }
    return render(request, "game/level_detail.html", contexts)

def level_detail2(request):
    contexts = {
    }
    return render(request, "game/level_detail2.html", contexts)