# -*- coding: utf-8 -*-
'''Parsing the Habr.ru best articles'''

import requests
from bs4 import BeautifulSoup
import re
from article.models import Article
from Cashoff.log_config import db_logger


def check_urls_in_db(titles, urls):
    '''Remove from the lists the articles with the urls that are already in the database'''

    numbers = []
    for i, url in enumerate(urls):
        check = Article.objects.filter(url=url)
        if check:
            numbers.append(i)
    if numbers:
        for i, title in enumerate(titles.copy()):
            if i in numbers:
                titles.remove(title)
        for i, url in enumerate(urls.copy()):
            if i in numbers:
                urls.remove(url)
    return titles, urls, len(numbers)

def clean_text(r):
    '''Get the plain text of the article'''

    soup = BeautifulSoup(r.content, 'html.parser')
    res = soup.find_all('div', {'class': 'post__text'})
    text = ''.join([i.text for i in res])
    # There are warnings:
    # Some characters could not be decoded, and were replaced with
    # REPLACEMENT CHARACTER.
    text = re.sub('\n+', '\n', text)
    return text


def get_next_page(page, r):
    '''Get the number of the next page or 0'''

    if page == -1:
        return 1
    soup = BeautifulSoup(r.content, 'html.parser')
    res = soup.find_all('a', {'class': 'arrows-pagination__item-link_next'})
    if not res:
        return 0
    page = [i.get('href') for i in res][0][12:-1]
    return page

def get_page(page):
    '''Get a page of the best Habr.ru articles'''

    error = False
    if page == 0:
        error = True
        return '', error
    elif page == 1:
        url = 'https://habr.com/ru/top/'
    else:
        url = 'https://habr.com/ru/top/page' + page + '/'
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    except:
        error = True
    if r.status_code != 200:
        error = True
    return r, error


def get_texts(urls):
    '''Get the texts of the articles with these urls'''

    texts = []
    for url in urls:
        text = get_url(url)
        texts.append(text)
    return texts


def get_titles(r):
    '''Get titles and urls of articles from the page'''

    error = False
    soup = BeautifulSoup(r.content, 'html.parser')
    res = soup.find_all('a', {'class': 'post__title_link'})
    if res:
        titles = [i.text for i in res]
        urls = [i.get('href') for i in res]
    else:
        error = True
    if len(titles) != len(urls):
        error = True
    if error:
        return '', '', error
    return titles, urls, error


def get_url(url):
    '''Get the text of the article with this url'''

    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if r.status_code != 200:
        return ''
    return clean_text(r)


def write_db(titles, texts, urls):
    '''Write into the database the obtained articles'''

    for i in range(len(urls)):
        article = Article()
        article.title = titles[i]
        article.text = texts[i]
        article.url = urls[i]
        article.save()

def parse():
    '''Main function for parsing.py'''

    page = -1
    r = ''
    num_pages, num_urls, num_in_db = 0, 0, 0
    while page:
        page = get_next_page(page, r)

        r, error = get_page(page)
        if error:
            break

        titles, urls, error = get_titles(r)
        if error:
            continue
        num_pages += 1

        titles, urls, num = check_urls_in_db(titles, urls)
        num_in_db += num
        if not urls:
            continue

        num_urls += len(urls)
        texts = get_texts(urls)

        write_db(titles, texts, urls)

    logger = db_logger('article.parsing.py')
    logger.info(f'Parsed {num_pages} pages, {num_urls} new urls.' +
                f' {num_in_db} already in the database.')

    return num_pages, num_urls, num_in_db

if __name__ == '__main__':
    parse()
