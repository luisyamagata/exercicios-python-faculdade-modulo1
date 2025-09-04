# Agora, a nossa pizzaria está cobrando uma taxa fixa de R$5 por entrega, além de R$1 por km até 5km, e R$2 por km até 10km. Mais ainda não entregamos com a distância superior a 10km.

# TODO: Taxa fixa: R$ 5.00
# TODO: Taxa variável:
#    Fixa + R$1.00 por km inferior ou igual a 5km
#    Fixa + R$2.00 por km superior a 5km E inferior a 10 km
#    Ainda não entregamos a distâncias superiores a 10 KM...
#       Print da mensagem, pedindo desculpas.


frete = 5

print('''
      =====================
      Selecione o Cliente.
      =====================
      ''')
cliente = int(input(f''' 
                    Digite 1 para Selecionar Joana (8km).
                    Digite 2 para Selecionar Guilherme (3km)
                    Digite 3 para Selecionar Rafael (11km) '''))

#print(cliente)
if cliente == 1:
    dist = 8
elif cliente == 2:
    dist = 3
elif cliente == 3:
    dist = 11
else:
    print('❌ERRO! Digite um número de cliente Válido.')
    cliente = int(input(f''' 
                    Digite 1 para Selecionar Joana (8km).
                    Digite 2 para Selecionar Guilherme (3km)
                    Digite 3 para Selecionar Rafael (11km)'''))

if dist <= 5:
    taxa_variavel = dist * 1
    entrega = frete + taxa_variavel
elif dist > 5 and dist < 10:
    taxa_variavel = ((dist-5)  * 2) + (5 * 1)
    entrega = frete + taxa_variavel
elif dist > 10:
    print('😥 Sinto Muito! Não realizamos ainda entregas para locais com distância superior a 10 KM...')


if cliente == 1 or cliente == 2:
    print(f'O valor do seu Frete com Taxa é de R${entrega}.00. R$ 5.00 da taxa fixa + R$ {taxa_variavel}.00 da taxa variável')


