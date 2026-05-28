'''Empresa irá dar aumentos somente para funcioários que não faltaram no último ano. Programa deve pedir o salário atual e o total de faltas. Situações:
- Salário de até R$1500, aumento de 200
- Salário entre R$1500.01 e R$3000, aumento de 100
- Salários acima de R$3000, 50 de aumento
- Mais de 5 faltas: Sem aumento'''

salario = float(input('Digite o salário atual: '))
faltas = int(input('Digite o número de faltas: '))

if salario < 1500.00:
    novo_salario = salario + 200
elif salario > 1500.01 and salario < 3000.00:
    novo_salario = salario + 100
elif salario > 3000.00:
    novo_salario = salario + 50

if faltas > 5:
    print('SEM DIREITO A AUMENTO')
else:
    print(f'O novo salário é: {novo_salario}')