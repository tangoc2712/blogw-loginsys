from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings

# Create your models here.
class SignVideoUpload(models.Model):
    word = models.CharField(null=False, blank=False, max_length=255)
    video = models.FileField(upload_to='uploads/%Y/%m/%d/',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contributor")

    class Meta:
        db_table = 'helpus'