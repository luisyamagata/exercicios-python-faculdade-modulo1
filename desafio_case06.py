print('-='*40)
print('Calculadora de IMC Boladona')
print('-='*40)
'''O Índice de Massa Corporal IMC é calculado pela fórmula:
IMC=peso/altura^2
IMC  \frac{peso}{altura^2
IMC=altura2peso'''

#TODO Peça ao usuário seu peso (kg) e altura (m)
#TODO Calcule o IMC, dado que o IMC equivale ao peso, em kg, dividido pelo quadrado da altura (em metros) 
peso = float(input('Quantos kg você pesa? '))
altura = float(input('Qual é a sua altura em metros? '))
print(f'Seu peso é {peso}')
print(f'Sua altura é {altura:.2f}')
altura_quadrado = float(altura ** 2)
print(altura_quadrado)
imc = float(peso/altura_quadrado)
print(f'Seu IMC é de {imc:.2f}')
if imc < 18.5:
    print('Seu IMC é inferior a 18.5. Portanto, você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Pelo seu IMC, seu peso está Normal.')
elif imc >= 25 and imc < 30:
    print('Você está com Sobrepeso')
else:
    print('Pelo seu IMC, você está com Obesidade 🫃')
