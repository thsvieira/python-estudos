'''
Aqui iremos ver como utilizar If e Else dentro de um Loop

Vamos pegar como exemplo uma loja online que após a confirmação da compra, retorna que a compra foi efetuada com sucesso e que os dados foram enviados no e-mail

Serão realizadas 3 tentativas de compra, se não conseguir, é enviado uma mensagem informando que a compra não foi efetuada
'''

compra_confirmada = True #Nesse cenário, estamos considerando que a compra foi concluída com sucesso
dados_compra = 'Compra efetuada no valor de R$12.50 e entrega confirmada.'

for enviar in range(3): #Nessa parte do código, a compra vai tentar ser concluída em no máximo 3 tentativas.
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes da compra enviados para o seu e-mail.')
        break #O break é usado para interromper o loop caso a condição seja alcançada(compra_confirmada = true) antes de rodar a próxima iteração
else:
    print('Falha no pagamento. Compra não efetuada.')