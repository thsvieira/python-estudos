'''
Trabalhando com *args e **kwargs - O *args é um parâmetro que aceita vários argumentos, sem precisar especificar cada um deles na função,

Todos os valores recebidos pelo *args são colocados em uma tupla, portanto esses valores passam ser imutáveis porém ainda é
possível trabalhar com eles

Vejamos um exemplo
'''

def soma_de_numeros(*args): #No parâmetro da função, declaramos que ela vai usar um *args
    total = 0
    for numero in args: #Aqui criamos um for que vai percorrer os dados armazenados na tupla formada pelo *args
        total = total + numero 
    return total #Retorna o valor da soma

print(soma_de_numeros(2, 2)) #4
print(soma_de_numeros(1, 4, 5)) #10
print(soma_de_numeros(3, 3, 3, 1, 5)) #15
print(soma_de_numeros(10, 15, 20, 25, 30, 35, 40, 45)) #220

'''
Percebemos que independente da quantidade de argumentos, a função vai funcionar normalmente, evitando erros como diferença
na quantidade de argumentos em relação aos parâmetros da função

Podemos melhorar ainda mais essa mesma função, confira o exemplo abaixo
'''

def soma_de_numeros(*args): 
    return sum(args) #Podemos usar a função 'sum' para simplesmente somar todos os dados armazenados na tupla

print(soma_de_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)) #120


'''
O *args também pode ser usados para receber vários dados que não são obrigatórios para um função e depois verificar
se os dados armazenados podem ser utilizados de alguma forma

Como por exemplo, verificar se uma palavra apareceu 
'''

def verificador(*args):
    for i in args:
        if 'Python' in args:
            return 'Aqui tem a palavra Python!'
        else:
            return 'Aqui não tem a palavra Python'
    

print(verificador('Banana', 3, 'Sapato', 29.4, 'Carro'))
print(verificador('Brasil', 5, 10000, 'Python'))

'''
Existe um outro parâmetro parecido com *args em Python, é o parâmetro **kwargs. Assim como o *args, o **kwargs aceita uma quantidade indeterminada de argumentos
porém, ao invés de colocar os dados em uma tupla, ele armazena em forma de dicionário. Então, é importante ao informar o argumento, qual será
a chave associada a esse argumento. 

Confira o exemplo abaixo:
'''

def comidas_favoritas(**kwargs):
    for pessoa, comida in kwargs.items(): #Aqui usamos a função .items() para percorrer por cada valor atribuído dentro do dicionário
        print(f'A comida favorita de {pessoa} é {comida}')

comidas_favoritas(Marcela='Lasanha', Pedro='Feijoada', Augusto='Coxinha', Mariana='Pizza')

'''
É importante ressaltar que os parâmetros precisam seguir uma ordem específica dentro de uma função

Sempre é colocado 1° os parâmetros obrigatórios,
2° os parâmetros opcionais com *args
3° os paramêtros 'default'
E por último, os **kwargs

Exemplo:
                  obrigatório    obrigatório   opcional   parametro padrão    
def funcao_teste(param_obrig_1, param_obrig_2,   *args,   param_default=0,    **kwargs)
'''
