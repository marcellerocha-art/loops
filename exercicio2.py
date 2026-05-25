# Exercício 2 - Soma até certo limite
# Você está jogando um jogo em que precisa somar os números inteiros sequencialmente até que a soma ultrapasse 20.
# Escreva um programa que calcule e exiba a soma desses números.

soma = 0
numero = 1

while soma <= 20:
    soma += numero
    numero += 1

print("A soma ultrapassou 20.")
print("Resultado:", soma)