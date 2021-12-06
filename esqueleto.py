
""" Proyecto Final - Programación Cientifica
    Juliana Rojas - 202010183
    Sebastian Baquero - 201728102
    Juan Camilo - 202010326
"""
from tkinter import*
import numpy as np
import matplotlib.pyplot as plt

# ---------- VARIABLES DEPENDIENTES ----------


# ---------- LABELS ----------
parameterTitle = 'Párametros'
btnExtraer = 'Extraer'
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
btnSolutionLabel3 = 'Runge-Kutta 2'
btnSolutionLabel4 = 'Runge-Kutta 4'
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
    pass

def importar():
    pass

def eulerAdelante():
    return

def eulerAtras():
    pass

def rungeKutta2():
    pass

def rungeKutta4():
    pass


root = Tk()
root.title('Modelo Tuberculosis')  
root.geometry("1200x675")



# Paneles principales
leftPanel = Frame(root, width=400)
rightPanel = Frame(root, width=400)
leftPanel.pack(expand='true', side='left', fill='y')
rightPanel.pack(side='right', fill='y')

#Panel Izquierdo
lTopPanel = Frame(leftPanel,width=400,padx=50,pady=85)
lBottomPanel = Frame(leftPanel,width=400,padx=50,pady=50)
lTopPanel.pack()
lBottomPanel.pack()


#Panel Izquierdo Superior
btnExportar = Button(lTopPanel , text=btnExtraer, padx=50)
btnImportar = Button(lTopPanel, text=btnImportar, padx=50)
img = PhotoImage(file="gráfica.PNG")

imgLabel = Label(lTopPanel, image = img)
SLabel = Label(lTopPanel,text=St)
ELabel = Label(lTopPanel,text=Et)
ILabel = Label(lTopPanel, text=It)
LLabel = Label(lTopPanel, text=Lt)
espacio = Label(lTopPanel,text=' ')

loadimage = PhotoImage(file="circle2.png")
roundedbutton1 = Button(lTopPanel,image=loadimage)
roundedbutton1["bg"] = "white"
roundedbutton1["border"] = "0"
roundedbutton2 = Button(lTopPanel,image=loadimage)
roundedbutton2["bg"] = "white"
roundedbutton2["border"] = "0"
roundedbutton3 = Button(lTopPanel,image=loadimage)
roundedbutton3["bg"] = "white"
roundedbutton3["border"] = "0"
roundedbutton4 = Button(lTopPanel,image=loadimage)
roundedbutton4["bg"] = "white"
roundedbutton4["border"] = "0"

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
entryTiempo1 = Entry(lBottomPanel)
entryTiempo2 = Entry(lBottomPanel)
entryTiempo3 = Entry(lBottomPanel)


titleLabelBL.grid(row=3,columnspan=2,column=2)
entryTiempo1.grid(row=4,column=0)
entryTiempo2.grid(row=4,column=2)
entryTiempo3.grid(row=4,column=4)
espacio.grid(row=4,column=5)
tiempoLabel.grid(row=4,column=6)

# Panel Derecho
rTopPanel = Frame(rightPanel, padx=40, pady=70,borderwidth=2)
rTopPanel.config(bd=1, relief=SOLID)
rBottomPanel = Frame(rightPanel, width=350, padx=75,pady=20,borderwidth=2)
rBottomPanel.config(bd=1,relief=SOLID)
rTopPanel.pack()
rBottomPanel.pack()
#rTopPane.grid(row=0,column=0)
#rBottomPane.grid(row=1,column=0)

# Panel Derecho Superior
titleLabelTR = Label(rTopPanel, text=parameterTitle)
btnParam1 = Button(rTopPanel, text=beta, padx=25,background='#ff681f')
btnParam2 = Button(rTopPanel, text=fi, padx=25,background='#ff681f')
btnParam3 = Button(rTopPanel, text=mu, padx=25,background='#ff681f')
btnParam4 = Button(rTopPanel, text=lmbda, padx=25,background='#ff681f')
btnParam5 = Button(rTopPanel, text=delta, padx=25,background='#ff681f')
btnParam6 = Button(rTopPanel, text=ro, padx=25,background='#ff681f')
btnParam7 = Button(rTopPanel, text=kappa, padx=25,background='#ff681f')
btnParam8 = Button(rTopPanel, text=r1, padx=25,background='#ff681f')
btnParam9 = Button(rTopPanel, text=r2, padx=25,background='#ff681f')
btnParam10 = Button(rTopPanel, text=gamma, padx=25,background='#ff681f')
btnParam11 = Button(rTopPanel, text=d1, padx=25,background='#ff681f')
btnParam12 = Button(rTopPanel, text=d2, padx=25,background='#ff681f')

entryParam1 = Entry(rTopPanel)
entryParam2 = Entry(rTopPanel)
entryParam3 = Entry(rTopPanel)
entryParam4 = Entry(rTopPanel)
entryParam5 = Entry(rTopPanel)
entryParam6 = Entry(rTopPanel)
entryParam7 = Entry(rTopPanel)
entryParam8 = Entry(rTopPanel)
entryParam9 = Entry(rTopPanel)
entryParam10 = Entry(rTopPanel)
entryParam11 = Entry(rTopPanel)
entryParam12 = Entry(rTopPanel)

titleLabelTR.grid(row=0,columnspan=2,column=0)
btnParam1.grid(row=1,column=0)
btnParam2.grid(row=2,column=0)
btnParam3.grid(row=3,column=0)
btnParam4.grid(row=4,column=0)
btnParam5.grid(row=5,column=0)
btnParam6.grid(row=6,column=0)
btnParam7.grid(row=7,column=0)
btnParam8.grid(row=8,column=0)
btnParam9.grid(row=9,column=0)
btnParam10.grid(row=10,column=0)
btnParam11.grid(row=11,column=0)
btnParam12.grid(row=12,column=0)
entryParam1.grid(row=1,column=1)
entryParam2.grid(row=2,column=1)
entryParam3.grid(row=3,column=1)
entryParam4.grid(row=4,column=1)
entryParam5.grid(row=5,column=1)
entryParam6.grid(row=6,column=1)
entryParam7.grid(row=7,column=1)
entryParam8.grid(row=8,column=1)
entryParam9.grid(row=9,column=1)
entryParam10.grid(row=10,column=1)
entryParam11.grid(row=11,column=1)
entryParam12.grid(row=12,column=1)

# Panel Derecho Inferior
titleLabelBR = Label(rBottomPanel, text=solutionMethodTitle)
btnMetodo1 = Button(rBottomPanel, text=btnSolutionLabel1, padx=50, command=eulerAdelante,bg='green')
btnMetodo2 = Button(rBottomPanel, text=btnSolutionLabel2, padx=60, command=eulerAtras,background='#FFE5B4')
btnMetodo3 = Button(rBottomPanel, text=btnSolutionLabel3, padx=50, command=rungeKutta2,background='#FFE5B4')
btnMetodo4 = Button(rBottomPanel, text=btnSolutionLabel4, padx=50, command=rungeKutta4,background='#FFE5B4')

titleLabelBR.grid(row=0)
btnMetodo1.grid(row=1)
btnMetodo2.grid(row=2)
btnMetodo3.grid(row=3)
btnMetodo4.grid(row=4)


root.mainloop()