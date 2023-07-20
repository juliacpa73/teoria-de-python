from exercicio04 import somarInteiro
from exercicio05 import tabuada
from exercicio05 import coletarPositivo
from exercicio06 import inicialFinal
from exercicio07 import impar
from exercicio08 import dezNumeros
from exercicio09 import somarNumeros
from exercicio10 import media
from exercicio11 import diferentesDeZero
from exercicio12 import exibirValores
from exercicio13 import fatorial
from exercicio14 import volei
from exercicio15 import miss
from vetores import preencherVetor
from vetores import consultarVetor
from vetores import apagarPosicao
from exercicio16 import eleitores
from exercicio17 import carro
from exercicio18 import calendario


def mostrarMenu():
    print('Escolha uma das opções abaixo' + '\n0. SAIR' +
          '\n1. Exercício 04' +
          '\n2. Exercício 05' +
          '\n3. Exercício 06' +
          '\n4. Exercício 07' +
          '\n5. Exercício 08' +
          '\n6. Exercício 09' +
          '\n6. Exercício 10' +
          '\n7. Exercício 11' +
          '\n8. Exercício 12' +
          '\n9. Exercício 13' +
          '\n10. Exercício 14' +
          '\n11. Exercício 15' +
          '\n12. Exercício 16' +
          '\n13. Exercício 17' +
          '\n14. Exercício 18' +
          '\n15. Exercício 19' +
          '\n16. Exercício 20' +
          '\n17. Preencher Vetor' +
          '\n18. Consultar Vetor' +
          '\n19. Apagar posição Vetor')

def operacao():
    #Chamar o método de cima
    opcao = 1
    while(opcao != 0):
        mostrarMenu()
        #Coletar a opção do usuário
        opcao = int(input('Digite aqui o número da opção escolhida: '))
        #Executo a ação
        if(opcao == 0):
            return "Obrigado!"
        elif(opcao == 1):
            print(somarInteiro())
        elif(opcao == 2):
            num = int(input('Informe um número: '))
            n = coletarPositivo()
            tabuada(num, n)
        elif(opcao == 3):
            num1 = int(input('Informe um número: '))
            num2 = int(input('Informe o fim: '))
            inicialFinal(num1, num2)
        elif(opcao == 4):
            impar()
        elif(opcao == 5):
            print(dezNumeros())
        elif(opcao == 6):
            print(somarNumeros(num))
        elif(opcao == 7):
            print(media())
        elif(opcao == 8):
            print(diferentesDeZero())
        elif(opcao == 9):
            print(exibirValores())
        elif(opcao == 10):
            print(fatorial)
        elif(opcao == 11):
            print(fatorial())
        elif(opcao == 12):
            print(volei())
        elif (opcao == 13):
            print(miss())
        elif (opcao == 14):
            print(eleitores())
        elif (opcao == 15):
            print(carro())
        elif (opcao == 16):
            print(calendario())
        elif (opcao == 17):
            num = int(input('Inforem o tamanho do vetor: '))
            preencherVetor(num)
        elif (opcao == 18):
            num = int(input('Informe o tamanho do vetor: '))
            consultarVetor(num)
        elif (opcao == 19):
            posicao = int(input('Informe a posição que deseja apagar: '))
            apagarPosicao(posicao -1)
        else:
            return 'Opção escolhida não válida, escolha novamente!'
    return

