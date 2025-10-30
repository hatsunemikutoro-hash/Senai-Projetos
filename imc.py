# imc = peso / altura x altura

peso = int(input("quanto ce pesa: "))

altura = float(input("qual sua altura: "))

imc = peso / (altura **2)
print("---------------------")
if imc <= 18.5:
    print("Baixo peso")
elif 18.5 <= imc < 24.9:
    print("peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
elif 30 <= imc < 34.9:
    print("Obesidade grau 1")
elif 35 <= imc < 39.9:
    print("Obesidade grau 2")
elif imc >= 40:
    print("Obesidade grau 3")

print("{:.1f}".format(imc))