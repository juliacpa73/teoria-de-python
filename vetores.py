notas = [] #Verto Global = Todas as funções podem
            #Visualizar/Usar esse vetor

def preencherVetor(fim) :
    for i in range(fim):
        num = int(input('Informe a {} nota: '.format(i+1)))
        notas.append(num) #Adicionando notas no vetor

def consultarVetor(fim):
    for i in range(fim):
        print('{}ª Posição {}'.format(i+1, notas[i]))

def apagarPosicao(posicao):
    if (len(notas) < posicao):
        print('Impssível remover, pois o tamanho é menor do que a posição.')
    else:
        del(notas[posicao]) #Excluindo um dado do vetor
        print('Removido com sucesso!')
