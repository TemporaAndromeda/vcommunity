from django.forms import ModelForm, widgets
from .models import *
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "post_image", "tags", "source_link"]
        widgets ={
            'tags': forms.CheckboxSelectMultiple(),

        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__( *args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder' : 'Add Title'})
        # self.fields['description'].widget.attrs.update({'class':'input', 'placeholder' : 'Add Description'})


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["vote_value", 'description']
        labels = {
            "vote_value": "Place your Vote",
            "description": "Add a comment with your vote"
            }
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__( *args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
