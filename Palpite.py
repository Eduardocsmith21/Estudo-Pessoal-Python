from random import randint
pc = randint(0,10)
print('Sou seu computador...Acabei de pensar em um numero entre 0 e 10')
print('Aerá que vocçê consege adivinha?')
ac = False
pal = 0
while not ac:
    jo = int(input('Qual é seu palpite: '))
    pal += 1
    if jo == pc:
        ac = True
    else:
        if jo < pc:
            print('MAIS...tente novamente')
        elif jo > pc:
            print('MENOS...tente novamente')
print('ACERTOU!')
print('Você precisou de {} palpites para acertar'.format(pal))

