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

#Se inserta el tipo de texto para la pantalla y se incluyen los primeros botones para la calculadora
texto_pantalla = StringVar()
#botones de la primera fila
Boton0 = Button(ventana, text="0", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(0)).grid(row=1, column=0, pady=10)
Boton1 = Button(ventana, text="1", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(1)).grid(row=1, column=1, pady=10)
Boton2 = Button(ventana, text="2", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(2)).grid(row=1, column=2, pady=10)
Boton3 = Button(ventana, text="3", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(3)).grid(row=1, column=3, pady=10)
#SE INSERTA LA SEGUNDA FILA DE BOTONES PARA LA PANTALLA, RECUERDE COMPAÑERO MANEJAR LA MISMA LINEA DE COMANDOS GRID
#botones de la segunda fila
Boton4 = Button(ventana, text="4", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(4)).grid(row=2, column=0, pady=10)
Boton5 = Button(ventana, text="5", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(5)).grid(row=2, column=1, pady=10)
Boton6 = Button(ventana, text="6", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(6)).grid(row=2, column=2, pady=10)
Boton7 = Button(ventana, text="7", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(7)).grid(row=2, column=3, pady=10)
