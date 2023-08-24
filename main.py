import numeros
import asyncio

def menu():

    print("Bienvenido a Farmacia San Pedro")

    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmética\n[A] - Alimentos\n")
        try:
            mi_seccion = input("Elija la sección de su preferencia: ").upper()
            ["P", "F", "C", "A"].index(mi_seccion)
            
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    numeros.decorador(mi_seccion)
    


def inicio():

    while True:
        menu()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break
inicio()
