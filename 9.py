'''Fazer a divisão de dois valores por meio de subtrações sucessivas. Por exemplo, 32/4 = 8, pois é possível subtrair de 32 o valor 4 oito vezes'''

valor1 = int(input('Informe o dividendo: '))
valor2 = int(input('Informe o divisor: '))
subtracoes = 0

while valor1 >= valor2:
    valor1 = valor1 - valor2
    subtracoes += 1

print(valor1)
print(subtracoes)