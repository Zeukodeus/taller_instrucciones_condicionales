x = int(input("Ingrese el valor de su sueldo actual: "))

if x<945200 :

    rta = "fue denegado tu crédito"

else :

    y = int(input("si tiene deudas ingrese el número 1, de lo contrario ingrese cualquier otro número: "))

    if y==1 :
        
        rta= "tu crédito fue denegado, lo sentimos"

    else : 

        rta = "tu crédito fue aprovado, FELICIDADES"

print (rta)