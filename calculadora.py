from pack.funciones import *
from os import *

"""
a- Ingreso un operando
b- Ingreso segundo operando
c- Operaciones
d- Mostrar Resultado
e- Salir

Se van desbloqueando cuando el anterior se realizo
Una ver Mostrado el resultado se bloquea todo de nuevo
Lo unico no bloqueado es el punto a y e al inicio
Cuidado con el erro de dividir por 0
"""

def limpiar_pantalla():
    system("cls")

def menu():
    print(f"""
    CALCULADORA
a- Ingresar primer valor
b- Ingresar segundo valor
c- Operaciones
d- Mostrar Resultado
e- Salir
                    
x = {operando_a}         
y = {operando_b}         
""")
    return input("\nSeleccione una opcion del menu: \n") # esta dentro de funcion menu

def submenu():
    print(f"""
1- Sumar
2- Restar
3- Dividir
4- Multiplicar
5- Factorial
""")

primer_paso = False
segundo_paso = False
tercer_paso = False
operando_a = None
operando_b = None

def validar_e_ingresar_numero()-> int:
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            return numero
        except ValueError:
            print("ERROR: Ingrese un número válido.")

while True:
    match menu():
        case "a":
            operando_a = validar_e_ingresar_numero()
            primer_paso = True
            limpiar_pantalla()
        case "b":
            if primer_paso:
                operando_b = validar_e_ingresar_numero()
                segundo_paso = True
                limpiar_pantalla()
            else:
                print("\nDebe ingresar el primer valor\n")
                system("pause")
                limpiar_pantalla()
        case "c":
            if segundo_paso:
                submenu()
                resultado = whileOpciones(operando_a,operando_b)
                limpiar_pantalla()
                tercer_paso = True
            else:
                print("\nDebe ingresar un valor primero\n")
                system("pause")
                limpiar_pantalla()
        case "d":
            if tercer_paso:
                print(f"El resultado es: {resultado}")
                system("pause")
                limpiar_pantalla()
            elif segundo_paso:
                print("\nNo podes ver el resultado sin ingresar un operador\n")
                system("pause")
                limpiar_pantalla()
            else:
                print("\nDebe ingresar un valor primero\n")
                system("pause")
                limpiar_pantalla()
        case "e":
            break


