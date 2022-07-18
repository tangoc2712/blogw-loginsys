from django.db import models
from django.forms import IntegerField

# Create your models here.

class Level(models.Model):
    level = models.IntegerField(null = False, blank = False, verbose_name="Level")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return "".join(str(self.level))
    
class Word(models.Model):
    word = models.CharField(null = False, blank = False, verbose_name="Word", max_length=255)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Description", null=True, blank=True)

    def __str__(self) -> str:
        return self.word