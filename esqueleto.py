from tkinter import *
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy.integrate as inte

# ---------- LABELS ----------
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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

#Panel Izquierdo Superior
btnExportar = Button(lTopPanel , text=btnExtraer, padx=50, fg='white', background='#E13B3B', command=lambda: exportar())
btnImportar = Button(lTopPanel, text=btnImportar, padx=50, fg='white', background='#E13B3B', command=importar)
espacio = Label(lTopPanel,text=' ')

op1 = IntVar()
op2 = IntVar()
op3 = IntVar()
op4 = IntVar()
roundedbutton1 = Checkbutton(lTopPanel, text=St, variable=op1, onvalue=1, offvalue=0)
roundedbutton2 = Checkbutton(lTopPanel, text=Et, variable=op2, onvalue=1, offvalue=0)
roundedbutton3 = Checkbutton(lTopPanel, text=It, variable=op3, onvalue=1, offvalue=0)
roundedbutton4 = Checkbutton(lTopPanel, text=Lt, variable=op4, onvalue=1, offvalue=0)

btnExportar.grid(row=1,column=2)
btnImportar.grid(row=1,column=3)
espacio.grid(row=4,column=1)
roundedbutton1.grid(row=6,column=1)
roundedbutton2.grid(row=6,column=2)
roundedbutton3.grid(row=6,column=3)
roundedbutton4.grid(row=6,column=4)


#Panel Izquierdo Inferior
titleLabelBL = Label(lBottomPanel, text=tiempoSimulacion)
espacio = Label(lBottomPanel,text=' ')
tiempoLabel = Label(lBottomPanel,text = tiempo)

t1 = IntVar()
t2 = IntVar()
t3 = IntVar()

entryTiempo1 = Entry(lBottomPanel, textvariable=t1, borderwidth=2, relief="ridge")
entryTiempo2 = Entry(lBottomPanel, textvariable=t2, borderwidth=2, relief="ridge")
entryTiempo3 = Entry(lBottomPanel, textvariable=t3, borderwidth=2, relief="ridge")


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

p1 = DoubleVar()
p2 = DoubleVar()
p3 = DoubleVar()
p4 = DoubleVar()
p5 = DoubleVar()
p6 = DoubleVar()
p7 = DoubleVar()
p8 = DoubleVar()
p9 = DoubleVar()
p10 = DoubleVar()
p11 = DoubleVar()
p12 = DoubleVar()

entryParam1 =Entry(rTopPanel, textvariable=p1, borderwidth=2, relief="ridge")
entryParam2 = Entry(rTopPanel, textvariable=p2, borderwidth=2, relief="ridge")
entryParam3 = Entry(rTopPanel, textvariable=p3, borderwidth=2, relief="ridge")
entryParam4 = Entry(rTopPanel, textvariable=p4, borderwidth=2, relief="ridge")
entryParam5 = Entry(rTopPanel, textvariable=p5, borderwidth=2, relief="ridge")
entryParam6 = Entry(rTopPanel, textvariable=p6, borderwidth=2, relief="ridge")
entryParam7 = Entry(rTopPanel, textvariable=p7, borderwidth=2, relief="ridge")
entryParam8 = Entry(rTopPanel, textvariable=p8, borderwidth=2, relief="ridge")
entryParam9 = Entry(rTopPanel, textvariable=p9, borderwidth=2, relief="ridge")
entryParam10 = Entry(rTopPanel, textvariable=p10, borderwidth=2, relief="ridge")
entryParam11 = Entry(rTopPanel, textvariable=p11, borderwidth=2, relief="ridge")
entryParam12 = Entry(rTopPanel, textvariable=p12, borderwidth=2, relief="ridge")

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
btnMetodo1 = Button(rBottomPanel, text=btnSolutionLabel1, padx=50, command=lambda: grafica(1), background='#9C9EA2')
btnMetodo2 = Button(rBottomPanel, text=btnSolutionLabel2, padx=60, command=lambda: grafica(2), background='#9C9EA2')
btnMetodo3 = Button(rBottomPanel, text=btnSolutionLabel3, padx=42, command=lambda: grafica(3), background='#9C9EA2')
btnMetodo4 = Button(rBottomPanel, text=btnSolutionLabel4, padx=49, command=lambda: grafica(4), background='#9C9EA2')
btnMetodo5 = Button(rBottomPanel, text=btnSolutionLabel5, padx=49, command=lambda: grafica(5), background='#9C9EA2')
btnMetodo6 = Button(rBottomPanel, text=btnSolutionLabel6, padx=63, command=lambda: grafica(6), background='#9C9EA2')

titleLabelBR.grid(row=0)
btnMetodo1.grid(row=1)
btnMetodo2.grid(row=2)
btnMetodo3.grid(row=3)
btnMetodo4.grid(row=4)
btnMetodo5.grid(row=5)
btnMetodo6.grid(row=6)

#grafica
def grafica(ms):

    if(ms == 1):
        solucionesF = eulerAdelante(float(entryParam1.get()),float(entryParam2.get()),float(entryParam3.get()),float(entryParam4.get()),float(entryParam5.get()),float(entryParam6.get()),float(entryParam7.get()),float(entryParam8.get()),float(entryParam9.get()),float(entryParam10.get()),float(entryParam11.get()),float(entryParam12.get()),float(entryTiempo1.get()),float(entryTiempo2.get()))
        solS = solucionesF[1]
        solI = solucionesF[2]
        solE = solucionesF[3]
        solL = solucionesF[4]
        tit = "Método de Solución Euler Hacia Adelante"
    elif (ms == 2):
        solucionesB = eulerAtras(float(entryParam1.get()),float(entryParam2.get()),float(entryParam3.get()),float(entryParam4.get()),float(entryParam5.get()),float(entryParam6.get()),float(entryParam7.get()),float(entryParam8.get()),float(entryParam9.get()),float(entryParam10.get()),float(entryParam11.get()),float(entryParam12.get()),float(entryTiempo1.get()),float(entryTiempo2.get()))
        solS = solucionesB[1]
        solI = solucionesB[2]
        solE = solucionesB[3]
        solL = solucionesB[4]
        tit = "Método de Solución Euler Hacia Atrás"
    elif (ms == 3):
        solucionesM = eulerModificado(float(entryParam1.get()),float(entryParam2.get()),float(entryParam3.get()),float(entryParam4.get()),float(entryParam5.get()),float(entryParam6.get()),float(entryParam7.get()),float(entryParam8.get()),float(entryParam9.get()),float(entryParam10.get()),float(entryParam11.get()),float(entryParam12.get()),float(entryTiempo1.get()),float(entryTiempo2.get()))
        solS = solucionesM[1]
        solI = solucionesM[2]
        solE = solucionesM[3]
        solL = solucionesM[4]
        tit = "Método de Solución Euler Modificado"
    elif (ms == 4):
        solucionesRK2 = rungeKutta2(float(entryParam1.get()),float(entryParam2.get()),float(entryParam3.get()),float(entryParam4.get()),float(entryParam5.get()),float(entryParam6.get()),float(entryParam7.get()),float(entryParam8.get()),float(entryParam9.get()),float(entryParam10.get()),float(entryParam11.get()),float(entryParam12.get()),float(entryTiempo1.get()),float(entryTiempo2.get()))
        solS = solucionesRK2[1]
        solI = solucionesRK2[2]
        solE = solucionesRK2[3]
        solL = solucionesRK2[4]
        tit = "Método de Solución Runge-Kutta 2"
    elif (ms == 5):
        solucionesRK4 = rungeKutta4(float(entryParam1.get()),float(entryParam2.get()),float(entryParam3.get()),float(entryParam4.get()),float(entryParam5.get()),float(entryParam6.get()),float(entryParam7.get()),float(entryParam8.get()),float(entryParam9.get()),float(entryParam10.get()),float(entryParam11.get()),float(entryParam12.get()),float(entryTiempo1.get()),float(entryTiempo2.get()))
        solS = solucionesRK4[1]
        solI = solucionesRK4[2]
        solE = solucionesRK4[3]
        solL = solucionesRK4[4]
        tit = "Método de Solución Runge-Kutta 4"
    elif (ms == 6):
        solucionesSolv = solve_ivp(float(entryTiempo1.get()), float(entryTiempo2.get()))
        solS = solucionesSolv[1]
        solI = solucionesSolv[2]
        solE = solucionesSolv[3]
        solL = solucionesSolv[4]
        tit = "Método de Solución solve.ivp"

    h = 0.5
    T = np.arange(float(entryTiempo1.get()), float(entryTiempo2.get()) + h, h)
    fig = plt.Figure(figsize=(9, 6), dpi=80)
    fg = fig.add_subplot(111)

    if(op1.get()==1):
        fg.plot(T, solS, 'b')
    if (op2.get() == 1):
        fg.plot(T, solI, 'r')
    if (op3.get() == 1):
        fg.plot(T, solE, 'g')
    if (op4.get() == 1):
        fg.plot(T, solL, 'm')

    fg.grid()
    fg.set_xlabel("Tiempo en años")
    fg.set_ylabel("Poblaciones")
    fg.set_title(tit)
    plt.show()
    plt.close()
    fra = Frame(lTopPanel)
    fra.config(width=700, height=450)
    fra.grid(row=3, columnspan=6, column=0)
    Plot = FigureCanvasTkAgg(fig, master=fra)
    Plot.draw()
    Plot.get_tk_widget().find_all()
    Plot.get_tk_widget().pack()

# Parametros - ESTO LO INGRESA EL USUARIO
h = 0.5

# ----------- MÉTODOS ---------

def dS(lmbda,beta,S,delta,I,L,mu):
    return lmbda - (beta*S*(I + delta*L)) - mu*S

def dE(beta,ro,S,I,delta,L,r_2,mu,kappa,r_1,E):
    return (beta*(1 - ro)*S*(I + delta*L)) + (r_2*I) - (mu + kappa*(1 - r_1))*E

def dI(beta,ro,S,I,delta,L,kappa,r_1,E,gamma,mu,d_1,fi,r_2):
    return (beta*ro*S*(I + delta*L)) + (kappa*(1 - r_1)*E) + gamma*L - (mu + d_1 + fi*(1 - r_2) + r_2)*I

def dL(fi,r_2,I,mu,d_2,gamma,L):
    return (fi*(1 - r_2)*I) - (mu + d_2 + gamma)*L

def FEulerBackRoot(vI, y1t1, y2t1, y3t1, y4t1,beta,fi,mu,lmbda,delta,ro,kappa,r1,r2,gamma,d1,d2):
    h=0.5
    return [y1t1 + h * dS(lmbda,beta,vI[0],delta,vI[1],vI[3],mu) - vI[0],
            y2t1 + h * dI(beta,ro,vI[0],vI[1],delta,vI[3],kappa,r1,vI[2],gamma,mu,d1,fi,r2) - vI[1],
            y3t1 + h * dE(beta,ro,vI[0],vI[1],delta,vI[3],r2,mu,kappa,r1,vI[2]) - vI[2],
            y4t1 + h * dL(fi,r2,vI[2],mu,d2,gamma,vI[3]) - vI[3]]

def FEulerModRoot(vI, y1t1, y2t1, y3t1, y4t1, beta,fi,mu,lmbda,delta,ro,kappa,r1,r2,gamma,d1,d2):
    h=0.5
    return [y1t1 + (h / 2.0) * (dS(lmbda,beta,vI[0],delta,vI[1],vI[3],mu) + dS(lmbda,beta,y1t1,delta,y2t1,y4t1,mu)) - vI[0],
            y2t1 + (h / 2.0) * (dI(beta,ro,vI[0],vI[1],delta,vI[3],kappa,r1,vI[2],gamma,mu,d1,fi,r2) + dI(beta,ro,y1t1,y2t1,delta,y4t1,kappa,r1,y3t1,gamma,mu,d1,fi,r2)) - vI[1],
            y3t1 + (h / 2.0) * (dE(beta,ro,vI[0],vI[1],delta,vI[3],r2,mu,kappa,r1,vI[2]) + dE(beta,ro,y1t1,y2t1,delta,y4t1,r2,mu,kappa,r1,y3t1)) - vI[2],
            y4t1 + (h / 2.0) * (dL(fi,r2,vI[2],mu,d2,gamma,vI[3]) + dL(fi,r2,y3t1,mu,d2,gamma,y4t1)) - vI[3]]

def sistemaEcuaciones(x,vI):
    beta = 0.025
    fi = 0.02
    mu = 0.0101
    lmbda = 2
    delta = 1
    ro = 0.3
    kappa = 0.005
    r1= 0
    r2= 0.8182
    gamma = 0.01
    d1= 0.022722
    d2= 0.20

    return [dS(lmbda,beta,vI[0],delta,vI[1],vI[3],mu),dI(beta,ro,vI[0],vI[1],delta,vI[3],kappa,r1,vI[2],gamma,mu,d1,fi,r2),dE(beta,ro,vI[0],vI[1],delta,vI[3],r2,mu,kappa,r1,vI[2]),dL(fi,r2,vI[2],mu,d2,gamma,vI[3])]



def eulerAdelante(beta,fi,mu,lmbda,delta,ro,kappa,r1,r2,gamma,d1,d2,t_0,t_f):
    h=0.5
    s_0 = 198
    e_0 = 1
    i_0 = 0
    l_0 = 0
    T = np.arange(t_0,t_f+h,h)

    # Paso 5
    # Contiene los valores estimados de la solucion
    sEulerFor = np.zeros(len(T))
    eEulerFor = np.zeros(len(T))
    iEulerFor = np.zeros(len(T))
    lEulerFor = np.zeros(len(T))
    # Ingresomos valor inicial
    sEulerFor[0] = s_0
    eEulerFor[0] = e_0
    iEulerFor[0] = i_0
    lEulerFor[0] = l_0

    for i in range(1,len(T)):
        sEulerFor[i] = sEulerFor[i-1] + h*dS(lmbda,beta,sEulerFor[i-1],delta,iEulerFor[i-1],lEulerFor[i-1],mu)
        iEulerFor[i] = iEulerFor[i-1] + h*dI(beta,ro,sEulerFor[i-1],iEulerFor[i-1],delta,lEulerFor[i-1],kappa,r1,eEulerFor[i-1],gamma,mu,d1,fi,r2)
        eEulerFor[i] = eEulerFor[i-1] + h*dE(beta,ro,sEulerFor[i-1],iEulerFor[i-1],delta,lEulerFor[i-1],r2,mu,kappa,r1,eEulerFor[i-1])
        lEulerFor[i] = lEulerFor[i-1] + h*dL(fi,r2,iEulerFor[i-1],mu,d2,gamma,lEulerFor[i-1])

    return (T,sEulerFor,iEulerFor,eEulerFor,lEulerFor)

def eulerAtras(beta,fi,mu,lmbda,delta,ro,kappa,r1,r2,gamma,d1,d2,t_0,t_f):
    h=0.5
    s_0 = 198
    e_0 = 1
    i_0 = 0
    l_0 = 0
    T = np.arange(t_0,t_f+h,h)
    sEulerB = np.zeros(len(T))
    eEulerB = np.zeros(len(T))
    iEulerB = np.zeros(len(T))
    lEulerB = np.zeros(len(T))
    sEulerB[0] = s_0
    eEulerB[0] = e_0
    iEulerB[0] = i_0
    lEulerB[0] = l_0

    for iter in range(1, len(T)):
        SolBack = opt.fsolve(FEulerBackRoot,
                            np.array([sEulerB[iter - 1],
                                    iEulerB[iter - 1],
                                    eEulerB[iter - 1],
                                    lEulerB[iter - 1]]),
                            (sEulerB[iter - 1],
                            iEulerB[iter - 1],
                            eEulerB[iter - 1],
                            lEulerB[iter - 1],
                            beta,
                            fi,
                            mu,
                            lmbda,
                            delta,
                            ro,
                            kappa,r1,r2,gamma,d1,d2),
                            xtol = 10 ** -15)

        sEulerB[iter] = SolBack[0]
        iEulerB[iter] = SolBack[1]
        eEulerB[iter] = SolBack[2]
        lEulerB[iter] = SolBack[3]

    return (T,sEulerB,iEulerB,eEulerB,lEulerB)

def eulerModificado(beta,fi,mu,lmbda,delta,ro,kappa,r1,r2,gamma,d1,d2,t_0,t_f):
   h = 0.5
   s_0 = 198
   e_0 = 1
   i_0 = 0
   l_0 = 0
   T = np.arange(t_0,t_f+h,h)
   sEulerM = np.zeros(len(T))
   eEulerM = np.zeros(len(T))
   iEulerM = np.zeros(len(T))
   lEulerM = np.zeros(len(T))
   sEulerM[0] = s_0
   eEulerM[0] = e_0
   iEulerM[0] = i_0
   lEulerM[0] = l_0


   for iter in range(1, len(T)):
      SolMod = opt.fsolve(FEulerModRoot,  # Función
                           np.array([sEulerM[iter - 1],  # x0
                                    iEulerM[iter - 1],
                                    eEulerM[iter - 1],
                                    lEulerM[iter - 1]]),
                           (sEulerM[iter - 1],  # Parámetros de función
                           iEulerM[iter - 1],
                           eEulerM[iter - 1],
                           lEulerM[iter - 1],
                           beta,
                           fi,
                           mu,
                           lmbda,
                           delta,
                           ro,
                           kappa,r1,r2,gamma,d1,d2),
                           xtol = 10 ** -15)  # Tolerancia

      sEulerM[iter] = SolMod[0]
      iEulerM[iter] = SolMod[1]
      eEulerM[iter] = SolMod[2]
      lEulerM[iter] = SolMod[3]

   return (T,sEulerM,iEulerM,eEulerM,lEulerM)


def rungeKutta2(beta,fi,mu,lmbda,delta,ro,kappa,r1,r2,gamma,d1,d2,t_0,t_f):
    s_0 = 198
    e_0 = 1
    i_0 = 0
    l_0 = 0
    T = np.arange(t_0,t_f+h,h)
    sRK2 = np.zeros(len(T))
    iRK2 = np.zeros(len(T))
    eRK2 = np.zeros(len(T))
    lRK2 = np.zeros(len(T))
    sRK2[0] = s_0
    iRK2[0] = i_0
    eRK2[0] = e_0
    lRK2[0] = l_0


    for iter in range(1, len(T)):
        k11 = dS(lmbda,beta,sRK2[iter - 1],delta,iRK2[iter-1],lRK2[iter-1],mu)
        k21 = dI(beta,ro,sRK2[iter - 1],iRK2[iter-1],delta,lRK2[iter-1],kappa,r1,eRK2[iter-1],gamma,mu,d1,fi,r2)
        k31 = dE(beta,ro,sRK2[iter - 1],iRK2[iter-1],delta,lRK2[iter-1],r2,mu,kappa,r1,eRK2[iter-1])
        k41 = dL(fi,r2,eRK2[iter-1],mu,d2,gamma,lRK2[iter-1])


        k12 = dS(lmbda,beta,sRK2[iter - 1] + k11 * h,delta,iRK2[iter-1]+ k21 * h,lRK2[iter-1]+ k41 * h,mu)
        k22 = dI(beta,ro,sRK2[iter - 1]+ k11 * h,iRK2[iter-1]+ k21 * h,delta,lRK2[iter-1]+ k41 * h,kappa,r1,eRK2[iter-1]+ k31 * h,gamma,mu,d1,fi,r2)
        k32 = dE(beta,ro,sRK2[iter - 1]+ k11 * h,iRK2[iter-1]+ k21 * h,delta,lRK2[iter-1]+ k41 * h,r2,mu,kappa,r1,eRK2[iter-1]+ k31 * h)
        k42 = dL(fi,r2,eRK2[iter-1]+ k31 * h,mu,d2,gamma,lRK2[iter-1]+ k41 * h)

        sRK2[iter] = sRK2[iter - 1] + ((h / 2.0) * (k11 + k12))
        iRK2[iter] = iRK2[iter - 1] + ((h / 2.0) * (k21 + k22))
        eRK2[iter] = eRK2[iter - 1] + ((h / 2.0) * (k31 + k32))
        lRK2[iter] = lRK2[iter - 1] + ((h / 2.0) * (k41 + k42))
    return (T,sRK2,iRK2,eRK2,lRK2)

def rungeKutta4(beta,fi,mu,lmbda,delta,ro,kappa,r1,r2,gamma,d1,d2,t_0,t_f):
    s_0 = 198
    e_0 = 1
    i_0 = 0
    l_0 = 0
    T = np.arange(t_0,t_f+h,h)
    sRK4 = np.zeros(len(T))
    iRK4 = np.zeros(len(T))
    eRK4 = np.zeros(len(T))
    lRK4 = np.zeros(len(T))
    sRK4[0] = s_0
    iRK4[0] = i_0
    eRK4[0] = e_0
    lRK4[0] = l_0

    for iter in range(1, len(T)):
        k11 = dS(lmbda,beta,sRK4[iter - 1],delta,iRK4[iter-1],lRK4[iter-1],mu)
        k21 = dI(beta,ro,sRK4[iter - 1],iRK4[iter-1],delta,lRK4[iter-1],kappa,r1,eRK4[iter-1],gamma,mu,d1,fi,r2)
        k31 = dE(beta,ro,sRK4[iter - 1],iRK4[iter-1],delta,lRK4[iter-1],r2,mu,kappa,r1,eRK4[iter-1])
        k41 = dL(fi,r2,eRK4[iter-1],mu,d2,gamma,lRK4[iter-1])

        k12 = dS(lmbda,beta,sRK4[iter - 1]+ (0.5 * k11 * h),delta,iRK4[iter-1]+ (0.5 * k21 * h),lRK4[iter-1]+ (0.5 * k41 * h),mu)
        k22 = dI(beta,ro,sRK4[iter - 1]+ (0.5 * k11 * h),iRK4[iter-1]+ (0.5 * k21 * h),delta,lRK4[iter-1]+ (0.5 * k41 * h),kappa,r1,eRK4[iter-1]+ (0.5 * k31 * h),gamma,mu,d1,fi,r2)
        k32 = dE(beta,ro,sRK4[iter - 1]+ (0.5 * k11 * h),iRK4[iter-1]+ (0.5 * k21 * h),delta,lRK4[iter-1]+ (0.5 * k41 * h),r2,mu,kappa,r1,eRK4[iter-1]+ (0.5 * k31 * h))
        k42 = dL(fi,r2,eRK4[iter-1]+ (0.5 * k31 * h),mu,d2,gamma,lRK4[iter-1]+ (0.5 * k41 * h))


        k13 = dS(lmbda,beta,sRK4[iter - 1]+ 0.5 * k12 * h,delta,iRK4[iter-1]+ 0.5 * k22 * h,lRK4[iter-1]+ 0.5 * k42 * h,mu)
        k23 = dI(beta,ro,sRK4[iter - 1]+ (0.5 * k12 * h),iRK4[iter-1]+ (0.5 * k22 * h),delta,lRK4[iter-1]+ (0.5 * k42 * h),kappa,r1,eRK4[iter-1]+ (0.5 * k32 * h),gamma,mu,d1,fi,r2)
        k33 = dE(beta,ro,sRK4[iter - 1]+ (0.5 * k12 * h),iRK4[iter-1]+ (0.5 * k22 * h),delta,lRK4[iter-1]+ (0.5 * k42 * h),r2,mu,kappa,r1,eRK4[iter-1]+ (0.5 * k32 * h))
        k43 = dL(fi,r2,eRK4[iter-1]+ (0.5 * k32 * h),mu,d2,gamma,lRK4[iter-1]+ (0.5 * k42 * h))


        k14 = dS(lmbda,beta,sRK4[iter - 1] + k13 * h,delta,iRK4[iter-1] + k23 * h,lRK4[iter-1] + k43 * h,mu)
        k24 = dI(beta,ro,sRK4[iter - 1]+ k13 * h,iRK4[iter-1]+ k23 * h,delta,lRK4[iter-1]+ k43 * h,kappa,r1,eRK4[iter-1]+ k33 * h,gamma,mu,d1,fi,r2)
        k34 = dE(beta,ro,sRK4[iter - 1]+ k13 * h,iRK4[iter-1]+ k23 * h,delta,lRK4[iter-1]+ k43 * h,r2,mu,kappa,r1,eRK4[iter-1]+ k33 * h)
        k44 = dL(fi,r2,eRK4[iter-1]+ k33 * h,mu,d2,gamma,lRK4[iter-1]+ k43)


        sRK4[iter] = sRK4[iter - 1] + (h / 6) * (k11 + 2 * k12 + 2 * k13 + k14)
        iRK4[iter] = iRK4[iter - 1] + (h / 6) * (k21 + 2 * k22 + 2 * k23 + k24)
        eRK4[iter] = eRK4[iter - 1] + (h / 6) * (k31 + 2 * k32 + 2 * k33 + k34)
        lRK4[iter] = lRK4[iter - 1] + (h / 6) * (k41 + 2 * k42 + 2 * k43 + k44)

    return (T,sRK4,iRK4,eRK4,lRK4)


def solve_ivp(t_0,t_f):
    s_0 = 198
    e_0 = 1
    i_0 = 0
    l_0 = 0
    T = np.arange(t_0, t_f + h, h)
    SolRK45 = inte.solve_ivp(sistemaEcuaciones, [t_0, t_f], [s_0,e_0,i_0,l_0],t_eval=T,method='RK45')
    return (T,SolRK45.y[0],SolRK45.y[1],SolRK45.y[2],SolRK45.y[3])

root.mainloop()