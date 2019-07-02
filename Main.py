import requests 
from bs4 import BeautifulSoup

URL = input('Cole a url Kabum: ')
precoRequirido = float(input("Preço esperado: "))

headers = {}
#headerAux = input("Paste de hader: ")

headers = ({"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'})

pagina = requests.get(URL, headers = headers)
soup = BeautifulSoup(pagina.content, 'html.parser')

def getDados():
	titulo = soup.find(id = "titulo_det").get_text()

	for span in soup.find('div', class_='preco_desconto-cm').findAll('strong'):
		preco = span.text

	aux = ""
	tamanhoPreco = 0	
	for i in preco:
		if tamanhoPreco > 2:
			aux += str(i);
		tamanhoPreco += 1;

	aux = aux.replace(".", "")
	aux = aux.replace(",", ".")

	preco = float(aux)

	titulo = titulo.strip()

	return preco, titulo

def analisaPreco(preco, precoRequirido):
	if preco < precoRequirido:
		return True
	
	return False

preco, titulo = getDados()

if analisaPreco(preco, precoRequirido):
	print("\nProduto:", titulo, "esta disponivel por: R$", preco)
