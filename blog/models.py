from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )

    title = models.CharField(max_length=200)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3, default='drf')

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='authored_posts')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id])


class Comment(models.Model):
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(),on_delete = models.CASCADE)
    is_activate = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True)

    # در این اسم پستی  که براش کاکمنت گذاشته شده نوشته می شود
    # پس این سطر کامنت های جدول Bookاست

    post = models.ForeignKey(Post,on_delete = models.CASCADE,related_name='comments')

    def __str__(self):
        return self.text






