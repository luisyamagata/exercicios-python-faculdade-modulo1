'''Case 3 – Posto de Gasolina ⛽
O posto “Abastece Bem” tem a seguinte tabela:
Gasolina: R$ 5.5/L
Etanol: R$ 4.00/L
Regras:
1. Pergunte ao cliente qual combustível deseja (Gasolina ou Etanol).
2. Pergunte quantos litros deseja abastecer.
3. Calcule e mostre o valor a pagar.
4. Se o cliente abastecer mais de 20 litros de etanol, ele ganha 5% de desconto.'''

#TODO Perguntar ao usuário o combustível desejado ok
#TODO Input da quantidade de litros
#TODO Calculo do valor a pagar OK
#TODO Exibição do valor a pagar OK
#TODO SE o cliente abastecer + de 20 L de etanol => aplicar desconto de 5%

print('-'*40)
print('Bem-Vindo ao posto ABASTECE BEM')
print('-'*40)
print('''Gasolina: R$ 5.50/L
Etanol: R$ 4.00/L''')
sabor = int(input('Qual combustível deseja? Digite 0 para Gasolina, 1 para Etanol '))
conta = 0
if sabor == 0:
    print('Você selecionou Gasolina.')
    qt_comb = int(input('Cada litro de Gasolina custa R$ 5.50. Digite a quantidade de Litros que deseja: '))
    #print(qt_comb)
    conta = float(qt_comb * 5.50)
    print(f'Você deve pagar R$ {conta:.2f}')
elif sabor == 1:
    print('Você selecionou Etanol')
    qt_comb = int(input('Cada litro de Etanol custa R$ 4.00. Digite a quantidade de Litros que deseja: '))
    if qt_comb > 20:
        desconto_bool = True
        print('Por abastecer mais de 20 L de etanol. Você ativou nossa promoção e ganhou 5% de desconto sobre o valor desse combustível.')
    conta = float(qt_comb * 4)
    if desconto_bool == True:
        desconto = 0.05
        print(f'O valor a pagar, antes do desconto é de {conta:.2f}')
        conta = conta - (conta * desconto)
        print(f'O valor a pagar, com o desconto de 5% é de R$ {conta:.2f}')
    
    print(f'Você deve pagar R$ {conta:.2f}')
    if qt_comb > 20:
        desconto = True
else:
    print('ERRO. Digite uma opção válida...')
