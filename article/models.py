'''Data models for article app'''

from django.db import models

class Article(models.Model):
    '''An article has title, text and url.
    Methods: __str__'''

    title = models.TextField(max_length=200)
    text700 = models.CharField(max_length=700, blank=True)
    text = models.TextField(max_length=5000)
    url = models.URLField()  # default length 200

    def __str__(self):
        '''String representation of class instances'''

        return self.title

    class Meta:
        ordering = ["-id"]
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

