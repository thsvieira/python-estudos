'''
Manipulando Listas - Alémn das funções nativas do Python para manipular listas, podemos trabalhar de outras formas

Vamos à alguns exemplos:
'''

frutas = ['Maçã', 'Banana', 'Goiaba', 'Abacaxi', 'Uva'] * 2 #Multiplicando a lista de forma direta, repete todos os itens 2x
print(frutas)

#Podemos também "somar" listas (concatenar) simplesmente usando o operador +
valores = [10, 20, 30, 40, 50] + frutas #Na lista valores, será adicionado os itens da lista frutas
print(valores)

#Pode também usar outras variáveis para armazenar as listas manipuladas, exemplo:
listas = valores + frutas
print(listas)

#Também podemos usar a função extend para concatenar listas
lista_1 = [1, 3, 5, 7, 9]
lista_2 = [2, 4, 6, 8, 10]

lista_1.extend(lista_2) #Aqui estamos adicionando os valores da lista_2 em lista_1
print(lista_1)

#Uma outra forma de concatenar listas, é criando listas dentro de listas

objetos = [['Cadeado', 'Tesoura'], ['Martelo', 'Alicate']] #Ao separar os itens dentro das listas com [], criamos 2 sublistas

'''
Ao criarmos sublistas, alteramos o index das listas. Exemplo:
indice sublista ->                     0                       1
                 objetos = [['Cadeado', 'Tesoura'], ['Martelo', 'Alicate']]
indice itens na sublista ->      0          1            0          1

Através do índice, podemos extrair somente os dados de alguma determinada sublista
'''
#[indice][posição]
print(objetos[0]) #Vai imprimir somente os itens da sublista na posição 0 
print(objetos[1]) #Vai imprimir somente os itens da sublista na posição 1
print(objetos[1][0]) #Dentro da sublista na posição 1, vai imprimir o item na posição 0

