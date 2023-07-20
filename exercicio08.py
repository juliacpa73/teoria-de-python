def dezNumeros():
    soma = 0
    for i in range(1,11):
        num = int(input("Informe {}º ".format(i)))
        soma += num
    return  'A soma dos elementos digitados é {}'.format(soma)


