nome = "Arthur Santana"
idade = 19
peso = 86
altura = 1.75
imc = peso / 1.75*1.75

print(nome, " tem ", idade, " anos, pesa ", peso, "kilos e possui IMC de ", imc)
print(f'{nome} tem {idade} anos de idade e imc de {imc:.2f}')
print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))
print('{} tem {} e seu imc é {}'.format(nome, idade, imc))