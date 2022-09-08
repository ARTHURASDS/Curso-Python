nome = input('Qual o seu nome?')
idade = int(input('Qual a sua idade?'))

menor_idade = 20
maior_idade = 30

if idade <= maior_idade and >= menor_idade:
    print(f'{nome} pode receber o empréstimo')
else:
    print(f'{nome} não pode receber o empréstimo')
