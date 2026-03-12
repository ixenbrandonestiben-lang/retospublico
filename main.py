def calcular ():
    separador()
    print(input("ingrese el nombre del alimento: "))
    separador()
    proteina = float(input("ingrese los gramos de proteina:"))  
    separador()               
    carbohidratos = float(input("ingrese los gramos de carbohidratos: "))
    separador() 
    grasa = float(input("ingrese los gramos de grasa: "))
    separador()
    suma = (proteina * 4) + (carbohidratos * 4) + (grasa * 9)
    separador()
    print("el total de calorias es: ", suma)
    separador()
    print("gracias por usar la calculadora de calorias")
    
def separador():
    print("----------------------------------------------------------------------")

    
while True:
    try:
        print("bienvenido a la calculadora de calorias")
        calcular()
        break
    except ValueError:
        print("error: por favor ingrese un numero valido")
                             