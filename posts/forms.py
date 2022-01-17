from django import forms
from .models import CommentModel


class CommentFormModel(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ['created_at', 'post']
