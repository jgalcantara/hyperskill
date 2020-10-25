import os
import sys
import requests
from collections import deque
from bs4 import BeautifulSoup
from colorama import Fore

tab_stack = deque()


def system_path():
    args = sys.argv
    path = str(args[1])
    return path


def file_save(pathname, urlx, listx):
    if ".com" in urlx:
        urlx = urlx.rstrip(".com")
    if ".org" in urlx:
        urlx = urlx.rstrip(".org")
    browser = open(f'{pathname}/{urlx.lstrip("https://")}', "w+",  encoding='UTF-8')
    browser.writelines(listx)
    browser.close()


def file_read(pathname, urlx):
    tab = open(f'{pathname}/{urlx}', 'r')
    for line in tab:
        print(line)
    tab.close()


def url_get(pathname, urlx):
    if "https" not in urlx:
        urlx = f'https://{urlx}'
    r = requests.get(urlx)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find_all('a')
    sx = []
    for i in s:
        i = str(i.get_text())
        print(Fore.BLUE + i)
        sx.append(i)
    file_save(pathname, urlx, sx)


pathx = system_path()
if not os.path.exists(pathx):
    os.mkdir(pathx)

while True:
    url = input()
    if "." in url:
        url_get(pathx, url)
        tab_stack.append(url)
    elif url == 'back':
        if len(tab_stack) != 0:
            tab_stack.pop()
            url = tab_stack.pop()
            file_read(pathx, url)
    elif url == "exit":
        break
    else:
        print("Error: Incorrect URL")
