'''Sabe-se que cada endereço de rede possui oito números zero ou uns em sequência, que formam o número binário. Solicite ao usuário 8 zeros ou uns para formar o número  binário (lendo dígito a dígito, um de cada vez). O programa deve percorrer os dígitos e calcular o seu valor correspondente na base 10, em decimal. 
- Multiplicar cada bit por 2 elevado a posição e somar os resultados. Considere que os números são informados de trás pra frente'''

soma = 0

for i in range(8):
    bit = int(input('Informe o bit: '))
    if bit != 1 and bit != 0:
        print('INVÁLIDO')
        break
    resultado = bit * (2**i)
    print(f'\n{resultado}')
    soma += resultado

print(f'\nA soma é: {soma}')