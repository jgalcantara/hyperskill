import sys
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) '
                         'Version/7.0.3 Safari/7046A194A'}

languages = ['arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese', 'dutch', 'polish', 'portuguese',
             'romanian', 'russian', 'turkish']


def parser(lang, lang2, word, x, y):
    url = f"https://context.reverso.net/translation/{lang}-{lang2}/{word}"
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    original_translate = soup.find_all("a", class_="translation")
    sentences = (soup.find("section", id='examples-content')).find_all("span", class_='text')
    translated_list = [ix.get_text().strip() for ix in original_translate[1:x]]
    translated_sentx = [sentences[iy].get_text().strip() + "\n" if iy % 2 != 0 else sentences[iy].get_text().strip()
                        for iy in range(0, y)]
    print(f"\n{lang2.capitalize()} Translations:")
    file_word.write(f"\n{lang2.capitalize()} Translations:\n")
    print(*translated_list, sep="\n")
    for trans in translated_list:
        file_word.write(trans + '\n')
    print(f"\n{lang2.capitalize()} Examples:")
    file_word.write(f"\n{lang2.capitalize()} Examples:\n")
    print(*translated_sentx, sep="\n")
    for trans in translated_sentx:
        file_word.write(trans + '\n')


args = sys.argv
lang_o = args[1]
lang2_o = args[2]
word_o = args[3]

s = requests.Session()
file_word = open(f'{word_o}.txt', 'w', encoding='utf-8')

try:
    if lang2_o == "all":
        for lng in languages:
            if lng == 'english':
                continue
            else:
                try:
                    parser(lang_o, lang2_o, word_o, 6, 10)
                except (IndexError, AttributeError):
                    print(f"Sorry, unable to find {word_o}")
                    break
    elif lang2_o not in languages:
        print(f"Sorry, the program doesn't support {lang2_o}")
    else:
        try:
            parser(lang_o, lang2_o, word_o, 6, 10)
        except (IndexError, AttributeError):
            print(f"Sorry, unable to find {word_o}")
            exit()
except requests.exceptions.ConnectionError:
    print("Something wrong with your internet connection")

file_word.close()
