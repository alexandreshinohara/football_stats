import requests
from time import sleep
from pathlib import Path
from random import random
tempo = 0.0
for x in range(1, 203):
    filename = Path('Sumulas_Paulistao/2022/' + str(x) + ' jogo.pdf')
    URL = 'https://conteudo.fpf.org.br/sumulas/2022/3973/' + str(x) + '.pdf'

    page = requests.get(URL)

    filename.write_bytes(page.content)
    dormir = (random() * 2) + 2
    tempo += dormir
    print(str(x) + ' jogo OK. Wait time: ' + str(dormir))
    sleep(dormir)
print('fim. tempo total = ' + str(tempo))
