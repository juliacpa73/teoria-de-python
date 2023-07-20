def diferentesDeZero():
    maior = 0
    menor = 0
    num = 1
    flag = False
    while(num != 0):
        num = int(input('Informe um número: '))
        if(flag == False):
            maior = num
            menor = num
            flag = True
        if(num > maior):
            maior = num
        if(num < menor):
            menor = num
        flag += 1
    print('O maior número digitado foi {}, menor número digitado foi {}.'.format(maior, menor))
