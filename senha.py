import os
from random import randint
#senha=[' ', ' ', ' ', ' ', ' ', ' ']
senha=[[], [], [], [], [], []]


def tela():
    os.system('cls')
    print('JOGADAS:.^30')
    print(' 0   1   2   3    num ok pos ok')
    for c in range(0,8):
        print(f'{senha[0]}. {senha[1]}. {senha[2]} {senha[3]} {senha[4]} {senha[5]}')


def jogar():
    for l in range(0,9):
        for c in range(0,4):
            senha[l][c]=int(input(f'Digite o {l+1}o. numero: '))
    print('-'*30)
    for l in range(0,9):
        for c in range(0,4):
            print(f'[{senha[l][c]}]', end='')





#tela()
jogar()









