def menu():
    print("1.Calcular el facorial de un numero")
    print("2.Suma de los primeros N numeros naturales")
    print("3. Calcular el e-nesimo numero fibonacci")
    print("4.Contar cuatas veces aparece una letra en una palabra")
    print("5.Invertir una cadena de texto")
    print("6.Calcukar la potencia de un numero")
    print("7.salir")

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
def suma(n):
    if n==1:
        return 1
    return n+suma(n-1)
def fibonacci(n):
    if n ==0:
        return 0
    return fibonacci(n-1)+fibonacci(n-2)
def contar(palabra,letra):
    if palabra=="":
        return  0
    if palabra(0)==letra:
        return 1+contar(palabra[1:],letra)
    return contar(palabra,letra)
def invertir(cadena):
    if cadena =="":
        return ""
    return invertir(cadena)+cadena[0]
def potencia(base, exponente):
    if exponente==0:
        return 1
    else:
        return base*potencia(base, exponente-1)

while True:
    menu()
    opcion=input("selecciona la opcion")
    if opcion =="1":
        num=input("ingrese un numero entero positivo")
        if num.isdigit():
            print("factorial",factorial(int(num)))
        else:
            print("error")
    elif opcion == "2":
        n =input("ingrese un numero entero positivo")
        if n.isdigit():
            print("suma de primeros", n, "numeros", suma(int(n)))
        else:
            print("error")
    elif opcion == "3":
        n=input("ingrese la posicion de fibonacci")
        if n.isdigit():
            print(f"fibonacci({n} =", fibonacci(int(n)))
        else:
            print("error")
    elif opcion == "4":
        palabra =input("ingrese la palabra")
        letra = input("ingrese la letra a contar")
        if (letra)==1:
            print(f"la letra{letra} aparece {contar(palabra, letra)} veces")
        else:
            print("error")
    elif opcion == "5":
        cadena = input("ingrese el texto")
        print("cadena invertida", invertir(cadena))
    elif opcion == "6":
        base = int(input("Base: "))
        exp = int(input("Exponente: "))
        if exp >= 0:
            print(f"{base}^{exp} = {potencia(base, exp)}")
        else:
            print("Error")
    elif opcion == "7":
        print("¡Gracias por usar el programa!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")

