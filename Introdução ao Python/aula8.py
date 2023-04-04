'''
Hoje vamos começar a entender melhor sobre estruturas de repetição em Python

Começando por Laços ou For Loops

Loop é bastante usado quando se tem ideia de quantas repetições serão necessárias para executar algo

Vamos aos exemplos:
'''

for numero in range(5): #Vai imprimir uma sequência de 0 até 4, se quisermos imprimir de 0 até 5, mudamos o range para 6
    print(numero)

'''
for inicia o laço, seguido pelo nome de uma variável qualquer que vai armazenar as repetições

in quer literalmente dizer "dentro"

range é uma função para estipular um alcance para as repetições, onde começa e até onde vai

A função range, aceita alguns parâmetros: start, stop e step

start vai dizer à partir de qual número começar, stop diz onde deve parar 

E com step você pode pular uma quantidade X de laços, seria a quantidade de incrementos
'''

for numero in range(1, 5): #Vai imprimir uma sequência de 1 até 4
    print(numero)

for numero in range(1, 20, 2): #Vai imprimir uma sequência de 1 até 19 pulando 1 repetição. Imprime um, pula o próximo.
    print(numero)

'''
Também é possível usar Loops com strings, de forma que você consegue acessar cada caracter da string

Veja o exemplo abaixo:
'''

palavra = 'Google'

for letra in palavra: #Aqui o laço vai percorrer cada caracter da string que está armazenada na variável palavra, 
    #e jogar esse resultado dentro da variável letra, imprimindo até acessar todos os caracteres de palavra
    print(f'{letra} está dentro da palavra {palavra}')

