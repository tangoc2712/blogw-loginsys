from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings

# Create your models here.
class SignVideoUpload(models.Model):
    word = models.CharField(null=True, blank=True, max_length=255)
    video = models.CharField(null=True, blank=True, max_length=255)
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contributor")

    class Meta:
        db_table = 'helpus'