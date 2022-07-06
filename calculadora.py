def multiplicacion(num_uno, num_dos):
    resultado = float(num_uno * num_dos)
    return resultado 

def suma(num_uno, num_dos):
    resultado = float(num_uno + num_dos)
    return resultado

def division(num_uno, num_dos):
    resultado = float(num_uno / num_dos)
    return resultado

def resta(num_uno, num_dos):
    resultado = float(num_uno - num_dos)
    return resultado


intentos = True


while intentos == True: 
    Operacion = ""
    intentos_in = ""
    num_uno = ""
    num_dos = ""

    while Operacion not in ["x","+","/","-"]:
        Operacion = input("Cual operacion deseas hacer? Introduce 'x' para multiplicar, Introduce '+' para sumar, Introduce '/' para dividir, Introduce '+' para sumar ")
        Operacion = Operacion.lower()
        if Operacion not in ["x","+","/","-"]:
            print("Seleccione una opcion correcta, intente de nuevo")

        

    while type(num_uno) != float:
        num_uno = (input("Introduce un numero "))
        try:
           float(num_uno)
        except ValueError:
            print("No es un numero, intenta de nuevo")
        else: 
            num_uno = float(num_uno) 


    while type(num_dos) != float:
        num_dos = (input("Introduce otro numero "))
        try:
           float(num_dos)
        except ValueError:
            print("No es un numero, intenta de nuevo")
        else: 
            num_dos = float(num_dos)



    if Operacion == "x":
        resultado = multiplicacion(num_uno,num_dos)
        print(resultado)
    if Operacion == "+":
        resultado = multiplicacion(num_uno, num_dos)
        print(resultado)
    if Operacion == "-":
        resultado = resta(num_uno,num_dos)
        print(resultado)

    if Operacion == "/" and num_dos != 0 :
        resultado = division(num_uno,num_dos)
        print(resultado)
    elif Operacion =="/" and num_dos == 0:
        print("Indefinido")

    while intentos_in not in ["no","si"]:
        intentos_in = input("Desea hacer otro intento? Escriba Si o No ")
        intentos_in = intentos_in.lower()

    print(intentos_in)

    if intentos_in == "no":
        intentos = False 

    Operacion = ""

        
        
