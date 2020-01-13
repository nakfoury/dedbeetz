from django import forms
from . import models


class VoicedBeatForm(forms.ModelForm):
    class Meta:
        model = models.VoicedBeat
        fields = ['file']
