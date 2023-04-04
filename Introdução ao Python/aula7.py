'''
Operador Ternário é uma excelente forma de deixar uma condição mais legível

E ao mesmo tempo, diminuir o tamanho do código

Pegando como exemplo uma condição simples sobre idade permitida para votação
'''

idade = 13

if idade >= 16:
    resultado = 'Voto Permitido'
else:
    resultado = 'Voto não Permitido'

print(resultado)

#Agora veja a diferença usando um operador ternário

idade = 17

resultado = 'Voto Permitido' if idade >= 16 else 'Voto não Permitido'

print(resultado)

'''
Da mesma forma que deixamos o código mais limpo acima, podemos fazer com múltiplos operadores de comparação

Vejamos um exemplo
'''

valor = 20

if valor >= 20 and valor < 40: #Aqui basicamente compara-se se o valor do produto está dentro do permitido 
    print('Produto foi Aceito')
else:
    print('Produto não foi Aceito')

#Agora vejamos outro exemplo executando a mesma lógica porém de uma forma mais limpa

valor = 10

if 20 <= valor < 40: #A lógica se mantém a mesma, porém, não precisou repetir a variável valor 2x
    print('Produto foi Aceito')
else:
    print('Produto não foi Aceito')