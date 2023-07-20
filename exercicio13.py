def fatorial():
    num = int(input('Informe um número: '))
    m = num
    for i in range(num-1, 0, -1):
        m = m * i
    print('O resultado é {}'.format(m))


