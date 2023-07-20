def exibirValores():
    num = 0
    s = 0
    c = 0
    for i in range(1, 21):
        num = int(input('Informe um número: '))
        if(num > 0):
            s += num
        if(num < 0):
            c += 1
    print('A soma dos positivos é: {} e a soma dos negativos é: {}'.format(s,c))


