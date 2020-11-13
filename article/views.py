'''Views for article app: AboutView, ArticlesView, DefaultView, PostView'''

from django.shortcuts import render, redirect
from django.views import View
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.core.paginator import Paginator
from article.parsing import parse


default_context = {'year': datetime.now().year,}

class AboutView(View):
    '''Controller for the about page'''

    def get(self, request, *args, **kwargs):
        '''GET request'''

        return render(request,
            'article/about.html', context = default_context)


class ArticlesView(View):
    '''Controller for the list of articles'''

    def get(self, request, page, *args, **kwargs):
        '''GET request'''

        # pagination https://docs.djangoproject.com/en/2.2/topics/pagination/
        context = default_context
        posts = Article.objects.all()
        paginator = Paginator(posts, 10)  # How many articles per page
        context['posts'] = paginator.get_page(page)
        return render(request,
            'article/index.html', context=context)


class ClearDBView(View):
    '''Controller for clearing the database'''

    def post(self, request, *args, **kwargs):
        Article.objects.all().delete()
        return redirect("/posts/1")


class DefaultView(View):
    '''Controller for /'''

    def get(self, request, *args, **kwargs):
        '''GET request'''

        return redirect("/about/")

class ParseView(View):
    '''Controller for parsing'''

    def get(self, request, *args, **kwargs):
        '''GET request'''

        context = default_context
        num_pages, num_urls, num_in_db = parse()
        context['num_pages'] = num_pages
        context['num_urls'] = num_urls
        context['num_in_db'] = num_in_db
        return render(request,
            'article/parse.html', context=context)

class PostView(View):
    '''Controller for a single article'''

    def get(self, request, post_id, *args, **kwargs):
        '''GET request'''

        context = default_context
        post = Article.objects.filter(id=post_id)
        if post:
            context['that_post'] = post[0]
        else:
            raise Http404("Статья с этим номером не найдена")
        return render(request,
            'article/post.html', context=context)