from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator


# Create your models here.

class VoicedBeat(models.Model):
    file = models.FileField(upload_to='voiced-beats', validators=[FileExtensionValidator(allowed_extensions=['wav'])])
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        """
        Update timestamps on save.
        ref: https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
        """
        now = timezone.now()
        if not self.id:
            self.created_at = now
        self.updated_at = now
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.file.name
