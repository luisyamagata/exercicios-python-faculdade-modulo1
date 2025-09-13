# Conversor de temperatura

'''
1. Peça uma temperatura em graus celsius
2. Pergunte se o usuário deseja converter para F ou K
3. Use as fórmulas F = (C * 9/5)+ 32
                    K = C + 273.15
4. Mostre o resultado da conversão'''

celsius = float(input('Digite uma temperatura em Graus Celsius: '))
escolha = int(input('''Selecione uma unidade para converter essa temperatura:
                [0] Kelvin
                [1] Farenheit '''))
if escolha == 0:
    kelvin = float(celsius + 273.15)
    print(kelvin)
elif escolha == 1:
    farenheit = float((celsius * 9/5) + 32)
    print(farenheit)
