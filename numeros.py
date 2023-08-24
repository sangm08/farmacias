
from configparser import SectionProxy
import time
from collections import deque
import turnos

def numeros_perfumeria():
    for n in range(1, 10000):
        yield f"P - {n}"


def numeros_farmacia():
    for n in range(1, 10000):
        yield f"F - {n}"


def numeros_cosmetica():
    for n in range(1, 10000):
        yield f"C - {n}"

def numeros_alimentos():
    for n in range(1, 10000):
        yield f"A - {n}"



p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()
a = numeros_alimentos()

def decorador(seccion):
  
    filaPerfumeria = deque([])
    filaFarmacia = deque([])
    filaCosmetica = deque([])
    filaAlimentos = deque([])

    print("\n" + "*" * 23)
    print("Su número es:")
    if seccion == "P":
        perf = next(p)
        print(perf)
        filaPerfumeria.append(str(perf))
    elif seccion == "F":
        farm = next(f)
        filaFarmacia.append(str(farm))
        print(farm)
    elif seccion == "C":
        cosme = next(c)
        print(cosme)
        filaCosmetica.append(str(cosme))
    elif seccion == "A":
        alim = next(c)
        print(alim)
        filaAlimentos.append(str(alim))
    turnos.recorreFila(filaPerfumeria)
    turnos.recorreFila(filaFarmacia)
    turnos.recorreFila(filaCosmetica)
    turnos.recorreFila(filaAlimentos)
    print("Aguarda un momento: Pronto serás atendido. Te aparecerá tu turno en cuanto esté disponible. ")
    print("*" * 23 + "\n")


