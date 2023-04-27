'''
Verificando items dentro de uma Lista - Uma forma simples de verificar se um item especifíco está dentro de uma lista, é utilizar estruturas de condição como If/Else 
em conjunto com "in" para constatar se o item está ou não contido na lista.

Vamos criar um programa que tenha as frutas que são vendidas em um mercado, e caso o usuário queira alguma fruta, digite o nome dela para adicionar no carrinho. Caso não tenha a fruta
desejada, retorne uma mensagem dizendo que está esgotada.

'''


comprar_fruta = input(f'Digite o nome da fruta que deseja comprar: ')

frutas = ['Acerola', 'Goiaba', 'Framboesa', 'Banana', 'Uva'] #Lista de frutas que estão disponíveis no mercado

if comprar_fruta.title() in frutas:   
#Ao usar a função .title garantimos que o programa vai reconhecer o item na lista conforme cadastrado (primeira letra maiúscula), independente da
#forma que o cliente digitar.
    print(f'Temos {comprar_fruta} em estoque. Adicionado ao carrinho.')
else:
    print(f'Não temos {comprar_fruta} em estoque. Produto esgotado.')
