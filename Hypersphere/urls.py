"""Hypersphere URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import redirect
from account.views import IndexView
from blog.views import BlogView
from settings.views import DashboardView

urlpatterns = [
    url(r'',include('account.urls.default'), name='index'),
    url(r'^signup/',IndexView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^settings/?$', lambda x: redirect('dashboard')),
    url(r'^settings/', include('settings.urls.default')),
    url(r'^(?P<username>\w+)/',include('blog.urls.default')),
]
