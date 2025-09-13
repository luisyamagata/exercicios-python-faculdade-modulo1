'''O cinema “CineMais” cobra **R$ 20,00 
o ingresso**.

📌 Regras:
Pergunte a idade do cliente.
Se a idade for menor que 12 anos, o ingresso custa R$ 10.00.
Se a idade for 60 anos ou mais, o ingresso custa R$ 12.00
Caso contrário, o ingresso custa o valor normal R$ 20.00'''

idade = int(input('Qual a sua idade?'))
if idade < 12:
    ingresso = 10
elif idade >= 60:
    ingresso = 12
else:
    ingresso = 20
print(f'Você tem {idade} anos. Portanto, seu ingresso custa R${ingresso:.2f}')
