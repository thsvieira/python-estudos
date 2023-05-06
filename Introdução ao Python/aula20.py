'''
Funções: Uma forma simples de definir funçõe é dizer que são blocos de código que realizam tarefas específicas

Nós podemos definir funções em python seguindo essa estrutura:

def nome_da_funcao(dados_de_entrada):
    bloco_de_codigo_da_funcao

Exemplo:
'''

def cumprimentar(): #Repare que está função não tem um dado de entrada ou parâmetro. Ela executa uma função simples de print
    print('Oi, tudo bem?')

cumprimentar() #Escrevemos dessa forma para "chamarmos" a função, ou seja, executa-la

def contar_ate_dez():
    for i in range(10): #Podemos usar a função pra diversas finalidades. Aqui a função conta até 10 sempre que é chamada
        print(1 + i)

contar_ate_dez()

#A função vai se repetir quantas vezes ela for chamada, como no exemplo abaixo:

for i in range(5):
    cumprimentar() #Aqui a função vai ser executada 5x imprimindo a mensagem "Oi, tudo bem?"

'''
Também é possível criar funções que retornam valores que são executados exclusivamente dentro da função através do 'return'

Confira o exemplo abaixo:
'''

def soma_dois_numeros():
    return 2 + 2

print(f'O resultado da soma de 2 + 2 é igual a: {soma_dois_numeros()}')

#A palavra reservada return sempre encerra a função, então tudo o que estiver dentro da função após o return, não sera executado

def teste():
    print('Essa mensagem está escrita antes do return')
    return 'Aqui foi executado o return'
    print('Essa mensagem está escrita depois do return')#Nesse exemplo, essa linha nunca sera executada

print(teste())

'''
Dentro de uma função, pode haver mais de 1 return, porém, dependendo de alguma condição apresentada será executado
somente 1 desses return, confira o exemplo:
'''

def teste_2():
    verdadeiro = True
    if verdadeiro == False:
        return 'É falso' #Como a condição do if não foi atendida, não executou esse return
    elif verdadeiro == True:
        return 'É verdadeiro' #Esse foi o return executado
    return 'Não é falso nem verdadeiro'

print(teste_2())

'''
Algumas funções podem ser usadas sem a necessidade de inserir dados para que elas sejam executadas, como visto nos 
exemplos anteriores.

Mas algumas funções, vão precisar de algum dado (parâmetro) para serem executadas, ou seja, ela precisa receber algum
dado para que ela possa retornar o que se espera da função, porque sem o dado de entrada, a função não é executada, 
mesmo sendo chamada.

Exemplo:
'''

def soma(num1, num2): #Aqui a função tem 2 parâmetros: num1 e num2, cada um vai receber um valor
    return num1 + num2 #O retorno dessa função vai ser a soma dos valores recebidos em num1 e num2

#Cada valor, é associado na sequência que a função vai receber os valores
resultado = soma(2, 4) #Aqui a função soma está sendo chamada e está enviando 2 valores(argumentos): 2 e 4
#      2->  num1,  4-> num2

print(resultado)#O resultado é o retorno da função, que é o resultado da soma de 2 + 4 = 6

'''
Aqui temos um exemplo um pouco mais complexo. Uma função com 3 parâmetetos, é uma calculadora que recebe vai receber
3 argumentos: uma opção de operação, e valor de cada número
'''

def calculadora(operacao, numero1, numero2): #Vai receber 3 argumentos: Opção escolhida, valor do 1° número e do 2° número
    if operacao == 1: #Se a operação escolhida pelo usuário for 1, executa essa parte do código, assim como o restante
        resultado = numero1 + numero2 #R
        return resultado #Retorna o resultado da operacao escolhida pelo usuário
    elif operacao == 2:
        resultado = numero1 - numero2
        return resultado
    elif operacao == 3:
        resultado = numero1 * numero2
        return resultado
    elif operacao == 4:
        resultado = float(numero1) / float(numero2)
        return resultado
    
print('### Calculadora ###')
controle = False
while controle == False: #Aqui foi criado um controle para caso o usuário digite um valor de opção diferente da lista
#Isso é importante para garantir que o 1° parâmetro esteja correto
    print('Digite o número da opção desejada: ')
    operacao = int(input('1 - Somar.  2 - Subtrair.  3 - Multiplicar.  4 - Dividir. \n'))
    if operacao >= 1 and operacao <= 4: #Se o valor estiver entre 1 e 4, sai do loop com o valor escolhido
        controle = True
    else:    
        print('Opção inválida! \n') #Qualquer número diferente de 1 e 4, é considerado uma opção inválida

numero1 = int(input('Digite o valor do 1° número: ')) #Recebe o 1° argumento 
numero2 = int(input('Digite o valor do 2° número: ')) #Recebe o 2° argumento
valor_final = calculadora(operacao, numero1, numero2) #Aqui a função é chamada e envia todos os argumentos coletados
print(f'O resultado da operação escolhida entre {numero1} e {numero2} é: {valor_final}')


