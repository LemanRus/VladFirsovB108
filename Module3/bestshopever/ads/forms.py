from django import forms

from .models import Advertisement, Comment


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


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(CommentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Write your comment here"})
        }

    def clean(self):
        cleaned_data = super().clean()
        if not self.request.user.is_authenticated:
            raise forms.ValidationError('Please log in to leave the comment')