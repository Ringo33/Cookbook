from django import forms
from django.forms.widgets import Textarea
from .models import Post, Comment


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'text', 'image']

        widgets = {
            'text': Textarea(attrs={'class': 'form-control form-control-sm'})
        }

    def clean_text(self):
        data = self.cleaned_data['text']
        if data.lower().find('невкусный') != -1:
            raise forms.ValidationError('В тексте запрещено упоминать "невкусный"!')
        return data


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': Textarea(attrs={'class': 'form-control form-control-sm'})
        }
