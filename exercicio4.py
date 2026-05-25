# Exercício 4: Tabuada
# Você é um estudante tentando aprender a tabuada. 
# Escreva um programa que peça um número ao usuário e, em seguida, exiba a tabuada desse número, de 1 a 10.

numero = int(input("Digite um número: "))

i = 1

while i <= 10:
    print(numero, "x", i, "=", numero * i)
    
    i += 1