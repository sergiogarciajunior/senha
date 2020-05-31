import os
from random import randint
senha=list()
jogo=list()
def sorteio():
    global senha
    global jogo
    senha=list()
    lista=list()
    cont=0
    while True:
        num = randint(1, 6)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >=4:
            break
    senha.append(lista[:])
    lista.clear()
    print(senha)
    return senha


def jogar():
    global jogo
    global senha
    t=0
    while t<4:
        numero=int(input(f'Digite o {t+1}o. numero: '))
        if numero<1 or numero>6:
            numero=int(input('insira um numero entre 1 e 6: '))
        t=t+1
        jogo.append([numero])

    print(jogo)
    return jogo


def teste():
    global senha
    global jogo
    print(f'senha {senha} jogo {jogo}')
    pos=0
    for c in range(0, 4):
        if jogo[c] == senha[c]:
           pos=pos+1
    print(pos)
    num=0
    for i in range(0, 4):
        for l in range(0, 4):
            if jogo[i]==senha[l]:
                num+=1
                n=num-pos
    print(n)
    return pos, num

#senha=[' ', ' ', ' ', ' ', ' ', ' ']
senha=[[], [], [], [], [], []]


def tela():
    global senha
    global jogo
    os.system('cls')
    print('JOGADAS:.^30')
    print(' 0   1   2   3    num ok pos ok')
    for c in range(0,8):
        print(f'{senha[0]}. {senha[1]}. {senha[2]} {senha[3]} {senha[4]} {senha[5]}')

tela()

print(f' oi {senha} senha')
print(f'jogo {jogo}')


sorteio()
jogar()
teste()




