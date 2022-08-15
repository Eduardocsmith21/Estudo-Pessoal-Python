n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print(""""    [ 1 ] Somar
     [ 2 ] Multiplicar
     [ 3 ] Maior
     [ 4 ] Novos números
     [ 5 ] Sair""")
    opção = int(input('Qual sua opção: '))
    if opção == 1:
        s = n1 + n2
        print('A soma de {} e {} da {}'.format(n1,n2,s))
    elif opção == 2:
        s  = n1 * n2
        print('A multiplicação de {} X {} tem o resultado de {}'.format(n1,n2,s))
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print("Entre {} e {} o número maior é {}".format(n1,n2,maior))
        else:
            maior = n2
            print('entre {} e {} o maior é {}'.format(n1,n2,maior))
    elif opção == 4:
        print('informe os valores novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Fim do programa. volte sempre!')
    else:
        print('Opção invalida.Tente novamente.')
    print('=-='*10)
print('Fim do programa!')

