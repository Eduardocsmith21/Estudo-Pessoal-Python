numero_digitado = int(input("Digite um número para saber a tabuada: "))
for contador in range(0, 11):
    print("{} X {} = {}".format(numero_digitado, contador, numero_digitado*contador))
    