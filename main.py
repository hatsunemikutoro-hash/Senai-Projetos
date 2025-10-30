numero = int(input("Insira um numero: "))

array = [1,2,3,4,5,6,7,8,9,10]

for v in array:
    for i in range(1,11):
        print()
        print(v, "x", i, ":", v * i)

for i in range(1,21):
        print(numero, "x", i, ":", numero * i)