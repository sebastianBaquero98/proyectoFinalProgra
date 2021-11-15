from tkinter import*

# ---------- LABELS ----------
parameterTitle = 'Párametros'
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

# Panes principales
leftPane = Frame(root, background="#d5e8d4",width=650)
rightPane = Frame(root, background="#d46161",width=350)
leftPane.pack(side='left', fill='y')
rightPane.pack(side='right', fill='y')

# Pane Derecho
rTopPane = Frame(rightPane,background="#F39C12",padx=50,pady=85)
rBottomPane = Frame(rightPane,background="#FFA07A",width=350,padx=85,pady=95)
rTopPane.pack()
rBottomPane.pack()
#rTopPane.grid(row=0,column=0)
#rBottomPane.grid(row=1,column=0)

# Pane Derecho Superior
titleLabelTR = Label(rTopPane,text=parameterTitle)
btnParam1 = Button(rTopPane,text=beta,padx=25)
btnParam2 = Button(rTopPane,text=delta,padx=25)
btnParam3 = Button(rTopPane,text=fi,padx=25)
btnParam4 = Button(rTopPane,text=mu,padx=25)

entryParam1 = Entry(rTopPane)
entryParam2 = Entry(rTopPane)
entryParam3 = Entry(rTopPane)
entryParam4 = Entry(rTopPane)

titleLabelTR.grid(row=0,columnspan=2,column=0)
btnParam1.grid(row=1,column=0)
btnParam2.grid(row=2,column=0)
btnParam3.grid(row=3,column=0)
btnParam4.grid(row=4,column=0)
entryParam1.grid(row=1,column=1)
entryParam2.grid(row=2,column=1)
entryParam3.grid(row=3,column=1)
entryParam4.grid(row=4,column=1)

# Pane Derecho Inferior
titleLabelBR = Label(rBottomPane,text=solutionMethodTitle)
btnMetodo1 = Button(rBottomPane,text=btnSolutionLabel1,padx=50,command=eulerAdelante)
btnMetodo2 = Button(rBottomPane,text=btnSolutionLabel2,padx=60,command=eulerAtras)
btnMetodo3 = Button(rBottomPane,text=btnSolutionLabel3,padx=50,command=rungeKutta2)
btnMetodo4 = Button(rBottomPane,text=btnSolutionLabel4,padx=50,command=rungeKutta4)

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