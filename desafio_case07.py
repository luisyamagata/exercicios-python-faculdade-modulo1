#CASE 7 - LOJA DE ROUPAS
# Uma loja vende camisas por R$ 50,00 cada
#1. Pergunte quantas camisas o cliente quer comprar
#2. Se comprar 3 ou mais camisetas, ele ganha 20% de desconto
#3. Mostre o valor final da compra

desconto = 0
qt_camisas = int(input('Cada camisa custa R$ 50.00. Quantas camisas deseja comprar? '))
conta = qt_camisas * 50

if qt_camisas >= 3:
    desconto = 0.20
    conta_desc = conta - (conta * desconto)
    print(f'O valor final da compra é de R$ {conta_desc:.2f}')
else:
    desconto = 0
    print(f'O valor final da compra é de R$ {conta:.2f}')
