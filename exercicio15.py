def miss():
    num = -1
    candidata = ''
    vencedora = ''
    maior = 0

    for i in range(1,17):
        candidata = input('O nome da candidata {}: '.format(i))
        num = int(input('Informe um número: '))

        while((num < 0) or (num > 10)):
            num = int(input('Informe um número: '))
            print('Erro! Digite a nota entre 0 e 10')

        if (num > maior):
            maior = num
            vencedora = candidata
            print('A vencedora {} ganhou com {}!'.format(vencedora, maior))


