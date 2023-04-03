'''
Nessa aula vou aprender sobre métodos e a função Slice

Começando pelo Slice, é uma função útil para retornar somente partes de um dado, vamos entender melhor nos exemplos à seguir
'''

fruta = 'Abacate'
#index   0123456   Para entender melhor, cada string possuí um INDEX que é uma referência de posicionamento para cada caracter
print(fruta[3]) #Ao pedirmos para retornar o número 3 entre as chaves, o comando irá retornar a posição 3 do Index, que é a letra C


#Nesse outro exemplo, iremos usar números e aqui o objetivo será retonar somente as casas decimais

numero = str(99.75) #Aqui usamos casting juntamente com a inserção de dados da variável, sem precisar criar outra linha de código pra isso. O objetivo é retornar o 75
#index       01234
print(numero[3:5]) #Para criar um efeito de buscar de X até Y, usa-se : entre as posições buscadas. Para buscar até a ultima casa, deve-se declarar 1 posição do index a mais

'''
Métodos dentro de Strings, são algumas funções úteis para manipular a saída de dados

Para usar um método dentro de uma string, basta adicionar um ponto seguido do nome do método
'''

mensagem = 'Eu adoro comida Caseira'
print(mensagem.lower()) #Nesse método, todo o texto será convertido para letras minúsculas

mensagem = 'Eu adoro comida Caseira'
print(mensagem.upper()) #Nesse método, todo o texto será convertido para letras maiúsculas

mensagem = 'eu adoro comida Caseira'
print(mensagem.capitalize()) #Nesse método, a primeira letra da string será convertida em letra maiúscula

mensagem = 'Eu adoro comida Caseira'
print(mensagem.find('c')) #Aqui usei um método para buscar aonde está o primeiro caracter c, e ele me retorna a posição do index onde ele está

mensagem = 'Eu adoro comida Caseira'
print(mensagem.find('C')) #Como o Python é uma liguagem Case Sensitive, isto é, existe diferença entre letras maiúsulas e minuscúlas, então ira retornar a posição do C maiúsculo

mensagem = 'Eu adoro comida Caseira'
print(mensagem.find('adoro')) #Podemos também descobrir onde se inicia uma determinada palavra, retornando o valor do index de onde ela se inicia

mensagem = 'Eu adoro comida Caseira'
print(mensagem.replace('a' , 'e')) #Nesse método, trocamos um dado por outro. Aqui trocamos todos os caracteres  A por E. 

mensagem = 'Eu adoro comida Caseira'
print(mensagem.replace('Caseira' , 'feita em casa')) #É possível usar o replace para trocar palavras e partes de uma string também.

mensagem = '      Eu adoro comida Caseira'
print(mensagem.strip()) #Esse método remove todos os espaços antes do primeiro caracter, é útil para validar inserções feitas de forma errônea por um usuário.

'''
Esses são apenas alguns dos métodos usados em Python, que são bastante úteis na manipulação de strings.

Aqui foram usandos os seguintes métodos como exemplo:

lower -> transforma tudo em minúsculo
upper -> transforma tudo em MAIÚSCULO
capitalize -> Tranforma o primeiro caracter em maiúsculo
find -> procura por algo dentro da string
replace -> substitui algo na string
strip -> remove espaços antes do primeiro caracter

'''