A=int(input("Número 1: "))
B=int(input("Número 2: "))
C=int(input("Número 3: "))


D=A+B

if D == C:
    rta= f"la suma de {A} y {B} es igual a {C}"
else:
    rta= f"la suma de {A} y {B} no son iguales a {C}"


print(rta)