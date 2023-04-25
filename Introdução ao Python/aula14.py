'''
Manipulando Listas - Podemos manipular listas de diversas formas, desde trocar um item da lista, removelo, mostras somente
1 item da lista... 

Vamos à alguns exemplos:
'''
#Toda item em uma lista, é anexado à um índice
calcados = ['Sapato', 'Chinelo', 'Botina', 'Galocha', 'Sandália', 'Coturno']
#  index ->     0         1          2        3           4           5
#Podemos pedir para imprimir somente um determinado item da lista pelo índice dele, por exemplo:
print(calcados[1]) #Aqui será impresso somente o item na posição 1 (Chinelo) ao colocar o índice dentro de [] na função print
#Também podemos trocar um item da lista escolhendo o lugar onde ele vai entrar pelo índice
calcados[0] = 'Tamanco' #Na posição 0 temos 'Sapato', porém será substituído por 'Tamanco'
print(calcados)

'''
Podemos manipular listas também usando funções específicas, listando algumas delas:

nome_da_lista.append(item_x) -> Essa função adiciona um item no fim da lista
nome_da_lista.pop(índice) -> Remove um item da lista pelo índice. Se o valor estiver vazio [], remove o último item da lista
nome_da_lista.remove(item_x) -> Remove o primeiro item da lista cujo "valor" seja igual ao especificado
nome_da_lista.insert(posição_x, item_x) -> Insere um item específico na posição desejada
nome_da_lista.sort() -> Organiza os itens na lista por ordem alfabética
nome_da_lista.reverse() -> Inverte a posição dos itens na lista
nome_da_lista.count(item_x) -> Retorna a quantidade de vezes que um item aparece em uma lista
nome_da_lista.clear() -> Remove todos os itens da lista

'''

calcados.append('Rasteirinha') #Vai adicionar o item 'Rasteirinha" no fim da lista calcados
print(calcados)
calcados.pop(0)#Remove o item na posição 0 do index
print(calcados)
calcados.remove('Galocha') #Se tiver um item chamado Galocha na lista, vai ser removido
print(calcados)
calcados.insert(3, 'Galocha')#Vai inserir o item Galocha na posição 3 do index
print(calcados)
calcados.sort()#Organiza os itens em ordem alfabética. Estava nessa ordem ['Chinelo', 'Botina', 'Sandália', 'Galocha', 'Coturno', 'Rasteirinha']
#passou a ser ['Botina', 'Chinelo', 'Coturno', 'Galocha', 'Rasteirinha', 'Sandália']
print(calcados)
calcados.reverse()
print(calcados)
print(calcados.count('Sandália'))#Retorna quantas vezes o item Sandália aparece na lista
calcados.clear()#Remove todos os itens da lista, retornando uma lista vazia []
print(calcados)







