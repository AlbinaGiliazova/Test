# -*- coding: utf-8 -*-
'''Serializers'''

from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    '''Serializer for Article model'''

    title = serializers.CharField(max_length=200)
    text = serializers.CharField(max_length=5000)
    url = serializers.URLField()  # default length 200
