'''Um número é perfeito se a soma de todos os seus divisores (excluindo ele mesmo) for igual ao próprio número. Escreva um programa que receba um número e verifique se ele é perfeito. Exemplo: 6 é perfeito ( 1 + 2 + 3 = 6)'''

num = int(input('Digite um número: '))
soma = 0
for i in range(1,num):
    if num % i == 0:
        soma += i

if soma == num:
    print('Número perfeito')
else:
    print('Não é perfeito')

