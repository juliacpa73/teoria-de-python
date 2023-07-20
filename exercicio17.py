def carro():
    carro = 1
    porcentagem = 0
    impostos = 0

    while (carro < 0):
        carro = int(input('Digite o valor'))
        print('Erro, digite novamente!')


    porcentagem = (porcentagem * 28/100)
    impostos = (carro * 45/100)

    return 'O valor do carro é: {}'.format(carro + porcentagem + impostos)