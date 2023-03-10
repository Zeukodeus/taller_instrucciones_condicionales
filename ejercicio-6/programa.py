A = int(input("ingrese el valor de a: "))
B = int(input("ingrese el valor de b: "))
C = int(input("ingrese el valor de c: "))


D = (B**2)-(4*A*C)

if (D == 0):
    X = -B/2*A
    rta = "las dos raices son: " + str(X)
else:
    if (D<0):
        rta = "raices imaginarias"
    else:
        X2 = (-(B)+(math.sqrt(D)))/(2*A)
        X1 = (-(B)-(math.sqrt(D)))/(2*A)
        rta = "las raices son: "+" x1: "+ str(X1)+" x2: " + str(X2)

print(rta)