from .models import Devtool
from django import forms

class DevtoolForm(forms.ModelForm):
    class Meta():
        model = Devtool
        fields = ('__all__')