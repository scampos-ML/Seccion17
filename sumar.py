def sumar(a,b):
    return a+b

while True:
    try:
        n1 = int(input("Ingrese valor n1: "))
        n2 = int(input("Ingrese valor n2: "))
        break
    except:
        print("Ingrese valores enteros")

print(sumar(n1,n2))