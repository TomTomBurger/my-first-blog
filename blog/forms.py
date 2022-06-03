from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Post, Comment, Account

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class AccountForm(ModelForm):

    class Meta:
        model = Account
        fields = ('cd', 'name',)