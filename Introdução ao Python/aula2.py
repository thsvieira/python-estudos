'''
Python é uma linguagem de tipagem dinâmica, ou seja, não é necessário declarar qual é o tipo de conteúdo que irá ser armazenado na variável,
pois a própria linguagem se encarrega de identificar qual é o tipo de dado armazenado

Existem basicamente 4 tipos de dados:

Integer: Números inteiros
Floating Point(float): Número fracionários
String: Sequência de caracteres
Boolean(bool): True ou False

'''

#Para declarar uma variável em Python, basta dar um nome a ela e atribuir um valor

x = 10

print(x)

#Para declarar uma string basta acrescer aspas simples que a linguagem já ira interpretar como uma sequência de caracteres

m = 'Olá'

print(m)


# É possível manipular os dados através de um recurso chamado Casting, sinalizando que um determinado dado seja lido da forma esperada

x = str(3) # Nesse exemplo a variável X será lidaa como uma String
y = int(4) # Nesse exemplo a variável y será lida como um Integer
z = float(5) #Nesse exemplo a variável z seráa lida como um Float

print(x + x) 
print(y + y)
print(z + z)

'''
Essa é uma forma SIMPLES de concatenar textos e variáveis

Vamos a seguinte frase como exemplo:

Meu nome é Thalisson, tenho 30 anos de idade e moro em Maringá - PR
'''

nome = 'Thalisson'
idade = str(30) #Aqui foi necessário converter o número em string porque não é possível concatenar integer com strings
cidade = 'Maringá - PR'

print('Meu nome é ' + nome + ' tenho ' + idade + ' anos de idade e moro em ' + cidade)