# CALCULADORA SIMPLES
# TODO Peça 2 Números ao usuário
# TODO Pergunte a operação básica que ele deseja realizar:
# TODO Use condicionais para realizar a operação escolhida
# TODO Mostre o resultado na tela

print('-='*40)
print('Calculadora BOLADONA')
print('-='*40)

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
operacao = int(input('''Selecione uma operação matemática:
                    [0] - SOMA
                    [1] - SUBTRAÇÃO
                    [2] - MULTIPLICAÇÃO
                    [3] - DIVISÃO '''))
print(operacao)
if operacao == 0:
    conta = n1 + n2
    print(f'O resultado da sua conta de soma é: {conta}')
elif operacao == 1:
    conta = n1 - n2
    print(f'O resultado da sua conta de subtração é: {conta}')
elif operacao == 2:
    conta = n1 * n2
    print(f'O resultado da sua conta de multiplicação é: {conta}')
elif operacao == 3:
    if n2 == 0:
        print('Erro. Não é possível dividir por zero!')
    conta = n1 / n2
    print(f'O resultado da sua conta de divisão é: {conta:.2f}')
