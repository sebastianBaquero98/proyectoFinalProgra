from tkinter import*

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
delta = u'\u0394'


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
root.geometry("1000x600")


# Paneles principales
leftPanel = Frame(root, background="#d5e8d4",width=650)
rightPanel = Frame(root, background="#d46161",width=350)
leftPanel.pack(expand='true', side='left', fill='y')
rightPanel.pack(side='right', fill='y')

#Panel Izquierdo
lTopPanel = Frame(leftPanel,background="#F39C12",width=650,padx=50,pady=85)
lBottomPanel = Frame(leftPanel,background="#FFA07A",width=650,padx=85,pady=95)
lTopPanel.pack()
lBottomPanel.pack()


#Panel Izquierdo Superior
btnExportar = Button(lTopPanel, background= "#D44848", text=btnExtraer, padx=35)
btnImportar = Button(lTopPanel, background= "#D44848", text=btnImportar, padx=35)
img = PhotoImage(file="gráfica.PNG")
imgLabel = Label(lTopPanel, image = img, width=350, height=200)
SLabel = Label(lTopPanel,text=St)
ELabel = Label(lTopPanel,text=Et)
ILabel = Label(lTopPanel, text=It)
LLabel = Label(lTopPanel, text=Lt)
espacio = Label(lTopPanel,text=' ',background="#F39C12")

btnExportar.grid(row=1,column=2)
btnImportar.grid(row=1,column=3)
imgLabel.grid(row=3,columnspan=6, column=0)
espacio.grid(row=4,column=1)
SLabel.grid(row=6, column=1)
ELabel.grid(row=6,column=2)
ILabel.grid(row=6,column=3)
LLabel.grid(row=6,column=4)


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
rTopPanel = Frame(rightPanel, background="#F39C12", padx=50, pady=85)
rBottomPanel = Frame(rightPanel, background="#FFA07A", width=350, padx=85, pady=95)
rTopPanel.pack()
rBottomPanel.pack()
#rTopPane.grid(row=0,column=0)
#rBottomPane.grid(row=1,column=0)

# Panel Derecho Superior
titleLabelTR = Label(rTopPanel, text=parameterTitle)
btnParam1 = Button(rTopPanel, text=beta, padx=25)
btnParam2 = Button(rTopPanel, text=delta, padx=25)
btnParam3 = Button(rTopPanel, text=fi, padx=25)
btnParam4 = Button(rTopPanel, text=mu, padx=25)

entryParam1 = Entry(rTopPanel)
entryParam2 = Entry(rTopPanel)
entryParam3 = Entry(rTopPanel)
entryParam4 = Entry(rTopPanel)

titleLabelTR.grid(row=0,columnspan=2,column=0)
btnParam1.grid(row=1,column=0)
btnParam2.grid(row=2,column=0)
btnParam3.grid(row=3,column=0)
btnParam4.grid(row=4,column=0)
entryParam1.grid(row=1,column=1)
entryParam2.grid(row=2,column=1)
entryParam3.grid(row=3,column=1)
entryParam4.grid(row=4,column=1)

# Panel Derecho Inferior
titleLabelBR = Label(rBottomPanel, text=solutionMethodTitle)
btnMetodo1 = Button(rBottomPanel, text=btnSolutionLabel1, padx=50, command=eulerAdelante)
btnMetodo2 = Button(rBottomPanel, text=btnSolutionLabel2, padx=60, command=eulerAtras)
btnMetodo3 = Button(rBottomPanel, text=btnSolutionLabel3, padx=50, command=rungeKutta2)
btnMetodo4 = Button(rBottomPanel, text=btnSolutionLabel4, padx=50, command=rungeKutta4)

titleLabelBR.grid(row=0)
btnMetodo1.grid(row=1)
btnMetodo2.grid(row=2)
btnMetodo3.grid(row=3)
btnMetodo4.grid(row=4)


root.mainloop()


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