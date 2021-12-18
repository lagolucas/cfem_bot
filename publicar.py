from json import load
import twitter_auth
from datetime import datetime

# importar o arquivo de hoje
file_name = datetime.now().strftime("%Y%m%d") + ".json"

with open ("variacoes/" + file_name, "r") as variacoes_file:
	variacoes = load(variacoes_file)

api = twitter_auth.autentica();

for estado, dados in variacoes.items():
	if (dados):
		previous_tweet = api.create_tweet (text = "Para o estado " + estado + " as variações do CFEM foram:")
		for mes, variacao in dados.items():
			previous_tweet = api.create_tweet(text = "No mês de " + mes + " o valor foi de " + str(variacao) + " R$.",
			in_reply_to_tweet_id=previous_tweet.data['id'])

