'''
Trabalhando com SETs - Um SET (Conjunto) em Python, é um agrupamento de valores únicos de forma não ordenada, ou seja,
não tem um índice associado como estamos acostumado com listas. Os SETs são reconcidos pelas chaves {}, e a vantagem de se
trabalhar com eles é que não possuem itens duplicados, cada elemento é unico.

Após criar um SET, você não pode alterar os valores, mas pode remover valores ou adiconar novos.

SET é bastante interessante em alguns casos, como por exemplo, eliminar dados duplicados de listas. Podemos fazer
isso transformando as listas em SETs

Vejamos alguns exemplos:
'''

lista1 = [1, 1, 2, 4, 7, 9, 9, 12]
lista2 = [1, 2, 3, 4, 4, 6, 9, 10]
#Entre as 2 listas, os números que se repetem são: 1, 2, 4 e 9

#Podemos transformar essas listas em SETS da seguinte forma:
set1 = set(lista1)
set2 = set(lista2)
#Criamos duas novas variáveis que vão receber o conteúdo das listas transformados em SETs
print(set1)
print(set2)

#Também podemos transformar de forma direta como no exeplo abaixo:
lista3 = set([0, 2, 2, 4, 5, 5, 6])
print(type(lista3)) #<class 'set'>
print(lista3) #{0, 2, 4, 5, 6} Set criado sem os valores repetidos da lista3

#Ou simplesmente criar um SET de forma direta:
set3 = {1, 2, 3, 4, 5}

'''
Ao imprimir a lista1 e lista2 convertidas em sets, tivemos esses resultados:

{1, 2, 4, 7, 9, 12}
{1, 2, 3, 4, 6, 9, 10}

Repare que todos os números que estavam duplicados, foram desconsiderados ao criar o SET

Isso também é útil quando queremos juntar 2  listas eliminando itens duplicados

Para isso, usamos alguns operadores básicos:

Union -> Junta 2 listas retirando os números repetidos, representado por |
Difference -> Retorna os valores da primeira sem os dados duplicados comparados com a 2° lista, representado por -
Simmetric Difference -> Retorna o valor das 2 listas mostrando apenas os valores únicos, representado por ^
And -> Mostra somente o que está duplicado entre as 2 listas, representado por &
'''
#set1 = {1, 2, 4, 7, 9, 12}
#set2 = {1, 2, 3, 4, 6, 9, 10}
print(set1 | set2) #Union -> {1, 2, 3, 4, 6, 7, 9, 10, 12}
print(set1 - set2) #Difference -> {12, 7}
print(set1 ^ set2) #Symmetric Difference -> {3, 6, 7, 10, 12}
print(set1 & set2) #And -> {1, 2, 4, 9}

#Depois que os SETs já estão criados, podemos usar a função .add() para adicionar um novo elemento:

#set1 = {1, 2, 4, 7, 9, 12}
set1.add(3) #Vamos adicionar o valor 3 no set1
print(set1) #resultado {1, 2, ->3<-, 4, 7, 9, 12}

#É possível também adicionar mais de um item simultaneamente através da função .update([]):

#set2 = {1, 2, 3, 4, 6, 9, 10}
set2.update([5, 7, 8]) #Vamos adicionar os valores 5, 7 e 8 no set2
print(set2) #resultado {1, 2, 3, 4, ->5<-, 6, ->7<-, ->8<- 9, 10}

#Uma outra função disponível, é remover itens usando o .remove()

#set1 = {1, 2, 3, 4, 7, 9, 12}
set1.remove(12)
print(set1) #resultado {1, 2, 3, 4, 7, 9}

