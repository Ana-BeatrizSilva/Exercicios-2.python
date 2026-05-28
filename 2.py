'''Leia as três notas do estudante e calcule sua média. Peça também a porcentagem de presença. Situações:
- Aprovado: Média 70 e presença acima de 75%
- Prova final: Média entre 40 e 69 e presença acima de 75%
- Reprovado por falta: Presença abaixo de 75% (independente da nota)
- Reprovado por nota: Média abaixo de 40'''

soma = 0

for i in range (3):
    nota = int(input('Digite sua nota: '))
    soma += nota

media = soma/3
print(f'A média foi: {media}')

presenca = int(input('Informe a presença: '))

if media >= 70 and presenca > 75:
    print('APROVADO!')    
elif 40 <= media <= 69 and presenca > 75:
    print('PROVA FINAL')
elif presenca < 75:
    print('REPROVADO POR FALTA')
elif media < 40:
    print('REPROVADO POR NOTA')