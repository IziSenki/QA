#WS
import requests
from bs4 import BeautifulSoup

# 1. Coletar manchetes da CNN
cnn_url = 'https://www.cnnbrasil.com.br/'
cnn_response = requests.get(cnn_url)

if cnn_response.status_code == 200:
    soup = BeautifulSoup(cnn_response.text, 'html.parser')
    print("\n🔴 Últimas notícias da CNN:")
    for manchete in soup.find_all('h3')[:5]:  # Pega as 5 primeiras manchetes
        print(f"- {manchete.text.strip()}")
else:
    print(f"Erro ao acessar CNN: {cnn_response.status_code}")

# 2. Verificar preço do Bitcoin
btc_url = 'https://www.coindesk.com/price/bitcoin'
btc_response = requests.get(btc_url, headers={'User-Agent': 'Mozilla/5.0'})

if btc_response.status_code == 200:
    soup = BeautifulSoup(btc_response.text, 'html.parser')
    preco = soup.find('div', class_='price-large')
    print(f"\n💰 Preço do Bitcoin: {preco.text.strip() if preco else 'Não encontrado'}")
else:
    print(f"Erro ao acessar CoinDesk: {btc_response.status_code}")
