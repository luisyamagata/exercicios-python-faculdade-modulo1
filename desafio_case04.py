# SISTEMA DE NOTAS
# Uma escola precisa de um sistema para calcular se o aluno passou ou não.
#TODO Pedir ao aluno para informar duas notas (N1 e N2)
#TODO Calcule a média das notas
#TODO Se a média for maior ou igual a 7, mostre "APROVADO"
#       * Se a média for entre 5 e 6.9, mostre "RECUPERAÇÃO"
#       * Se a média for menor que 5, mostre "REPROVADO"

n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
media = ((n1+n2)/2)
print(n1)
print(n2)
print(f'A sua média foi de {media:.2f}')
if media >= 7:
    print('👍 Parabéns, você foi APROVADO')
elif media > 5 and media <= 6.9:
    print('😒 Infelizmente, você ficou em RECUPERAÇÃO') 
else:
    print('😔 Sinto muito... Você foi REPROVADO.')
