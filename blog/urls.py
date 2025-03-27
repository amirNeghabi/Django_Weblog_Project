from django.urls import path
from . import views

urlpatterns = [
    # در صفحه اول به کاربر فایل ویو زیر رو نشون بده
    # path('',views.post_list_view,name='post_list'),
    # path('<int:pk>/',views.post_detail_view,name='post_detail'),
    # path('create/',views.post_create,name='post_create'),
    # path('<int:pk>/update/',views.post_update,name = 'post_update'),
    # path('<int:pk>/delete/',views.post_delete,name='post_delete'),
#     -----------------------class_base_view---------
    # در صفحه اول به کاربر فایل ویو زیر رو نشون بده
    path('',views.PostListView.as_view(),name='post_list'),
    # در صفحه دیتیل ، جزییات هر پست را نشان بده
    path('<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
#     با ادرس creat کاربر را به صفحه ساخت پست ببر
    path("create/",views.PostCreateView.as_view(),name='post_create'),
#     کاربر را صفحه آپدیت فرم ببر
    path("<int:pk>/update/",views.PostUpdateView.as_view(),name='post_update'),
    path("<int:pk>/delete/",views.PostDeleteView.as_view(),name='post_delete'),
]