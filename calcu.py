from tkinter import *
from math import *
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("400x600")
ventana.resizable(False, False)
ventana.configure(background="turquoise4")

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



texto_pantalla = StringVar()
#botones de la primera fila (JUAN)
Boton0 = Button(ventana, text="0", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(0)).grid(row=1, column=0, pady=10)
Boton1 = Button(ventana, text="1", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(1)).grid(row=1, column=1, pady=10)
Boton2 = Button(ventana, text="2", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(2)).grid(row=1, column=2, pady=10)
Boton3 = Button(ventana, text="3", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(3)).grid(row=1, column=3, pady=10)

#botones de la segunda fila (MAICOL)
#botones de la tercera fila
Boton4 = Button(ventana, text="4", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(4)).grid(row=2, column=0, pady=10)
Boton5 = Button(ventana, text="5", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(5)).grid(row=2, column=1, pady=10)
Boton6 = Button(ventana, text="6", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(6)).grid(row=2, column=2, pady=10)
Boton7 = Button(ventana, text="7", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(7)).grid(row=2, column=3, pady=10)

Boton8 = Button(ventana, text="8", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(8)).grid(row=3, column=0, pady=10)
Boton9 = Button(ventana, text="9", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(9)).grid(row=3, column=1, pady=10)
BotonIgual = Button(ventana, text="=", background=color_boton, width=ancho_boton, height=alto_boton, command=resultado).grid(row=3, column=2, pady=10)
BotonPunto= Button(ventana, text=".", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(".")).grid(row=3, column=3, pady=10)

#botones de la cuarta fila (MAICOL)
BotonLimpiar = Button(ventana, text="C", background=color_boton, width=ancho_boton, height=alto_boton, command=limpiar).grid(row=4, column=0, pady=10)
BotonSuma = Button(ventana, text="+", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar("+")).grid(row=4, column=1, pady=10)
BotonResta = Button(ventana, text="-", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar("-")).grid(row=4, column=2, pady=10)
BotonMult = Button(ventana, text="*", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar("*")).grid(row=4, column=3, pady=10)

#botones de la quinta fila 
BotonDiv = Button(ventana, text="÷", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar("/")).grid(row=5, column=0, pady=10)
BotonRaiz = Button(ventana, text="√", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar("sqrt")).grid(row=5, column=1, pady=10)
BotonPi = Button(ventana, text="π", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar("pi")).grid(row=5, column=2, pady=10)
BotonE = Button(ventana, text="E", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar("e")).grid(row=5, column=3, pady=10)
#botones de la sexta fila
BotonParenizq = Button(ventana, text="(", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar("(")).grid(row=6, column=0, pady=10)
BotonParender = Button(ventana, text=")", background=color_boton, width=ancho_boton, height=alto_boton, command=lambda:pulsar(")")).grid(row=6, column=1, pady=10)
pantalla = Entry(ventana, font=("arial", 20, "bold"), width=22, borderwidth=10, background="gray64", textvariable=texto_pantalla)
pantalla.grid(row=0, column=0, columnspan=4, padx=20, pady=20)
ventana.mainloop()