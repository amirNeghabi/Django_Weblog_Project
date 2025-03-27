from django.test import TestCase
from django.contrib.auth.models import User
# با متد reverse میتوان به اسم یه url رفت
from django.shortcuts import reverse
from .models import Post


# Create your tests here.

# ساخت کلاس برای تست مدل Post
class BlogPostTest(TestCase):
    # ساخت یک پست با توجه به عن.ان هایی که در جدول مدلPost داریم
    @classmethod
    def setUpTestData(cls):
        # ساخت یک یوزر برای استفاده در فیلد نویسنده پست
        cls.user = User.objects.create(username="user1")
        # دستور ساخت پست1 با وضعیت published
        cls.post1 = Post.objects.create(
            title='post1',
            text='This is a test post',
            status=Post.STATUS_CHOICES[0][0],
            author=cls.user,
        )
        # ساخت پست2 با وضعیت draft
        cls.post2 = Post.objects.create(
            title='post2',
            text='This is a test post2',
            status=Post.STATUS_CHOICES[1][0],
            author=cls.user,
        )

    #     تست برای بررسی درستی اینکه آیا در هنگام نمایش هر پست عنوان آن به صورت str نمایش داده
    # مشود یا نه؟(مربوط به فایل modelو تابع __str__)

    def test_post_model_str(self):
        # ساخت شیی از پست ساخته شده در دیتا بیس تستی برای
        post = self.post1
        # بررسی کن ایا با اجرای تابع strروی این شی postحاصل برابر با عنوان این شیی پست است یا نه
        # زیرا تابع str یماد و عنوان هر پست را بر میگرداند
        self.assertEqual(str(post), post.title)

    #     تستی برای اینکه مطمن شویم عنوان و متن پیام ذخیره شده در دیتابیس همونی استک به کاربر نشان
    # داده می شود
    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'post1')
        self.assertEqual(self.post1.text, 'This is a test post')
        self.assertEqual(self.post1.status, Post.STATUS_CHOICES[0][0])

    #     تستی برای اطمینان از دسترسی کاربر از طریق آدرس صفحه به صفحهblog
    def test_post_list_url(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    #     تست درسنی کارکرد سایت و دسترسی کاربر به صفحه blog از طریق اسم آن
    def test_post_list_url_by_name(self):
        # رفتن به اسم url:post_list
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)

    #         تستس برای درستی نمایش تیتر پست در صفحه post_list
    def test_post_title_on_blog_list_page(self):
        # برو ب صفحه پست لیست و ان را در response قرار بده
        response = self.client.get(reverse("post_list"))
        self.assertContains(response, self.post1.title)

    def test_post_details_on_blog_detail_page(self):
        # برو به صفحه detail اون url ای که کاربر خواسته
        response = self.client.get(reverse("post_detail", args=[self.post1.id]))

        # ایا تیتر و متن پست در  صفحه جزییات نمایش داده می شود یا ن؟
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    # تستی برای درسترسی کاربر به صفحه جزییات با آدرس صفحه detail
    def test_post_detail_url(self):
        response = self.client.get(f"/blog/{self.post1.id}/")
        self.assertEqual(response.status_code, 200)

    # ساخت تست برای دسترسی کاربر به صفحه جزییات با استفاده از اسم url
    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse("post_detail", args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    #         تستی برای زمانی که کاربر ای دی پستی را وارد میکند که وجود ندارد و باید خطای 404 دریافت کند
    def test_status_code_404_if_page_dos_not_exist(self):
        response = self.client.get(reverse("post_detail", args=[999]))
        self.assertEqual(response.status_code, 404)

    # تستی برای اطمینان از درستی اینکه فقط پست ها با وضعیت published به کاربر نمایش داده شود
    def test_draft_post_not_show_in_post_list(self):
        response = self.client.get(reverse("post_list"))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.text)

    #      تستی برای اطمینان از درستی کارکرد تابع post_crete_view برای اینکه ببینیم
    # اگر کاربر درخواستی از نوع POST بدهد این تابع میاد و یک پست در دیتا بیس تستی بسازد یا ن؟
    def test_post_create_view(self):
        # برو بهurlای به اسم post_list و یک پست بساز
        response = self.client.post(reverse('post_create'), {
            'title': 'some title',
            'text': 'some text',
            'status': Post.STATUS_CHOICES[0][0],
            'author': self.user.id,
        })

        # آیا پست به درستی در دیتابیس ساخته شده؟
        self.assertEqual(response.status_code, 302)

        # آیا مقادیر مد نظر ما برای فیلد های مختلف پست تستی در دیتا بیس قرار گرفته؟

        self.assertEqual(Post.objects.last().title, 'some title')
        self.assertEqual(Post.objects.last().text, 'some text')
        self.assertEqual(Post.objects.last().status, Post.STATUS_CHOICES[0][0])
        self.assertEqual(Post.objects.last().author, self.user)

# ساخت تست برای درستی کارکرد تابع update_view
    def test_post_update_view(self):
        response = self.client.post(reverse("post_update",args=[self.post2.id]), {
            "title": "updated title",
            "text": "updated text",
            "status": Post.STATUS_CHOICES[0][0],
            # همون ای دی که برای سازنده پست 2 در نظر گرفتی رو بنویس بدون تغییر
            "author": self.post2.author.id,
        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(Post.objects.last().title, 'updated title')
        self.assertEqual(Post.objects.last().text, 'updated text')

        # ساخت تست برای درستی کارکرد تابع delete_view
    def test_post_delete_view(self):
        response = self.client.post(reverse("post_delete",args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)
