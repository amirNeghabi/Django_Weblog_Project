"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    # اگر کاربر در  یو ار ال، بلاک رو زد اون رو ببر به ادرس یو ار ال زیر
    path("blog/", include('blog.urls')),
    path("",include('blog.urls')),
    path("accounts/",include('django.contrib.auth.urls')),
#     ساخت یو ار ال برای رفتن کاربر به صفحه sing up
    path('accounts/',include('accounts.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]
