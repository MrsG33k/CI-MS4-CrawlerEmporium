from django import forms
from .models import BlogComment


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['message']
        labels = {
            'message': 'Comment Input'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['message'].widget.attrs.update({
            'class': 'form-control bg-dark text-white border-secondary',
            'placeholder': 'Enter commentary...',
            'rows': 3
        })
