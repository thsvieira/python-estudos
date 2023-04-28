'''
Dicionários em Python - No Python, dicionário é uma estrutura de dados que armazena valores associados a uma chave(Key) e
valor(Value). 

A estrutura básica é escrita dessa forma: {'chave': 'valor'}. Utiliza {} para estruturar o dicionário e a chave é separada 
do valor por dois pontos.

É uma estrutura indexada(pelas chaves) e aceita diferentes tipos de dados

Vamos à alguns exemplos:
'''

carro = {'modelo': 'flex', 'ano': 2023, 'montadora': 'FIAT'}
print(carro) #Imprime todo o conteúdo armazenado no dicionário
print(carro['ano']) #Vai retornar somente o valor que está indexado em 'ano'

#Uma forma simples de alterar o valor associado à alguma chave é fazer como no exemplo abaixo
carro['montadora'] = 'Chevrolet'
print(carro['montadora']) #'montadora': 'FIAT' foi alterado para 'montadora': 'Chevrolet'

#Podemos também utilizar a função .update({}) quando for necessário alterar mais de um elemento ao mesmo tempo
carro.update({'modelo': 'Gasolina', 'ano': 2019})
print(carro) #{'modelo': 'Gasolina', 'ano': 2019, 'montadora': 'Chevrolet'}

#Também é possível adicionar uma nova chave para associar outros valores no dicionário criado
carro.update({'cor': 'Preto'})
print(carro) #{'modelo': 'Gasolina', 'ano': 2019, 'montadora': 'Chevrolet', 'cor': 'Preto'}
#Toda chave criada dessa forma vai para o fim do dicionário conforme apresentado no exemplo

#Além de adicionar novas chaves, podemos remove-las também usando o DEL, exemplo:
del carro['cor']
print(carro) #{'modelo': 'Gasolina', 'ano': 2019, 'montadora': 'Chevrolet'} a chave 'cor' foi removida

'''
Uma forma de extrair dados de dentro de um dicionário, é usando um For Loop especificando o que você precisa
Como por exemplo, somente as chaves, somente os valores  ou ambos

Exemplo:
'''
for x in carro.keys(): #Retorna somente as chaves(keys)
    print(x) 

for y in carro.values(): #Retorna somente os valores(values) associados as chaves
    print(y)

for chaves, valores in carro.items(): #Usando a função .items() associado a 2 variáveis de controle, retorna ambos os valores
    print(chaves, valores)

#Vale ressaltar, que é possível adicionar mais de um valor associado a uma chave usando a função .update({'chave':['dados']})

carro.update({'cores': ['Prata', 'Preto', 'Vermelho', 'Branco']})
print(carro) #{'modelo': 'Gasolina', 'ano': 2019, 'montadora': 'Chevrolet', 'cores': ['Prata', 'Preto', 'Vermelho', 'Branco']}

'''
Em algum momento, nosso dicionario pode ficar muito grande, com várias chaves e valores.

Colocar tudo em uma única linha, pode acabar atrapalhando na visualização assim como na manipulação direta

Pra resolver isso, podemos simplesmente identar de uma forma mais harmônica conforme no exemplo abaixo:
'''
carro = {
    'modelo': 'Gasolina', 
    'ano': 2019, 
    'montadora': 'Chevrolet', 
    'cores': ['Prata', 'Preto', 'Vermelho', 'Branco']
}

#Dessa forma fica muito mais legível e fácil para manipular o dicionário de forma direta