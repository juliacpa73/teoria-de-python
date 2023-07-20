def calendario():

    anos = int(input('Digite o ano: '))
    while (anos < 0):
        anos = int(input('Digite o ano: '))
        print('Data errada!')

    meses = int(input('Digite o mês: '))
    while (meses < 0):
        meses = int(input('Digite o mês: '))
        print('Data errada!')

    dias = int(input('Digite os dias: '))
    while (dias < 0):
        dias = int(input('Digite os dias: '))
        print('Data errada!')

    meses2 = meses * 30
    anos2 = anos * 365

    resultado = meses2 + anos2
    print('A quantidade de dias são {}'.format(resultado))





