A=int(input("NÚMERO 1: "))
B=int(input("NÚMERO 2: "))

C= A%B
if C == 0:
    D=B%A
    if D == 0:
        rta= f"{A} es igual a {B}"
    else:
        rta=f"{A} es multiplo de {B}"
else:
    D=B%A
    if D == 0:
        rta = f"{B} es multiplo de {A}"
    else:
        rta=f"{A} y {B} no son multiplos"


print(rta)
