'''
Vamos aprender a interagir com o usuário, como pedir para que o usuário insira um dado que vamos precisar e o programa armazene esse dado em uma variável

Pra isso, usamos a função input

Essa função é usada para receber um dado e armazena-la em uma variável

Vamos pegar como exemplo o contexto da última aula

'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
idade = str(idade) #Aqui foi necessário converter o número em string porque não é possível concatenar integer com strings
cidade = input('Digite o nome da cidade onde você mora: ')

print('Meu nome é ' + nome + ' tenho ' + idade + ' anos de idade e moro em uma cidade chamada ' + cidade)


#Vamos criar agor um pequeno programa que calcula qual a idade do usuário com base nos dados inseridos

ano_nascimento = input('Digite o ano em que você nasceu: ')
ano_atual = input('Digite o ano atual: ')
idade = int(ano_atual) - int(ano_nascimento) #Utilizando novamente a técnica de manipulação de dados(casting) garantimos que os dados serão tratados como números inteiros
print(idade)

'''
Existe uma maneira muito mais inteligente de concatenar strings e dados númericos como float e integer

Para isso iremos usar uma função para formatar strings. Vamos pegar o primeiro código acima e melhorar a saída formatando a string
'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
idade = str(idade) #Aqui foi necessário converter o número em string porque não é possível concatenar integer com strings
cidade = input('Digite o nome da cidade onde você mora: ')

print(f'Meu nome é {nome} tenho {idade} anos de idade e moro em uma cidade chamada {cidade}') #Dessa forma fica muito mais compreensível como será a saida de dados com as variáveis

