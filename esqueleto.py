
""" Proyecto Final - Programación Cientifica
    Juliana Rojas - 202010183
    Sebastian Baquero - 201728102
    Juan Camilo - 202010326
"""
from tkinter import*
import numpy as np
import matplotlib.pyplot as plt

# ---------- VARIABLES DEPENDIENTES ----------

from tkinter import *
from tkinter import filedialog

# ---------- LABELS ----------
parameterTitle = 'Párametros'
btnExtraer = 'Exportar'
btnImportar = 'Importar'
tiempoSimulacion = 'Tiempo de simulación'
tiempo = 'Años'
St = 'S(t)'
Et = 'E(t)'
It = 'I(t)'
Lt = 'L(t)'
solutionMethodTitle = 'Método de solución'
btnSolutionLabel1 = 'Euler adelante'
btnSolutionLabel2 = 'Euler atrás'
btnSolutionLabel3 = 'Euler modificado'
btnSolutionLabel4 = 'Runge-Kutta 2'
btnSolutionLabel5 = 'Runge-Kutta 4'
btnSolutionLabel6 = 'solve_ivp'

beta = u'\u03b2'
fi = u'\u03d5'
mu = u'\u03bc'
lmbda = u'\u03BB'
delta = u'\u03B4'
ro = u'\u03C1'
kappa = u'\u03BA'
r1= 'r1'
r2= 'r2'
gamma = u'\u03B3'
d1= 'd1'
d2= 'd2'


# ----------- MÉTODOS ---------
def exportar():
    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = filedialog.asksaveasfile(filetypes=files, defaultextension=files)

def importar():
    filename = filedialog.askopenfilename(initialdir="/",
                                            title="Select a File",
                                            filetypes=(("Text files",
                                                         "*.txt*"),
                                                        ("all files",
                                                        "*.*")))

def eulerAdelante():
    return

def eulerAtras():
    pass

def eulerModificado():
    pass

def rungeKutta2():
    pass

def rungeKutta4():
    pass

def solve_ivp():
    pass

root = Tk()
root.title('Modelo Tuberculosis')  
root.geometry("1200x675")



# Paneles principales
leftPanel = Frame(root, width=400)
rightPanel = Frame(root, width=400)
leftPanel.pack(expand='true', side='left', fill='y')
rightPanel.pack(side='right', fill='y', padx=40, pady=20)

#Panel Izquierdo
lTopPanel = Frame(leftPanel,width=400,padx=50,pady=85)
lBottomPanel = Frame(leftPanel,width=400,padx=50,pady=20)
lTopPanel.pack()
lBottomPanel.pack()


#Panel Izquierdo Superior
btnExportar = Button(lTopPanel , text=btnExtraer, padx=50, fg='white', background='#E13B3B', command=lambda: exportar())
btnImportar = Button(lTopPanel, text=btnImportar, padx=50, fg='white', background='#E13B3B', command=importar)
img = PhotoImage(file="gráfica.PNG")

imgLabel = Label(lTopPanel, image = img)
SLabel = Label(lTopPanel,text=St)
ELabel = Label(lTopPanel,text=Et)
ILabel = Label(lTopPanel, text=It)
LLabel = Label(lTopPanel, text=Lt)
espacio = Label(lTopPanel,text=' ')

loadimage = PhotoImage(file="circle2.png")
roundedbutton1 = Button(lTopPanel, image=loadimage, borderwidth=2, relief="raised")
roundedbutton1["bg"] = "white"
roundedbutton2 = Button(lTopPanel, image=loadimage, borderwidth=2, relief="raised")
roundedbutton2["bg"] = "white"
roundedbutton3 = Button(lTopPanel, image=loadimage, borderwidth=2, relief="raised")
roundedbutton3["bg"] = "white"
roundedbutton4 = Button(lTopPanel, image=loadimage, borderwidth=2, relief="raised")
roundedbutton4["bg"] = "white"

btnExportar.grid(row=1,column=2)
btnImportar.grid(row=1,column=3)
imgLabel.grid(row=3,columnspan=6, column=0)
espacio.grid(row=4,column=1)
SLabel.grid(row=7, column=1)
ELabel.grid(row=7,column=2)
ILabel.grid(row=7,column=3)
LLabel.grid(row=7,column=4)
roundedbutton1.grid(row=6,column=1)
roundedbutton2.grid(row=6,column=2)
roundedbutton3.grid(row=6,column=3)
roundedbutton4.grid(row=6,column=4)


#Panel Izquierdo Inferior
titleLabelBL = Label(lBottomPanel, text=tiempoSimulacion)
espacio = Label(lBottomPanel,text=' ')
tiempoLabel = Label(lBottomPanel,text = tiempo)
entryTiempo1 = Entry(lBottomPanel, borderwidth=2, relief="ridge")
entryTiempo2 = Entry(lBottomPanel, borderwidth=2, relief="ridge")
entryTiempo3 = Entry(lBottomPanel, borderwidth=2, relief="ridge")


titleLabelBL.grid(row=3,columnspan=2,column=2)
entryTiempo1.grid(row=4,column=0)
entryTiempo2.grid(row=4,column=2)
entryTiempo3.grid(row=4,column=4)
espacio.grid(row=4,column=5)
tiempoLabel.grid(row=4,column=6)

# Panel Derecho
rTopPanel = Frame(rightPanel, padx=72, pady=50, borderwidth=2, width=350)
rTopPanel.config(bd=1, relief=SOLID)
rBottomPanel = Frame(rightPanel, width=350, padx=75, pady=20, borderwidth=2)
rBottomPanel.config(bd=1, relief=SOLID)
rTopPanel.pack()
rBottomPanel.pack()

# Panel Derecho Superior
titleLabelTR = Label(rTopPanel, text=parameterTitle)
btnParam1 = Label(rTopPanel, text=beta, padx=25, background='#F9A051', borderwidth=2, relief="ridge")
btnParam2 = Label(rTopPanel, text=fi, padx=25,background='#F9A051', borderwidth=2, relief="ridge")
btnParam3 = Label(rTopPanel, text=mu, padx=25,background='#F9A051', borderwidth=2, relief="ridge")
btnParam4 = Label(rTopPanel, text=lmbda, padx=25,background='#F9A051', borderwidth=2, relief="ridge")
btnParam5 = Label(rTopPanel, text=delta, padx=25,background='#F9A051', borderwidth=2, relief="ridge")
btnParam6 = Label(rTopPanel, text=ro, padx=25,background='#F9A051', borderwidth=2, relief="ridge")
btnParam7 = Label(rTopPanel, text=kappa, padx=25,background='#F9A051', borderwidth=2, relief="ridge")
btnParam8 = Label(rTopPanel, text=r1, padx=23,background='#F9A051', borderwidth=2, relief="ridge")
btnParam9 = Label(rTopPanel, text=r2, padx=23,background='#F9A051', borderwidth=2, relief="ridge")
btnParam10 = Label(rTopPanel, text=gamma, padx=25,background='#F9A051', borderwidth=2, relief="ridge")
btnParam11 = Label(rTopPanel, text=d1, padx=22,background='#F9A051', borderwidth=2, relief="ridge")
btnParam12 = Label(rTopPanel, text=d2, padx=22,background='#F9A051', borderwidth=2, relief="ridge")

entryParam1 = Entry(rTopPanel, borderwidth=2, relief="ridge")
entryParam2 = Entry(rTopPanel, borderwidth=2, relief="ridge")
entryParam3 = Entry(rTopPanel, borderwidth=2, relief="ridge")
entryParam4 = Entry(rTopPanel, borderwidth=2, relief="ridge")
entryParam5 = Entry(rTopPanel, borderwidth=2, relief="ridge")
entryParam6 = Entry(rTopPanel, borderwidth=2, relief="ridge")
entryParam7 = Entry(rTopPanel, borderwidth=2, relief="ridge")
entryParam8 = Entry(rTopPanel, borderwidth=2, relief="ridge")
entryParam9 = Entry(rTopPanel, borderwidth=2, relief="ridge")
entryParam10 = Entry(rTopPanel, borderwidth=2, relief="ridge")
entryParam11 = Entry(rTopPanel, borderwidth=2, relief="ridge")
entryParam12 = Entry(rTopPanel, borderwidth=2, relief="ridge")

titleLabelTR.grid(row=0,columnspan=2,column=0)
btnParam1.grid(row=1,column=0)
btnParam2.grid(row=3,column=0)
btnParam3.grid(row=5,column=0)
btnParam4.grid(row=7,column=0)
btnParam5.grid(row=9,column=0)
btnParam6.grid(row=11,column=0)
btnParam7.grid(row=13,column=0)
btnParam8.grid(row=15,column=0)
btnParam9.grid(row=17,column=0)
btnParam10.grid(row=19,column=0)
btnParam11.grid(row=21,column=0)
btnParam12.grid(row=23,column=0)
entryParam1.grid(row=1,column=1)
entryParam2.grid(row=3,column=1)
entryParam3.grid(row=5,column=1)
entryParam4.grid(row=7,column=1)
entryParam5.grid(row=9,column=1)
entryParam6.grid(row=11,column=1)
entryParam7.grid(row=13,column=1)
entryParam8.grid(row=15,column=1)
entryParam9.grid(row=17,column=1)
entryParam10.grid(row=19,column=1)
entryParam11.grid(row=21,column=1)
entryParam12.grid(row=23,column=1)

# Panel Derecho Inferior
titleLabelBR = Label(rBottomPanel, text=solutionMethodTitle)
btnMetodo1 = Button(rBottomPanel, text=btnSolutionLabel1, padx=50, command=eulerAdelante, background='#9C9EA2')
btnMetodo2 = Button(rBottomPanel, text=btnSolutionLabel2, padx=60, command=eulerAtras,background='#9C9EA2')
btnMetodo3 = Button(rBottomPanel, text=btnSolutionLabel3, padx=42, command=eulerModificado,background='#9C9EA2')
btnMetodo4 = Button(rBottomPanel, text=btnSolutionLabel4, padx=49, command=rungeKutta2,background='#9C9EA2')
btnMetodo5 = Button(rBottomPanel, text=btnSolutionLabel5, padx=49, command=rungeKutta4, background='#9C9EA2')
btnMetodo6 = Button(rBottomPanel, text=btnSolutionLabel6, padx=63, command=solve_ivp, background='#9C9EA2')

titleLabelBR.grid(row=0)
btnMetodo1.grid(row=1)
btnMetodo2.grid(row=2)
btnMetodo3.grid(row=3)
btnMetodo4.grid(row=4)
btnMetodo5.grid(row=5)
btnMetodo6.grid(row=6)


root.mainloop()