def volei():
    media = 0
    soma = 0
    num1 = int(input('Informe a quantidade de jogadores: '))
    for i in range(1, num1 + 1):
        num2 = float(input('Informe a altura de cada um: '))
        soma += num2
        media = soma/i
    print('O resultado é {}'.format(media))

