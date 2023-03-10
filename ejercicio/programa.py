x = int (input(" el valor de x: "))
y = int (input(" el valor de y: "))

if x==0 and y==0 :

    rta = "Están el origen"
else :

    if x==0 and (y>0 or y<0) :

        rta = "Está en el eje Y"

    else :
        if y==0 and (x>0 or x<0) :

            rta = "Está en el eje X"
        
        else :

            if x>0 and y>0 :

                rta = f"Está en el primer cuadrante {x, y}"
            
            else :

                if  x<0 and y>0:

                    rta = f"Está en el segundo cuadrante {x, y}"

                else :
                    
                    if x<0 and y<0 :

                        rta = f"Está en el tercer cuadrante {x, y}"

                    else :

                        x>0 and y<0

                        rta = f"Está en el cuarto cuadrante {x, y}"


print(rta)