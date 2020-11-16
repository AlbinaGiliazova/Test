# -*- coding: utf-8 -*-
'''URL configuration for article app'''

from django.urls import path, re_path
from article.views import AboutView, ArticlesView, ClearDBView, DefaultView, \
                        ParseView, PostView, RestPageView, \
                        RestPostView, RestAboutView

# app_name will help us do a reverse look-up latter.
# https://webdevblog.ru/sozdanie-django-api-ispolzuya-django-rest-framework-apiview/
# app_name = "article"

urlpatterns = [
    re_path('about/?', AboutView.as_view(), name='about'),
    re_path('clear_db/?', ClearDBView.as_view(), name='clear_db'),
    re_path('index.html', DefaultView.as_view()),
    re_path('parse/?', ParseView.as_view(), name='parse'),
    re_path('rest/page/(?P<page>[^/]*)/?', RestPageView.as_view()),
    re_path('rest/howto/?', RestAboutView.as_view(), name='rest'),
    re_path('rest/(?P<post_id>[^/]*)/?', RestPostView.as_view()),
    re_path('posts/(?P<page>[^/]*)/?', ArticlesView.as_view(), name='home'),
    path('', DefaultView.as_view()),
    re_path("(?P<post_id>[^/]*)/?", PostView.as_view(), name='post'),
]