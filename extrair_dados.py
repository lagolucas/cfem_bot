from bs4 import BeautifulSoup
import requests
import json
import calendar
from datetime import datetime

with open("urls.json", encoding='utf-8') as jsonfile:
        urls = json.load(jsonfile)

page = requests.get(urls['nacional'])
soup = BeautifulSoup(page.content, "html.parser")

tabela = soup.find(class_="tabelaRelatorio")
linhas = tabela.find_all("tr")

dict = {}

for linha in linhas:
	estado = linha.find(href = True)
	if estado:
		dict[estado.text.strip()] = {}
		celulas = linha.find_all("td", style="text-align: right;")
		i = 1
		for celula in celulas:
			if i <= 12:
				dict[estado.text.strip()][calendar.month_name[i]] = float(celula.text.strip().replace(".", "").replace(",", "."))
			else:
				dict[estado.text.strip()]["Anual"] = float(celula.text.strip().replace(".", "").replace(",", "."))
			i+=1

with open("dados/" + datetime.now().strftime("%Y%m%d") + '.json', 'w') as fp:
    json.dump(dict, fp)
