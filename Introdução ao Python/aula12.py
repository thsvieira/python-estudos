'''
While Loop, é usado para executar um bloco de instruções repetidamente até que uma determinada condição seja satisfeita.

Essa é a melhor opção dentro das estruturas de repetição quando não se sabe exatamente quando a condição vai ser atingida
para que a repetição seja encerrada.

No exemplo abaixo, vamos pedir para o usário digitar um número para somar quantas vezes ele quiser, até que ele peça para
o programa encerrar. Então dentro desse cenário, o usuário pode pedir para somar praticamente até o infinito, e o loop só
vai parar, quando ele não quiser mais continuar a soma.
'''
somar = True 
resultado = 0

while somar: #enquanto a variável somar for verdadeira, o laço vai se repetir indefinidamente
    soma = int(input('Digite um valor para somar ou digite 0(ZERO) para sair e ter o resultado da soma: '))
    resultado += soma
    if soma == 0: #Se o usuário digitar 0, a condição passa a ser FALSA e o programa se encerra.
        somar = False
print(f'O resultado da soma é: {resultado}')



