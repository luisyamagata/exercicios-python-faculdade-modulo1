'''## **Case 1 – Loja de Doces 🍬**

A loja “Doce Sabor” vende balas a **R$ 0,50 cada** 
e chocolates a **R$ 2,00 cada**.

📌 Regras:

Pergunte ao cliente quantas balas e quantos chocolates ele deseja comprar.

Calcule o valor total da compra.
 Se o valor total for maior que R$ 20, mostre a mensagem:
"Parabéns, você ganhou um desconto de 10%!" e aplique o desconto.
 Mostre o valor final da compra.'''

#TODO armazenar a escolha do cliente OK 
#TODO calcular o valor total da compra: (Balas * 0.5) + (Choco * 2) OK
#TODO SE o valor for > R$ 20.00 exibir a mensagem "Parabéns, você ganhou um desconto de 10%!" 
#TODO e aplicar tal desconto
#TODO Exibir o valor final da compra

print('-='*30)
print('Bem-Vindo à Loja DOCE SABOR')
print('-='*30)
conta = 0
escolha = int(input('Temos Balas a R$ 0.50 e chocolates a R$ 2.00 cada. Digite 0 para comprar balas ou 1 para comprar chocolates, ou digite 2 para comprar ambos: '))
if escolha == 0:
    print('Você selecionou BALAS:')
    qt_balas = int(input('Digite a quantidade de balas: '))
    custo_balas = (qt_balas * 0.5)
    conta += custo_balas
    print(f'Você deseja {qt_balas} balas, elas culstam R$ {conta:.2f}')
    
elif escolha == 1:
    print('Você selecionou CHOCOLATES.')
    qt_choco = int(input('Digite a quantidade de chocolates: '))
    custo_choco = (qt_choco * 2)
    conta += custo_choco
    print(f'Você deseja {qt_choco} chocolates, eles culstam R$ {conta:.2f}')
    
elif escolha == 2:
    print('Você selecionou BALAS E CHOCOLATES')
    print('Primeiro, defina a quantidade de BALAS:')
    
    qt_balas = int(input('Digite a quantidade de balas: '))
    custo_balas = (qt_balas * 0.5)
    print(f'Você deseja {qt_balas} balas, elas culstam R$ {custo_balas:.2f}')
    print('Agora, defina a quantidade de CHOCOLATES:')
    qt_choco = int(input('Digite a quantidade de chocolates: '))
    custo_choco = (qt_choco * 2)
    print(f'Você deseja {qt_choco} chocolates, eles culstam R$ {custo_choco:.2f}')
    conta += custo_balas + custo_choco
    print(f'O valor total da sua compra é de R${conta:.2f}')
if conta > 20:
    print('Parabéns, você ganhou um desconto de 10%!')
    desconto = conta * 0.1
    conta_c_desc = conta - desconto
    print(f'O valor da sua compra com desconte é de R$ {conta_c_desc:.2f}')    

