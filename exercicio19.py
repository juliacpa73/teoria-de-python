elemento = []

def vetor():
    maior = 0
    menor = 0

    for i in range(5):
        num = int(input('Informe a {} nota: '.format(i+1)))
        elemento.append(num)

    if (flag == False ):
        maior = num
        menor = num
        flag = True

    if (num > maior):
        maior = num

    if (num > menor):
        menor = num


def consultarVetor(5):
    for i in range(5):
        print('O maior número digitado foi {}.'.format(i + 1, maior, elemento[i]))