import os
import time
from bs4 import BeautifulSoup
import requests


def demo():
    try:
        os.path.join()
        with open('data.txt', 'w') as file:
            for f in file:
                print(f.lower())
    except Exception as err:
        print(err)


def demo1():
    r=requests.get('https://www.hao123.com/')
    BeautifulSoup.find_all()
    print(r.text)


if __name__ == '__main__':
    demo1()
