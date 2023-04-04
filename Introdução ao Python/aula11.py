'''
Continuando com a interação de laços aninhados(nested loops), aqui veremos um exemplo bastante útil trabalhando com STRINGS

O objetivo vai ser imprimir uma palavra espaçada, seguindo esse padrão:

MARAVILHOSO -> M A R A V I L H O S O
'''

palavra = 'EU GOSTO DE COMIDA CASEIRA!!'

for espaco in palavra: 
    print(f' {espaco}', end='') 
'''
Essa funcionalidade end='' vai ser usada para que o laço não pule uma linha ao dar uma volta.

Ao identificar um espaço em branco, ele encerra o laço e começa na mesma linha

Repare que á um pequeno espaço dentro da string formatada, 

Ele está sendo considerando toda vez que imprime o próximo caracter, o que cria a string impressa com espaços
'''