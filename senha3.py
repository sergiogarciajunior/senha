import os
from random import randint
senha=list()
jogo=list()
ficha=list()
lista=list()
jogo1=list()

while True:
    senha.clear()
    jogo.clear()
    cont=0
    while True:
        num = randint(1, 6)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >=4:
            break
    senha.extend(lista[:])
    lista.clear()
    print(f' senha e {senha}')
    t=0
    while t<4:
        numero=int(input(f'Digite o {t+1}o. numero: '))
        if numero<1 or numero>6:
            numero=int(input('insira um numero entre 1 e 6: '))
        t=t+1
        jogo.append(numero)
#        jogo1.append(numero)
#        jogo.append(jogo1[:])
#         jogo1.clear()
    print(jogo)
    print(f'a senha e {senha} e o jogo e {jogo}')
    pos = 0
    for c in range(0, len(senha)):
        print(f'o jogo e {jogo[c]} e senha e {senha[c]}')
        if jogo[c] == senha[c]:
            pos = pos+1
    print(pos)
    num=0
    for i in range(0, len(senha)):
        for l in range(0, len(senha)):
            if jogo[i] == senha[l]:
                num = num+1
    print(num-pos)
    ficha.append([jogo, num-pos, pos])
    print(ficha)
    r=str(input('quer continuar (s/n): '))
    if r in 'Nn':
        break
print('foi legal voce jogar')



#def tela():
#    global senha
#   global jogo
#    os.system('cls')
#    print('JOGADAS:.^30')
#    print(' 0   1   2   3    num ok pos ok')
#    for c in range(0,8):
#        print(f'{senha[0]}. {senha[1]}. {senha[2]} {senha[3]} {senha[4]} {senha[5]}')
callable(senha)

