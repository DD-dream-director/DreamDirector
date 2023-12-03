from django import forms
from account_app.models import Profile


class SelectedTagForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['tags']
