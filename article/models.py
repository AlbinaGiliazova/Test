'''Data models for article app'''

from django.db import models

class Article(models.Model):
    '''An article has title, text and url.
    Methods: __str__'''

    title = models.TextField(max_length=200)
    text = models.TextField(max_length=5000, blank=True)
    url = models.URLField()  # default length 200

    def __str__(self):
        '''String representation of class instances'''

        return self.title

    @property
    def text_700(self):
        return self.text[:701] if len(self.text) > 700 else self.text

    class Meta:
        ordering = ["-id"]
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
