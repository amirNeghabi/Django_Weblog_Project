from django.contrib import admin
from django.urls import path
from django.shortcuts import get_object_or_404, redirect
from django.utils.html import format_html
from django.contrib.admin.views.decorators import staff_member_required
from .models import Post, Comment


# ✅ ویوی تغییر وضعیت پست (منتشر / پیش‌نویس)
@staff_member_required
def toggle_post_status(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.status = 'drf' if post.status == 'pub' else 'pub'
    post.save()
    return redirect(request.META.get('HTTP_REFERER', '/admin/'))


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'author', 'toggle_status_button']
    list_filter = ['status']
    actions = ['make_published', 'make_draft']
    readonly_fields = ['toggle_status_button']

    # ✅ آدرس URL سفارشی برای ویو تغییر وضعیت
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('toggle_status/<int:pk>/', self.admin_site.admin_view(toggle_post_status), name='toggle_post_status'),
        ]
        return custom_urls + urls

    # ✅ دکمه وضعیت سریع برای هر پست
    def toggle_status_button(self, obj):
        if obj.status == 'pub':
            color = 'red'
            label = '⛔ غیرفعال کن'
        else:
            color = 'green'
            label = '✅ فعال کن'
        url = f'toggle_status/{obj.pk}/'
        return format_html(f"<a href='{url}' style='color:{color};'>{label}</a>")

    toggle_status_button.short_description = 'وضعیت سریع'

    # ✅ اکشن برای انتشار پست‌ها
    def make_published(self, request, queryset):
        updated = queryset.update(status='pub')
        self.message_user(request, f"{updated} پست منتشر شد.")

    make_published.short_description = "📢 انتشار پست‌های انتخاب‌شده"

    # ✅ اکشن برای پیش‌نویس کردن
    def make_draft(self, request, queryset):
        updated = queryset.update(status='drf')
        self.message_user(request, f"{updated} پست به پیش‌نویس برگشت داده شد.")

    make_draft.short_description = "📝 غیرفعال‌سازی پست‌های انتخاب‌شده"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'post',
        'text',
        'datetime_created',
        'recommend',
        'is_activate',
        'toggle_activation_button',  # 👈 دکمه تغییر وضعیت
    )
    list_filter = ['is_activate', 'recommend', 'datetime_created']
    readonly_fields = ['toggle_activation_button']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('toggle_comment/<int:pk>/', self.admin_site.admin_view(self.toggle_comment_status),
                 name='toggle_comment_status'),
        ]
        return custom_urls + urls

    def toggle_activation_button(self, obj):
        if obj.is_activate:
            color = 'red'
            label = '⛔ غیرفعال کن'
        else:
            color = 'green'
            label = '✅ فعال کن'
        url = f'toggle_comment/{obj.pk}/'

        return format_html(f"<a href='{url}' style='color:{color};'>{label}</a>")

    toggle_activation_button.short_description = 'وضعیت سریع'

    def toggle_comment_status(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.is_activate = not comment.is_activate
        comment.save()
        return redirect(request.META.get('HTTP_REFERER', '/admin/'))
