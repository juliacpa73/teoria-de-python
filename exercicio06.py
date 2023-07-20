#6. Faça um algoritmo que escreva na tela os números de um número inicial a um número final.
#Os números inicial e final devem ser informados pelo usuário.
def inicialFinal(num1, num2):
    if (num1 < num2):
        for i in range(num1, num2+1):
             print(i)
    else:
        for i in range(num1, num2-1, -1):
            print(i)