from django import forms
from .models import User_select

class SelectedTagForm(forms.ModelForm):
    class Meta:
        model = User_select
        fields = ['name']
