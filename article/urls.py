# -*- coding: utf-8 -*-
'''URL configuration for article app'''

from django.urls import path, re_path
from article.views import AboutView, ArticlesView, ClearDBView, DefaultView, \
                        ParseView, PostView

urlpatterns = [
    re_path('about/?', AboutView.as_view(), name='about'),
    re_path('clear_db/?', ClearDBView.as_view(), name='clear_db'),
    re_path('index.html', DefaultView.as_view()),
    re_path('parse/?', ParseView.as_view(), name='parse'),
    re_path('posts/(?P<page>[^/]*)/?', ArticlesView.as_view(), name='home'),
    path('', DefaultView.as_view()),
    re_path("(?P<post_id>[^/]*)/?", PostView.as_view(), name='post'),
]