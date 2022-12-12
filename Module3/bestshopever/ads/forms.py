from django import forms

from bestclassified.models import Stars


class AdCreateForm(forms.Form):
    rate = forms.ChoiceField(widget=forms.Select, choices=Stars.choices)