"""
URL configuration for myboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls), # Django 기본 admin 페이지

    path('users/', include('users.urls')) # 'users' 앱의 URL 패턴 포함 # users.urls 모듈을 불러와서 해당 앱의 URL 패턴을 /users/ 경로 아래에 포함시킨다
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
