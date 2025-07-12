from django import forms
from .models import Post, Comment

# فرم ساخت پست
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','text','author','status']

# فرم ارسال نظز برای کاربر
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text','recommend']
