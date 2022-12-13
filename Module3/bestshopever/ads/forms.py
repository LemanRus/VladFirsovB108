from django import forms

from ads.models import Advertisement


class AdCreateForm(forms.ModelForm):

    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'image', 'category']
        labels = {
            'title': 'Title',
            'description': 'Description of advertisement',
            'image': 'Product photo',
            'category': 'Choose category',
        }
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Describe your product in detail'
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }
