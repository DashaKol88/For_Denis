from django import forms
from .models import Author, Comment


class AuthorRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Author
        fields = ['name', 'email', 'homepage', 'password']


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    parent_comment_id = forms.IntegerField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Comment
        fields = ['content', 'parent_comment_id']
