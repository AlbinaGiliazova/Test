'''Views for article app: AboutView, ArticlesView, DefaultView'''

from django.shortcuts import render, redirect
from django.views import View
from article.models import Article
from datetime import datetime


default_context = {'year': datetime.now().year,}

class AboutView(View):
    '''Controller for the about page'''

    def get(self, request, *args, **kwargs):
        '''GET request'''

        return render(request,
            'article/about.html', context = default_context)


class ArticlesView(View):
    '''Controller for the list of articles'''

    def get(self, request, *args, **kwargs):
        '''GET request'''

        context = default_context
        context['posts'] = Article.objects.all()
        return render(request,
            'article/index.html', context=context)

class DefaultView(View):
    '''Controller for /'''

    def get(self, request, *args, **kwargs):
        '''GET request'''

        return redirect("/about/")