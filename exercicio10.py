def media():
    soma = 0
    num = 1
    i = 0
    while(num != 0):
        num = int(input('Informe um número: '))
        if(num != 0):
            if(num % 2 == 0):
                soma += num
                i += 1
    return 'O resultado é {}'.format(soma/i)

