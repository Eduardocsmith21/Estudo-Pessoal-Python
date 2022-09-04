
from random import randint

from time import sleep

Computador = randint(0, 10)
print('Vou pensa em um numero entre 0 e 10 tenta adivinhar....')
jogador = int(input('Em que numero eu pensei: '))
print('PROCESSANDO...')
sleep(1)
if jogador == Computador:
    print('PARABENS VOCÊ CONSEGUIU ME VENCER!')
else:
    print('GANHEI! pensei no numero {} e não '
          ' {}'.format(Computador,jogador))


