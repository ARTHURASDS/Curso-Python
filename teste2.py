nome = "Arthur Santana"
idade = 19
altura = 1.75
peso = 86
ano = 2022
nascimento = ano - idade
imc = peso / altura**2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kgs.')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')
