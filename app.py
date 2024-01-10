# Importando as bibliotecas que vamos usar
from datetime import datetime
import requests

# Criando uma funcao que mostra data e hora ja formatados
def data_hora():
    data = datetime.now()
    formato_personalizado = "%A, %d de %B de %Y - %H:%M:%S"
    data_formatada = data.strftime(formato_personalizado)

    # mostrando a hora e data atual    
    print("{:>27}{:^96}{:<20}".format(elemento_esquerda, data_formatada, elemento_direita))
    print(linha_centralizada)


# Criando uma funcao que mostra o clima 
def clima():
    # recebendo o nome da cidade
    print('{:>27}'.format(elemento_esquerda), end='')
    NomeDaCidade = input('Informe o nome da cidade: ')
    print(linha_centralizada)
    # validando chave de api
    chave_api = 'daf16b60db76b1b4008da805bbbf0bf6'
    cidade = NomeDaCidade

    # Construindo a URL da API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt&units=metric'

    # Fazendo a solicitação HTTP
    resposta = requests.get(url)

    # Verificando se a solicitação foi bem-sucedida (código de resposta 200)
    if resposta.status_code == 200:
        dados_clima = resposta.json()

        # Informações climáticas centralizadas
        print("{:>27}{:^96}{:<20}".format(elemento_esquerda, f"Condição climática em {cidade}", elemento_direita))
        print("{:>27}{:^96}{:<20}".format(elemento_esquerda, f"Temperatura: {dados_clima['main']['temp']}", elemento_direita))
        print("{:>27}{:^96}{:<20}".format(elemento_esquerda, f"Condição: {dados_clima['weather'][0]['description']}", elemento_direita))
        print(linha_centralizada)
    else:
        # Mensagem de erro centralizada
        print("{:^150}".format(f"Erro na solicitação. Código de resposta: {resposta.status_code}"))



# criando uma variavel com a linha centralizada
linha = '=' * 100
linha_centralizada = linha.center(150)

# Elementos a serem exibidos
elemento_esquerda = "||"
elemento_centro = "CLIMA TEMPO"
elemento_direita = "||"

# Tamanho total da linha desejada
tamanho_total = 80

# Formatar a linha com alinhamentos diferentes
linha_formatada = "{:>27}{:^96}{:<20}".format(elemento_esquerda, elemento_centro, elemento_direita)



# Criando tela de apresentacao das informacoes 
print('=' * 150)
print(linha_centralizada)
print(linha_formatada)
print(linha_centralizada)
data_hora()
clima()
print('=' * 150)
print('PROGRAMA FINALIZADO'.center(150))
print('=' * 150)
