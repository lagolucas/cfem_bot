import os
from json import load
from json import dump
from datetime import datetime

directory = os.fsencode("dados")
files = os.listdir(directory)
files.sort(reverse=True)

with open('dados/' + files[0].decode('UTF-8'), 'r') as jsonfile:
	dados_hoje = load(jsonfile)

with open('dados/' + files[1].decode('UTF-8'), 'r') as jsonfile:
	dados_ontem = load(jsonfile)

variacao = {}
for estado, dados in dados_hoje.items():
	variacao[estado] = {}
	for mes, valor in dados.items():
		if dados_ontem[estado][mes] != valor:
			variacao[estado][mes] = valor - dados_ontem[estado][mes]


with open("variacoes/" + datetime.now().strftime("%Y%m%d") + '.json', 'w') as fp:
    dump(variacao, fp)
