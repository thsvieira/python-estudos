'''
Sequence Unpacking  - Uma outra forma de trabalhar com listas, é associando os itens de uma lista a outras variáveis.

Podemos fazer isso com todos os itens da lista de forma individual (uma variável para cada item), ou, agrupar itens
em uma nova lista

Exemplos:
'''

#Aqui temos uma lista de cores
cores = ['vermelho', 'azul', 'verde', 'amarelo']
print(cores)

'''
Para associar o 1°, 2°, 3° e 4° item, podemos adiciona-los cada um em uma variável diferente especificando qual item da
lista será adicionado usando o index da lista como referência
'''

vermelho = cores[0]
azul = cores[1]
verde = cores[2]
amarelo = cores[3]

print(vermelho)
print(azul)
print(verde)
print(amarelo)

'''
A linguagem Python permite uma forma melhor de fazer isso usando sequence unpacking

Basicamente, você pode associar itens de uma lista à multiplas variaveis em apenas uma linha
'''
#Aqui cada variável vai ser associada sequencialmente a cada item da lista cores
red, blue, green, yellow = cores
#     red       blue    green    yellow
# ['vermelho', 'azul', 'verde', 'amarelo']
#      0         1        2         3     
print(red)
print(blue)
print(green)
print(yellow)

'''
Se quisermos associar apenas alguns itens da listas a variáveis, podemos associar o restante à uma nova lista usanado o *

Confira o exemplo abaixo:
'''

veiculos = ['Carro', 'Caminhão', 'Furgão', 'Moto', 'Bicicleta']
carro, caminhão, furgao, *duas_rodas = veiculos #Aqui associamos cada item à uma variável e somente os itens 'Moto' 
#e 'Bicicleta foram adicionados a uma nova lista associada a variável duas_rodas

print(veiculos) #Imprime todos os itens da lista veiculos
print(duas_rodas) #Imprime somentes os itens associados a variavel duas_rodas
