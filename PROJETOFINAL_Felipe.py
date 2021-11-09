#FELIPE SERGIO DE SOUZA MARTINS
#DRE:120068354

# PARTE I #

from random import *

def matrizMat(matriz):
    '''Função que de entrada recebe uma matriz, escrita na sintaxe do python, e
    escreve na tela do usuário (no shell) a mesma matriz, porém em forma matemática.
    retorna None.
    list -> None'''
    for linhas in matriz:
        for colunas in linhas:
            print(colunas, end=' ')
        print()
    return None

def posicaoVazia(matriz):
    '''Função que recebe de entrada uma matriz, e retorna aleatóriamente uma posição vazia
    nesta mesma matriz. Se a matriz estiver totalmente preenchida, retorna uma posição inexistente (111,111)
    list -> tuple'''
    posicoes = []
    for linhas in range(len(matriz)):
        for colunas in range(len(matriz[linhas])):
            if matriz[linhas][colunas] == 0 :
                posicoes.append((linhas,colunas))
    if posicoes == []:
        return (111,111)
    return posicoes[randint(0, len(posicoes) - 1)]

def soma(matriz):
    '''Função que recebe de entrada uma matriz qualquer e realiza a soma entre dois elementos
     de cada umas das linhas dessa matriz, se os mesmos forem iguais. Após a soma, a linha é atualizada,
       não contendo mais os numeros iguals, e sim a soma entre eles e um 0.
       list -> list'''
    auxiliar = 0
    for linhas in range(4):
        for colunas in range(0,4):
            if colunas < 3 and auxiliar == 0:
                if matriz[linhas][colunas] == matriz[linhas][colunas + 1]:
                    auxiliar = 1
                    matriz[linhas][colunas + 1] = matriz[linhas][colunas] * 2
                    matriz[linhas][colunas] = 0
            else:
                auxiliar = 0
    return matriz

# PARTE II #

def girar_matriz(matriz):
    '''Gira uma matriz em 90 graus a esquerda. Tornando cada linha em uma coluna e vise-versa.
     list -> list'''
    matriz_girada = [[],[],[],[]]
    for linhas in matriz:
        matriz_girada[0].append(linhas[-1])
        matriz_girada[1].append(linhas[-2])
        matriz_girada[2].append(linhas[-3])
        matriz_girada[3].append(linhas[-4])
    return matriz_girada

def mov(matriz):
    for linhas in matriz:
        posicao = 4
        for index in range(4,0,-1):
            index = index -1
            if linhas[index] != 0:
                linhas.insert(posicao,linhas[index])
                linhas.pop(index)
                posicao += -1
    return matriz

def rearranjar(matriz):
    ''' Função que joga todos os elementos para a direita da matriz, alterando a matriz fornecida.
    list -> list'''

    matriz = mov(matriz)
    matriz = soma(matriz)
    matriz = mov(matriz)

    return matriz

def rearranjar_Matriz_dir(matriz):
    '''Função que joga todos os elementos da matriz para a direita, porém não altera a matriz original.
     list -> list'''
    matriz = girar_matriz(girar_matriz(girar_matriz(girar_matriz(matriz))))
    matriz = rearranjar(matriz)
    return matriz

def rearranjar_Matriz_baixo(matriz):
    '''Joga todos os elementos de uma matriz para baixo, somando elementos que estão adjacentes e
        são iguais.
        list -> list'''
    matriz = girar_matriz(matriz)
    matriz = rearranjar(matriz)
    matriz = girar_matriz(girar_matriz(girar_matriz(matriz)))
    return matriz

def rearranjar_Matriz_esq(matriz):
    '''Joga todos os elementos de uma matriz para seu lado esquerdo, somando elementos que estão adjacentes e
        são iguais.
        list -> list'''
    matriz = girar_matriz(girar_matriz(matriz))
    matriz = rearranjar(matriz)
    matriz = girar_matriz(girar_matriz(matriz))
    return matriz

def rearranjar_Matriz_cima(matriz):
    '''Joga todos os elementos de uma matriz para cima, somando elementos que estão adjacentes e
        são iguais.
        list -> list'''
    matriz = girar_matriz(girar_matriz(girar_matriz(matriz)))
    matriz = rearranjar(matriz)
    matriz = girar_matriz(matriz)
    return matriz

def movimento_possivel_horizontal(matriz):
    '''Checa se ainda existe um movimento para a horizontal dentro do grid.
    list -> boolean'''
    for linhas in range(4):
        for colunas in range(3):
            if matriz[linhas][colunas] == matriz[linhas][colunas+1]:
                return True
    return False

def movimento_possivel_vertical(matriz):
    '''Checa se ainda existe um movimento para a vertical dentro do grid.
    list -> boolean'''
    for linhas in range(3):
        for colunas in range(4):
            if matriz[linhas][colunas] == matriz[linhas+1][colunas]:
                return True
    return False


