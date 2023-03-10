x = int(input("ingrese el valor del peso en kg: "))
d = float(input("ingrese el valor de la altura en m: "))


f = x/(d**2)


if f<16:
    rta= "Criterio de ingreso al hospital"
else:
    if 16<=f<17:
        rta = "infrapeso"
    else:
        if 17<=f<18:
            rta= "Bajo peso"
        else:
            if 18<=f<25:
                rta="peso normal (saludable)"
            else:
                if 25<=f<30:
                    rta= "Sobrepeso (obesidad grado I)"
                else:
                    if 30<=f<35:
                        rta= "Sobrepeso cronico (obesidad grado II)"
                    else:
                        if 35<=f<40:
                            rta="Obesidad premorbida (obesidad grado III)"
                        else:
                            rta= "Obesidad morbida (obesidad de grado IV)"
print(rta)