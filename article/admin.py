'''Classes for admin's part of the site'''

from django.contrib import admin
from article.models import Article

class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)