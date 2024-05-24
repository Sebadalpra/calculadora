from os import *

def suma(valor_uno: int, valor_dos: int)-> int:
    return valor_uno + valor_dos

def resta(valor_uno: int, valor_dos: int)-> int:
    return valor_uno - valor_dos

def dividir(valor_uno: int, valor_dos: int)-> float:
    return valor_uno / valor_dos

def multiplicar(valor_uno: int, valor_dos: int)-> int:
    return valor_uno * valor_dos

def factorial(valor_factorial: int) -> int:
    if valor_factorial < 0:
        print("No se puede calcular el factorial de un número negativo.")
        system("pause")
        return None
    elif valor_factorial == 0 or valor_factorial == 1:
        return 1
    else:
        fact = 1
        for i in range(2, valor_factorial + 1):
            fact *= i
        return fact

def whileOpciones(valor_uno: int, valor_dos: int):
    while True:
        opcion = input("\nIngrese un opcion : \n")
        match opcion.lower():
            case "sumar" | "1":
                return suma(valor_uno,valor_dos)
            case "restar" | "2":
                return resta(valor_uno,valor_dos)
            case "dividir" | "3":
                try:
                    return dividir(valor_uno,valor_dos)
                except ZeroDivisionError:
                    print("No se puede dividir por cero")
                    system("pause")
                    return
            case "multiplicar" | "4":
                return multiplicar(valor_uno,valor_dos)
            case "factorial" | "5":
                factorial_uno = factorial(valor_uno)
                factorial_dos = factorial(valor_dos)
                return factorial_uno, factorial_dos
            case _:
                print("Opción no válida")

            