from django import forms
from .models import SelectedItem # 紐づけを行うモデル

class SelectedItemForm(forms.ModelForm):
    class Meta:
        model = SelectedItem
        fields = ['selected_item']
