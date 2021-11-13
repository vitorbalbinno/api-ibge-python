import requests

nome = input('Digite um nome: ')
sexo = input('Sexo (F/M)? ')

listaRanking = {}
listaNome = {}
periodos = {0: '1930', 1: '1930-1940', 2: '1940-1950', 3: '1950-1960', 4: '1960-1970',
            5: '1970-1980', 6: '1980-1990', 7: '1990-2000', 8: '2000-2010'}

paramsNome = {'sexo': sexo}
urlNome = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'
nomeResultado = requests.get(urlNome, params=paramsNome).json()

urlRanking = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking'
rankingResultado = requests.get(urlRanking).json()


for i in rankingResultado:
    for j in i['res']:
        listaRanking[j['nome']] = j['frequencia']

valor = 0
for i in nomeResultado:
    for j in i['res']:
        listaNome[periodos[valor]] = j['frequencia']
        valor += 1

print(f'\nO nome que você digitou foi {nome.capitalize()}, aqui temos a quantidade de registros para esse nome:\n')
print('PERÍODO(em décadas)'.ljust(50), 'QUANTIDADE')
for k, v in listaNome.items():
    print(k.ljust(50), v)

print('\nEsse é o ranking dos 20 nomes mais registrados no Brasil(1930 - 2010):\n')
print('NOME'.ljust(50), 'QUANTIDADE')
for k, v in listaRanking.items():
    print(k.ljust(50), v)