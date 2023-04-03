'''
Aqui vamos aprender sobre operações matemáticas, de comparação e atribuição em Python

Para relembrar, algumas operações matemáticas tem prioridade em relação à outras

1. Parênteses (Primeiro calcula tudo que estiver entre parênteses)
2. Exponenciação
3. Multiplicação e Divisão
4. Soma e Subtração

'''

calculo = 2 + 2 #Soma simples
print(calculo)

calculo = 2 * (2 + 3)#Aqui soma primeiro, e depois multiplica pelo resultado da soma
print(calculo)

calculo = 2 ** 3 #Exponenciação em Python é feito com o uso de dois asteriscos
print(calculo)

'''
Um pequeno resumo de operadores de comparação em Python

==  Igual à
=!  Não é igual
>  Maior que
< Menor que
>= Maior ou igual
<= Menor ou igual

'''

numero = 10 == 10
print(numero) #Aqui o resultado será apresentado como TRUE, porque comparações lógicas tem resultado booleano: verdadeiro ou falso. 

texto = 'banana' == 'banana'
print(texto) #Também funciona para comparar strings, verifica a se a sequência de caracteres é igual a da outra palavra. *Lembrando que a linguagem é Case Sentitive*

'''
Operadores de Atribuição manipulam a entrada de dados de forma simples e bastante eficiente

Vejamos alguns exemplos
'''

x = 5 #Aqui atribuimos o valor 5 a variável x
print(x) 

x = 5 #Aqui atribuimos o valor 5 a variável x
x = x + 10 #Aqui adiciomos o valor que já estava armazenado na variável + o valor 10
print(x) 

x = 5
x += 10 #Nessa linha, usamos um operaador de atribuição (colando o + antes do =), dizendo que estamos adicionando a variável x o valor dela mais outro valor específico
print(x)

'''
Isso pode ser usado tanto para multiplicação, divisão, subtração e etc.

Basta usar o operador matemático desejado antes do =
'''