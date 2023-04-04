'''
Nested Loops ou Laços Aninhados, é basicamente um loop dentro de outro interagindo entre si

O laço de "fora" é chamado de Outer Loop e o laço de "dentro" é chamado de Inner Loop

Vamos fazer um exemplo usando as tabuadas de 1 a 10
'''

for numero_da_tabuada in range(1, 11): #Esse for vai rodar primeiro
    print(f'Tabuada do {numero_da_tabuada}') #Aqui vai imprimir qual volta do laço o 1° for está (começando em 1)
    for numero_multiplicado in range(1, 11): #Esse laço  vai rodar 10x, à partir do 1
        print(f'{numero_da_tabuada} x {numero_multiplicado} =  {numero_da_tabuada * numero_multiplicado}') 
        ''' 
            Basicamente mostra a volta atual de cada laço pra construir a tabuada. O laço interno vai completar todas as voltas ANTES de retornar para o laço de fora,
            que vai executar a segunda volta, e então entra no laço interno que vai completar todas as voltas e assim por diante

            1° volta do laço de fora             1° volta do laço de dentro
                        1                  *               1                  =  1
            1° volta do laço de fora             2° volta do laço de dentro
                        1                  *               2                  =  2
            1° volta do laço de fora             3° volta do laço de dentro
                        1                  *               3                  =  3

                        ...

            2° volta do laço de fora             1° volta do laço de dentro
                        2                  *               1                 =  2
            2° volta do laço de fora             2° volta do laço de dentro
                        2                  *               2                 =  4 
            2° volta do laço de fora             3° volta do laço de dentro
                        2                  *               3                 =  6

                    E assim sucessivamente          
        ''' 