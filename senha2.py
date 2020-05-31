senha=[1, 4, 3, 5]
jogo=[1, 2, 6, 5]
pos=0
for c in range(0,4):
    if jogo[c] == senha[c]:
        print(f'o{c} {jogo[c]}')
        pos=pos+1
print(f' a pos {pos}')







