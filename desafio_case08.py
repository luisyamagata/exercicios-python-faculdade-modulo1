# BANCO DIGITAL
# Um cliente pode fazer um saque no banco
# 1. Peça o salto atual da conta e o valor do saque.
# 2. Se o valor do saque for maior que o saldo, mostre "Saldo insuficiente"
# 3. Caso contrário, faça o saque e mostre o novo saldo.

print('-='*40)
print('''Bem-vindo ao Banco Zero Um 
Seu melhor Banco Digital''')
print('-='*40)
saldo = float(input('Digite o saldo atual da conta: '))
saque = float(input('Digite o valor que deseja sacar de sua conta: '))
if saque > saldo:
    print('Saldo insuficiente.')
else:
    saldo = saldo - saque
    print(saldo)