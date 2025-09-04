'''Crie um programa que calcule o valor do frete com base na distância:
Até 5km, R$5
De 6km até 10Km, R$10
Acima de 10km, exibir que a entrega não é feita.'''

dist = int(input('Digite a distância, em KM da sua casa até a Pizzaria Sabores: '))

if dist <= 5:
    frete = 5
    print(f"O valor do seu frete é de R${frete}.00")
elif dist > 5 and dist <= 10:
    frete = 10
    print(f"O valor do seu frete é de R${frete}.00")
else:
    print('Sinto muito. Não realizamos entregas para casas com distância superior a 10 KM.')

