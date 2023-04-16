# ДЕРОРАТОРЫ ФУНКЦИЙ

import webbrowser


def walidator(func):
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Неверный URL")


    return wrapper


@walidator
def open_url(url):
    webbrowser.open(url)

open_url("https://itproger.com")
# open_url("https://gb.ru")












