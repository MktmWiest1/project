from django import forms
from . import models


class ShowsForm(forms.ModelForm):
    class Meta:
        model = models.TWShows
        fields = '__all__'
