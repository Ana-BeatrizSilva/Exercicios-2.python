'''Pedir idade de uma pessoa e verificar se ela é criança (menor de 12 anos), adolescente (maior que 12 e menor que 18), adulto (igual ou maior que 18), e idoso (60 e mais):'''

idade = int(input('Digite a idade: '))
if idade < 12:
    print('CRIANÇA')
elif idade >= 12 and idade < 18:
    print('ADOLESCENTE')
elif idade > 18:
    print('ADULTO')
elif idade > 60:
    print('IDOSO')