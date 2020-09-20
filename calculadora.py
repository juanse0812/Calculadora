#calculadora
#se añade las librerias y se agrega la estructura de la calculadora
from tkinter import *
from math import *
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("400x600")
ventana.resizable(False, False)
ventana.configure(background="turquoise4")
#SE SIGUE AÑADIENDO LA ESTRUCTURA DE LA CALCULADORA Y SE AÑADE LA FUNCION A
color_boton="light slate gray"
ancho_boton=10
alto_boton=3
operador = ""
def limpiar():
    global operador
    operador = ""
    texto_pantalla.set("0")
def pulsar(A):
    global operador
    operador += str(A)
    texto_pantalla.set(operador)
def resultado():
    global operador
    try:
        r = str(eval(operador))
    except:
        r = "Error"
    texto_pantalla.set(r)

