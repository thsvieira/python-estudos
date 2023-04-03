
#Aqui aprenderemos sobre o uso das condições if, else e elif em Python

velocidade = 40 #Essa é a velocidade atual

if velocidade > 110: #Se a velocidade for maior do que 110, imprima os seguintes textos 
    print('Acima da velocidade Permitida!')
    print('Favor reduzir a sua velocidade.')
elif velocidade < 60: #Essa é uma mistura de if + else. Se a primeira condição não for atendida, o código pula para essa condição que é a próxima a ser verificada
    print('Velocidade muito abaixo do limite. Favor dirigir acima de 80KM/h')
else: #Se não estiver acima de 110 (velocidade atual é 100) e também não estiver abaixo de 60(nenhuma das condições foram atendidas), imprima o texto abaixo
    print('Velocidade OK')

'''
if e else são 2 operadores usados para verificar uma condição

if verifica uma determinada condição e executa uma determinada ação, 

Se essa ação não atender a condição determinada, executa a ação contida dentro de else

Porém, existe a condição elif, que é basicamente uma junção de else + if

Dentro da sequência lógica, se a 1° condição não for atendida (if), passa para a próximma(elif), e verifica quantas forem pré-determinadas. 

Se nenhuma condição for atendida, executa o que estiver dentro de else

'''
