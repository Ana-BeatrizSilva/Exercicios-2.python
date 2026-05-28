'''Algoritmo que leia as médias de estudantes. O laço deve ser interrompido quando o usuário digitar -1. Ao final, deve exibir:
- A soma de todas as médias
- Quantos estudantes ficaram acima da média (70)'''

soma = 0
acimaMedia = 0

while True:
    media = float(input('Digite sua média: '))
    if media == -1:
        break
    soma += media
    if media > 70:
        acimaMedia += 1

print(f'Soma das médias: {soma}')
print(f'Quantos estudantas ficaram acima da média?: {acimaMedia}')
