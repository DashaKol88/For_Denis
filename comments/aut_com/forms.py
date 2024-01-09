from django import forms
from .models import Author


class AuthorRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Author
        fields = ['name', 'email', 'homepage', 'password']


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
    parent_comment_id = forms.IntegerField(required=False, widget=forms.HiddenInput)
