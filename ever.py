#!/usr/bin/env python3
# EVER PRO3 MATRIX
# Compatible con Termux - Python 3

import os
import random
import string
import time
import subprocess


# COLORES ANSI
GREEN = "\033[92m"
DARK = "\033[32m"
WHITE = "\033[97m"
RED = "\033[91m"
RESET = "\033[0m"


# RUTA DE SALIDA
SALIDA = "EVER_RESULTADOS"


def limpiar():
    os.system("clear")


def matrix_intro():
    limpiar()
    caracteres = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in range(15):
        linea = "".join(random.choice(caracteres) for _ in range(60))
        print(GREEN + linea + RESET)
        time.sleep(0.05)

    time.sleep(1)


def logo():
    print(GREEN + r"""
 ███████╗██╗   ██╗███████╗██████╗ 
 ██╔════╝██║   ██║██╔════╝██╔══██╗
 █████╗  ██║   ██║█████╗  ██████╔╝
 ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗
 ███████╗ ╚████╔╝ ███████╗██║  ██║

        EVER PRO3 MATRIX
    """ + RESET)


def barra(total):
    for i in range(total):
        porcentaje = int((i+1)/total*30)
        print(
            "\r["
            + "#" * porcentaje
            + "-" * (30-porcentaje)
            + f"] {i+1}/{total}",
            end=""
        )
        time.sleep(0.02)
    print()


def crear_carpeta():
    if not os.path.exists(SALIDA):
        os.mkdir(SALIDA)



# -------------------------------
# GENERADOR DE NOMBRES
# -------------------------------

nombres = [
"Juan","Carlos","Luis","Pedro","Miguel",
"José","Mateo","Lucas","Santiago",
"María","Ana","Sofía","Camila",
"Valentina","Lucía","Martina"
]


def generador_nombres():

    cantidad = int(input("Cantidad de resultados: "))

    print("""
1. Nombre + Nombre
2. Nombre + Número
""")

    opcion=input("> ")

    resultados=[]

    for i in range(cantidad):

        if opcion=="1":
            valor=random.choice(nombres)+" "+random.choice(nombres)

        else:
            valor=random.choice(nombres)+str(random.randint(100,9999))

        resultados.append(valor)

    barra(cantidad)

    guardar(resultados,"nombres.txt")



# -------------------------------
# GENERADOR PASSWORD
# -------------------------------

def generador_password():

    longitud=int(input("Longitud: "))
    cantidad=int(input("Cantidad: "))

    usar = string.ascii_letters + string.digits + "!@#$%&*"

    lista=[]

    for i in range(cantidad):
        clave="".join(
            random.choice(usar)
            for _ in range(longitud)
        )
        lista.append(clave)

    barra(cantidad)

    guardar(lista,"passwords.txt")



# -------------------------------
# LISTAS PERSONALIZADAS
# -------------------------------

def lista_personalizada():

    ruta=input("Ruta del archivo de nombres: ")

    if not os.path.exists(ruta):
        print(RED+"Archivo no encontrado"+RESET)
        return

    prefijo=input("Prefijo: ")
    sufijo=input("Sufijo: ")

    with open(ruta,"r",encoding="utf-8") as f:
        nombres=f.read().splitlines()


    resultados=[]

    for nombre in nombres:
        resultados.append(
            prefijo+nombre+sufijo
        )

    barra(len(resultados))

    guardar(resultados,"lista_personalizada.txt")



# -------------------------------
# GUARDADO
# -------------------------------

def guardar(datos,nombre):

    crear_carpeta()

    ruta=input(
        f"Ruta de guardado (ENTER = {SALIDA}/{nombre}): "
    )

    if ruta.strip()=="":
        ruta=os.path.join(SALIDA,nombre)

    with open(ruta,"w",encoding="utf-8") as f:
        for linea in datos:
            f.write(linea+"\n")


    print(
        GREEN+
        "\nGuardado correctamente:"
        +ruta+
        RESET
    )



# -------------------------------
# ADMINISTRADOR PYTHON
# -------------------------------

def archivos():

    print("""
1. Crear archivo .py
2. Editar archivo
3. Ejecutar script
4. Mostrar archivos
""")

    op=input("> ")

    if op=="1":

        ruta=input("Nombre/ruta archivo: ")

        if not ruta.endswith(".py"):
            ruta+=".py"

        with open(ruta,"w") as f:
            f.write("# Creado con EVER PRO3 MATRIX\n")

        print("Archivo creado")


    elif op=="2":

        ruta=input("Archivo a editar: ")

        if os.path.exists(ruta):

            with open(ruta) as f:
                contenido=f.read()

            print(contenido)

            nuevo=input("Agregar texto: ")

            with open(ruta,"a") as f:
                f.write("\n"+nuevo)

        else:
            print("No existe")


    elif op=="3":

        ruta=input("Script a ejecutar: ")

        try:
            subprocess.run(
                ["python",ruta]
            )
        except:
            print("Error ejecutando")


    elif op=="4":

        for archivo in os.listdir():
            if archivo.endswith(".py"):
                print(archivo)



# -------------------------------
# MENU PRINCIPAL
# -------------------------------

def menu():

    while True:

        limpiar()
        logo()

        print(GREEN+"""
[1] Generador de nombres
[2] Generador de contraseñas
[3] Listas personalizadas
[4] Administrador Python
[5] Salir
""" + RESET)


        op=input("EVER > ")

        try:

            if op=="1":
                generador_nombres()

            elif op=="2":
                generador_password()

            elif op=="3":
                lista_personalizada()

            elif op=="4":
                archivos()

            elif op=="5":
                break

        except Exception as e:
            print(RED,"Error:",e,RESET)

        input("\nENTER para continuar")



if __name__=="__main__":
    matrix_intro()
    menu()