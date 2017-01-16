# coding=utf-8
import requests
from bs4 import BeautifulSoup
import random


def joke():
    alljoke = []
    url = 'http://www.qiushibaike.com'
    r = requests.get(url)
    content = r.content
    soup = BeautifulSoup(content)
    allcontent = soup.find_all(attrs={'class': 'content'})

    for i in allcontent:
        alljoke.append(i.text)

    joke = alljoke[random.randint(0, len(alljoke) - 1)]
    return joke


