#7. Escreva um algoritmo que gera e escreva os números ímpares entre 100 e 200
def impar():
    num1 = 100
    num2 = 200
    for i in range(num1, num2+1):
       if(i % 2 == 1):
            print(i)