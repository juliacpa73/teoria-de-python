def eleitores():
    total = int(input('Informe o total: '))
    brancos = int(input('Informe a quantidade de votos brancos: '))
    nulos = int(input('Informe a quantidade de votos nulos: '))
    validos = int(input('Informe a quantidade de votos válidos: '))

    while (total < 0):
        total = int(input('Informe o total: '))
        print('Erro, digite novamente!')

    while (brancos < 0):
        brancos = int(input('Informe a quantidade de votos brancos: '))
        print('Erro, digite novamente!')

    while (nulos < 0):
        nulos = int(input('Informe a quantidade de votos nulos: '))
        print('Erro, digite novamente!')

    while (validos < 0):
        validos = int(input('Informe a quantidade de votos válidos: '))
        print('Erro, digite novamente!')

    if ((brancos + nulos + validos) > total):
        print('Erro, os votos ultrapassaram o total!')

    porcentagemBrancos = (brancos * 100) / total
    porcentagemNulos = (nulos * 100) / total
    porcentagemValidos = (validos * 100) / total

    print('A porcentagem dos votos brancos é {}, enquanto o resultado dos votos nulos é {} e válidos {}'.format(porcentagemBrancos, porcentagemNulos, porcentagemValidos))


