from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES =(
        ('pub','Published'),
        ('drf','Draft'),
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    # ذخیره زمانی که پستی در دیتا بیس ویرایش می شود
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices= STATUS_CHOICES,max_length=3 )
#     اسم نویسنده پست
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)

    # برای نمایش عنوان هر پست در پنل ادمین از این دستور استفاده میکنیم
    def __str__(self):
        return self.title

#     معیین کردن آدرس هر شی ساخته شده از این url
    def get_absolute_url(self):
        return reverse("post_detail",args =[self.id])

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






