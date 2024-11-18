from django import forms
from .models import Character, Equipement


class MoveForm(forms.ModelForm):
    lieu = forms.ModelChoiceField(queryset=Equipement.objects.all(), label="Nouveau lieu")

    class Meta:
        model = Character
        fields =['lieu']
