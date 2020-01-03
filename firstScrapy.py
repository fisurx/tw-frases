from bs4 import BeautifulSoup
import requests

import pandas as pd

url = "https://www.chiquipedia.com/frases-bonitas/frases-cortas/"
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

eq = soup.find_all("div", class_="contenido")


res = list()
frases = []

for i in eq:
   res.append(i.text)

lista = res[0].split("\n")
lista.pop(0)

frases = lista

for i in frases:
    print i