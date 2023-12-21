# CÁLCULO IMC DE ESTUDIANTES

import os

header = """
*******************************
\tCÁLCULO IMC
*******************************
"""

def verify(valorDato, nombreDato, tipoDato):
    valorDato = 0
    isIncorrect = True
    while (isIncorrect):
        try:
            valorDato = tipoDato(input(f"Ingrese {nombreDato} del estudiante : "))
        except ValueError:
            print("Ingrese un dato válido")
        else:
            if (valorDato <= 0):
                print("Ingrese un número positivo")
            else:
                isIncorrect = False
    return valorDato

nombre = input("Ingrese el nombre del estudiante : ")
valor = 0
edad = verify(valor, "edad", int)
peso = verify(valor, "peso", float)
altura = verify(valor, "altura", float)

imc = peso/pow(altura, 2)
categoria = ""
estudiante = [nombre, edad, peso, altura, imc, categoria]

if (imc >= 18.5 and imc <= 24.9):
    estudiante[5] = "Normal"
elif (imc >= 25 and imc <= 29.9):
    estudiante[5] = "Sobrepeso"
elif (imc >= 30 and imc <= 34.9):
    estudiante[5] = "Obesidad I"
elif (imc >= 35 and imc <= 39.9):
    estudiante[5] = "Obesidad II"
elif (imc > 40):
    estudiante[5] = "Obesidad III"

os.system("cls")
print(header)
print("Nombre:    \t", estudiante[0])
print("Edad:      \t", estudiante[1])
print("IMC:       \t", estudiante[4])
print("Categoría: \t", estudiante[5])