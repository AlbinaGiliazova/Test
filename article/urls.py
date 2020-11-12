# -*- coding: utf-8 -*-
'''URL configuration for article app'''

from django.urls import path, re_path
from article.views import AboutView, ArticlesView, DefaultView

urlpatterns = [
    re_path('about/?', AboutView.as_view(), name='about'),
    re_path('posts/', ArticlesView.as_view(), name='home'),
    re_path('index.html', DefaultView.as_view()),
    path('', DefaultView.as_view()),

]
