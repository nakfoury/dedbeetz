from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django import forms
from django.contrib import messages
from . import forms


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = forms.VoicedBeatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Add a message as user feedback to the page
            messages.add_message(request, messages.SUCCESS, "Your beat was uploaded successfully.")
            # Redirection prevents the user from accidentally resubmitting the form
            return HttpResponseRedirect(reverse('sickbeetz'))
        # Intentionally fall-through if the form is not valid.
        # The validation errors will be displayed in the rendered page.
    else:
        form = forms.VoicedBeatForm()
    return render(request, 'sickbeetz/index.html', {'form': form})
