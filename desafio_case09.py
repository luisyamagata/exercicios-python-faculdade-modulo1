# JOGO DA IDADE

''' 1. Pergunte a idade do usuário
 2. Se a idade for < 12: "Você é uma criança"
 3. Se estiver entre 12 e 17, mostre: "Você é adolescente".
 4. Se estiver entre 18 e 59, mostre: "Você é adulto".
 5. Se for 60 ou mais, mostre: "Você é idoso'''

idade = int(input('Qual é a sua idade? '))
if idade < 12:
    print('Você é uma criança')
elif idade > 12 and idade <= 17:
    print('Você é adolescente')
elif idade >= 18 and idade <= 59:
    print('Você é adulto')
elif idade > 60:
    print('Você é idoso.')
