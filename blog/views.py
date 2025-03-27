from django.shortcuts import render,redirect
from .models import Post
# مربوط ب راه اول مدیریت خطا
from django.core.exceptions import ObjectDoesNotExist
# راه دوم مدیریت خطا
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# استفاده ااز متد فرم در دریافت اطلاعات از کاربر
from .forms import NewPostForm
# استفاده از کلاس بیس ویو
from django.views import generic
# بعد از حذف پست کاربر را به صفحه دیگیری ریدایرکت کن
from django.urls import reverse_lazy


# Create your views here.
# ساخت ویویی برای نمایش تمام پست های موجود در دیتا بیس
# def post_list_view(request):
#     # گرفتن تمام داده ها(پست های موجود ) در دیتا بیس
#     # posts_list = Post.objects.all()
#     # -------------------------
#
#     # نمایش پست هایی با وضعیت منتشر شده در صفحه post_list
#     posts_list = Post.objects.filter(status = 'pub').order_by("-datetime_modified")
#
#     # کاربر رو به صفجه html ایی زیر ببر و داده هایی که از ذیتا بیس استخراج کردی رو هم همراه درخواستت برگردون
#     return render(request,'blog/posts_list.html',{'posts_list':posts_list})

# def post_detail_view(request,pk):
#
#     # راه اول مدیریت خطا
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except ObjectDoesNotExist:
#     #     post = None
#     #     print('Post does not exist')
#     # ----------------------------
#     # راه دوم مدیریت خطا
#     post = get_object_or_404(Post,pk=pk)
#
#     return render(request,'blog/post_detail.html',{'post':post})

# def post_create(request):
#     # معیین کرد نوع درخواست کاربر
#     # print(request.method)
#     # print("Thia is a creat view")
#     # ------------
#
#     # دریافت اطلاعات فرم از  کاربر
#     # print(request.POST)
#     # print("-"*20)
#     # --------
#     # تفکیک post,get:
#     # if request.method == 'POST':
#     #     print("post request.")
#     # else:
#     #     print("Get request.")
#     #     -------------
#     # برو به درخواستی ک کاربر داده و مقدار کلیدی ک برابر title است رو بهم بده
#     # print(request.POST.get('title'))
#     # -------------
#     # استفاده از تفکیک نوع درخواست کاربر get,Post
#     # if request.method =="POST":
#
#             # print(request.POST.get('title'))
#             # print(request.POST.get('text'))
#         # ----------------ذخیره اطلاعات فرم در ویو------------
#         #     گرفتن  فیلد های فرم و قرار دادن ان در یک متغییر
# #         post_title = request.POST.get("title")
# #         post_text = request.POST.get("text")
# #         user = User.objects.all()[0]
# #         #     اضافه کردن ریکورد جدید به کلاس Post
# #         Post.objects.create(title=post_title,text=post_text,status='pub',author=user)
# #
# #     else:
# #             print("Get request")
# #
# #     return render(request,'blog/post_create.html')
# # from django.contrib.auth.models import User
# # # -----------------------------------------------------استفاده از فرم ها در جنگو------------------------------------------------------------
#     if request.method == "POST":
#         # ساخنت یک شی از فرم
#         form = NewPostForm(request.POST)
#         # اگر اطلاعات کاربر درست بود آن را سیو کن
#         if form.is_valid():
#             form.save()
#     #         پس از ذخیره اطلاعات کاربر در دیتا بیس یک فرم جدید و خالی بهش نمایش داده بشه
#     #         form = NewPostForm()
#     # ---------------
#     # پس از ذخیره اطلاعات کاربر ان را به صفحه اصلی سایت ببر
#             return redirect("post_list")
#     else:
#         # ساخت شی از کلاس ساخته شده در فایل forms
#         form = NewPostForm()
#     return render(request,'blog/post_create.html',context={'form':form})


# def post_update(request,pk):
# #     یافتن پست ای که ای دی ا رو کاربر داده
#     post = get_object_or_404(Post,pk=pk)
#     # ساخت فرمی با اطلاعات پستی که کاربر رای دی ان را داده است
#     # یا فرمی با اطلاعات آپدیت شده کاربر در بار دوم اجرای این تابع ،وقتی کاربر submit میکند
#     form = NewPostForm(request.POST or None,instance=post)
#     # بررسی صحت اطلاعات وروردی کاربر و ذخیره ان در دیتا بیس
#     if form.is_valid():
#         form.save()
#         return redirect("post_list")
#     return render(request,'blog/post_create.html',context={'form':form})


# def post_delete(request,pk):
#     post = get_object_or_404(Post,pk=pk)
#     if request.method =="POST":
#         post.delete()
#         return redirect("post_list")
#     return render(request,'blog/post_delete.html',context={'post':post})

# -------------------class_base_view------------------------------------------------------------------------------------
# ساخت کلاس برای list_view
class PostListView(generic.ListView):
    # معیین کردن مدلی که باید آن را لیست کند(همه اشیای ان در دیتا بیس را برمی دارد)
    model = Post

    # معیین کردن نوع تمپلیتی ک باید به کاربر نمایش داده شود
    template_name = "blog/posts_list.html"
    context_object_name = "posts_list"
    # استفاده از متد ها برای گذاشتن شرط برای برداشتن شی های موجود از مدل در دیتابیس
    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')

    # ساخت کلاس برای صفحه جزییات هر پست
class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

# ساخت کلاس برای صفحه ساخت پست
class PostCreateView(generic.CreateView):
    # ازکدام فرم در این کلاس استفاده کردی؟
    form_class = NewPostForm
    template_name = "blog/post_create.html"

# ساخت فرم برای اپدیت پست ها
class PostUpdateView(generic.UpdateView):
    # نوع مئل را باید معیین کنیم تا جنگو بهش کوِییری بزند
    model = Post
    form_class = NewPostForm
    template_name = "blog/post_create.html"

# ساخت کلای برای حذف پست
class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
#     بعد از ساخت کلاس و با کمی تاخیر برو و آدرس صفحه نمایش پست را پیدا کن
# و کاربر را بعد از حذف پست به اون صفحه ریدایرکت کن
    success_url = reverse_lazy("post_list")

