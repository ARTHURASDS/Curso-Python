num1 = input("Digite Um Número! ")
num2 = input("Digite Outro Número! ")

def is_number(val):
    return is_int(val) or is_float(val)

try:

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print("Não foi possível converter os números para realizar o cálculo!")

except:

if is_number(num1) and is_number(num2)
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
else:
    print("O caracter digitado não é um número!")

