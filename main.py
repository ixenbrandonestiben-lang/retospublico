def calcular ():
    proteina = float(input("ingrese los gramos de proteina:"))                 
    carbohidratos = float(input("ingrese los gramos de carbohidratos: "))
    grasa = float(input("ingrese los gramos de grasa: "))
    
    suma = (proteina * 4) + (carbohidratos * 4) + (grasa * 9)
    print("el total de calorias es: ", suma)
    
while True:
    try:
        print("bienvenido a la calculadora de calorias")
        calcular()
        break
    except ValueError:
        print("error: por favor ingrese un numero valido")
                             