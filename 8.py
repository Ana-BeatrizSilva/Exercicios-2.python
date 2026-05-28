'''Algoritmo que lê a idade de várias pessoas. O laço deve ser interrompido quando o usuário digitar 0. Ao final, mostrar:
- A média das idades digitadas
- Quantas pessoas são maiores de idade (18)'''

contMaiores = 0
soma = 0
cont = 0

while True:
    idade = int(input('Digite sua idade: '))
    if idade == 0:
        break
    else:
        soma += idade
        cont += 1
        if idade >= 18:
            contMaiores += 1

media = soma/cont
print(f'Média das idades: {media}')
print(f'Total de maiores de idade: {contMaiores}')