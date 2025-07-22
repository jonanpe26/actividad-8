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
    return contar()