n = int(input("Ingrese el valor del costo del articulo: "))


if n< 3000:
    m = (15*n)/100
    
else:
    if 3000 <= n <= 6000:
        m = 500
    else: 
      m = (25* n)/100


p = n + m


print(p)