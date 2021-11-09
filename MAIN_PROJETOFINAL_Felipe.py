from PROJETOFINAL_Felipe import *

def jogar():
    mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #matriz inicial para formar a grid 4x4 apenas com zeros.
    numeros = [2,4] #numeros que irão ser sorteados e colocados dentro da grid para continuar a soma.
    condicao_vito = 2048 #O Jogo irá ser encerrado quando este numero for atingido. Altere-o para valores menores como 16 se quiser realizar algum teste rápido.

    print('Olá e boas vindas ao jogo 2048 :), use as teclas WASD para mover os numeros. Boa sorte!')
    print('Se Desejar sair do jogo, digite "sair", se preferir recomeçar, digite "recomeçar". ')
    print()

    num = choices(numeros, weights=[10, 1])
    num = int(num[0]) #Variável que recebe os numeros que irão ser encaixados dentro da grid aleatóriamente.
    pos_vazia = posicaoVazia(mat)
    mat[pos_vazia[0]][pos_vazia[1]] = num #Adiciona um numero a uma posição aleatória do grid.

    matrizMat(mat)

    joga = 1
    while joga == 1:

        mat2 = mat.copy() #Matriz criada para comparar posteriormente com a matriz original.

        num = choices(numeros, weights=[10, 1])
        num = int(num[0]) #Variável que recebe os numeros que irão ser encaixados dentro da grid aleatóriamente.

        dire = input('>>> ') #Corpo onde é recebido o comando de em qual direção os numeros serão jogados e somados.
        if dire == 'w':
            mat = rearranjar_Matriz_cima(mat)
        elif dire == 'a':
            mat = rearranjar_Matriz_esq(mat)
        elif dire == 's':
            mat = rearranjar_Matriz_baixo(mat)
        elif dire == 'd':
            mat = rearranjar_Matriz_dir(mat)

        elif dire == 'sair': #Corpo onde é recebido os comando de sair ou recomeçar o jogo.
            break
        elif dire == 'recomeçar':
             return jogar()

        else:
            print('por favor dê um comando válido.')
            continue

        for linhas in mat: #Verifica se o jogador atingiu a condição de vitória e se deseja continuar jogando.
            for colunas in linhas:
                if colunas == condicao_vito:
                    matrizMat(mat)
                    resposta = input('Parabéns, você formou o {} e ganhou! :D Desenha continuar jogando? (sim/nao) '.format(condicao_vito) )
                    if resposta == 'sim':
                        condicao_vito = condicao_vito * 2
                        continue
                    else:
                        return print('Obrigado por jogar :)')

        #Verifica se a grid esta totalmente preenchida e se ainda existe movimentos possíveis.
        if posicaoVazia(mat) == (111,111) and (not movimento_possivel_horizontal(mat)) and (not movimento_possivel_vertical(mat)):
            resposta = input('Você perdeu :( Deseja Recomeçar o jogo? (Sim/Não) ')
            if resposta == 'sim':
                return jogar()
            return print('jogo finalizado.')

        pos_vazia = posicaoVazia(mat)
        if mat2 != mat: #Caso a matriz tenha se alterado com algum movimento de rearranjo, adiciona um numero a uma posição do grid.
            try:
                mat[pos_vazia[0]][pos_vazia[1]] = num
            except:
                continue

        matrizMat(mat)
        print()
    return print('jogo finalizado.')

if __name__ == '__main__':
    jogar()



