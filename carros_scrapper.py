# Imports
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Criando uma função para extrair o texto do blocos de informação dos carros
def extrai_informacao(car_block, feature1, feature2, feature3):
    feat1 = []
    feat2 = []
    feat3 = []
    for car in car_block:
        var1 = car.find('span', class_= feature1).text
        var2 = car.find('span', class_= feature2).text
        var3 = car.find('span', class_= feature3).text
        feat1.append(var1)
        feat2.append(var2)
        feat3.append(var3)
    # Cria um dataset
    cars = pd.DataFrame({feature1:feat1,feature2:feat2,feature3:feat3})
    # Imprime a primeira e ultima linhas
    print(cars[:1])
    print(cars[-1:])
    return cars

# Extraindo todos os car blocks da page
def car_blocks(text):
    cb = soup.find_all('div', class_='car_block')
    return cb


if __name__ == '__main__':
    # Grava o endereço em uma variável
    page = 'http://localhost:8000/index.html'

    # Puxa o conteúdo da pagina para resultado
    resultado = requests.get(page)
    texto = resultado.text

    # Se o status for diferente de 200, geramos mensagem de erro
    if resultado.status_code != 200:
        print("O request obteve status {}. Verifique sua conexão!".format(resultado.status_code))

    # Usando o BeautifulSoup, fazer o parse
    soup = BeautifulSoup(texto, 'html.parser')

    # Extrai os blocos de informações de carros
    cb = car_blocks(soup)
    print("Informações dos carros carregadas com sucesso")

    # Escolha as 3 variáveis a serem extraídas do texto da Web. A variável será inserida no código de acordo com o dicionário 'variaveis'
    variaveis = {1:'car_name',2:'mpg',3:'cylinders',4:'horsepower',5:'weight'}
    print('Escolha 3 variáveis para serem gravadas no arquivo .CSV.')
    print("1:'car_name',2:'mpg',3:'cylinders',4:'horsepower',5:'weight'")
    v1 = int(input('Digite o número correspondente à variável 1 : '))
    v1 = variaveis[v1]
    v2 = int(input('Digite o número correspondente à variável 2 : '))
    v2 = variaveis[v2]
    v3 = int(input('Digite o número correspondente à variável 3 : '))
    v3 = variaveis[v3]


    # Faz o parse das informações e grava em um arquivo CSV
    df = extrai_informacao(cb, v1, v2, v3)

    # Grava CSV em disco
    df.to_csv('car_info.csv', index=False)
    print('Arquivo -car_info.csv- gerado com sucesso. Obrigado por utilizar meu programa!')
