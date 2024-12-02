N1= int(input("Ingrese el primer número: "))
N2= int(input("Ingrese un segundo número diferente: "))
N3= int(input("Ingrese un tercer número diferente a los dos anteriores: "))

if N1>N2 and N1>N3:
    MAYOR=N1

elif N2>N3:
    MAYOR=N2

else:
    MAYOR=N3

print(f"EL VALOR MAYOR ENTRE: N1, N2 Y N3 ES: {MAYOR}")