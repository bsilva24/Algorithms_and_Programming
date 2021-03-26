from time import sleep
import webbrowser
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pickle
import os.path
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import sys
from PIL import Image
from PIL import ImageTk

def aplicacao():
    window = Tk()
    window.title('STARTLIS - STARTUPS LISBOA')
    window.resizable(False, False)
    window.geometry('600x450+584+230')
    window.iconbitmap(r'./Files/Image/trolito.ico')
    
    labelwel = Label(window)
    labelwel.place(relx=0.25, rely=0.067, height=35, width=305)
    labelwel.configure(background="#0082ba", foreground="white", relief='ridge', text='''Seja bem-vindo!''')
    
    '''img1 = PhotoImage(file="./Files/Image/img1.png")
    labelimg = Label(window)
    labelimg.place(relx=0.317, rely=0.211, height=145, width=225)
    labelimg.configure(relief='ridge', image=img1 )'''
    
    frame1 = Frame(window)
    frame1.place(relx=0.25, rely=0.667, relheight=0.190, relwidth=0.508)
    frame1.configure(relief='groove', borderwidth="2", width=305)
    
    buttonviz = Button(frame1, command=menuLista)
    buttonviz.place(relx=0.066, rely=0.111, height=24, width=267)
    buttonviz.configure(text='''Visualizar Startups''', pady="0", width=267, background="#0082ba", foreground="white")
                        
    buttonclose = Button(frame1, command=window.destroy)
    buttonclose.place(relx=0.066, rely=0.600, height=24, width=267)
    buttonclose.configure(text='''Fechar Programa''', pady="0", width=267, background="#0082ba", foreground="white")
    
    labelopt = Label(window)
    labelopt.place(relx=0.25, rely=0.6, height=31, width=109)
    labelopt.configure(relief='groove', text='''Menu de Opções:''', foreground="white", background="#0082ba")
                    
    topmenu(window)
    
    window.mainloop()

def creditos():    
    messagebox.showinfo('Créditos',"""  
    Elaborado por:                         
                                            
     - {:20s}   -   Nº 30003769       
     - {:20s}   -   Nº 30003099       
     - {:20s}   -   Nº 30003410       
     - {:20s}   -   Nº 30003067       
                                            
            Algoritmia e Programação        
     @UAL - Universidade Autónoma de Lisboa     
    """.format('Bruno Silva', 'Daniel Silvestre', 'Rafael Rocha', 'Ricardo Oliveira'))
        
def SerializarListaPkl(empresas): #Função de serialização dos dados em ficheiro binário
    with open('empresas_bin.pkl','wb') as f: 
        pickle.dump(empresas,f)
    f.close()

def DesserializarListaPkl(empresas): #Função de desserialização dos dados em ficheiro binário
    with open('empresas_bin.pkl','rb') as f:
        empresasCarregadas = pickle.load(f)

    for i in range(len(empresasCarregadas)):
        empresas.append(empresasCarregadas[i])
    f.close()
    
def guardarBin():
    SerializarListaPkl(empresas)
    messagebox.showinfo("Guardar Binário", "Ficheiro guardado com sucesso!")
    
def GuardarFicheiroTexto(empresas): #Função de guardar dados da matriz em ficheiro de texto
    ficheirotexto = open("Ficheiro-Texto.txt", "w")
    ficheirotexto.write("+-----------------------------------------------------------+\n")
    ficheirotexto.write("       STARTUPs 2018 – 10 melhores em Lisboa e outras")
    ficheirotexto.write("\n+-----------------------------------------------------------+")
    
    for i in range(len(empresas)):
        ficheirotexto.write("\n{}, {}, {}\n".format(empresas[i][0], empresas[i][1], empresas[i][2]))
    ficheirotexto.close()

def guardarTxt():
    GuardarFicheiroTexto(empresas)
    messagebox.showinfo("Guardar Ficheiro de Texto", "Ficheiro guardado com sucesso!")
    
def abrirTxt():
    if os.path.isfile('./Ficheiro-Texto.txt') is True:
        nometxt = "Ficheiro-Texto.txt"
        os.startfile(nometxt)
    else:
        messagebox.showerror("Erro", "Não existe nenhum ficheiro guardado ainda.\nPor favor guarde primeiro.")
    
def topmenu(win):
    menu = Menu(win)
    menu['bg'] = "#58ACFA"
    win.config(menu=menu)
   
    filemenu = Menu(menu)
    
    abrirmenu = Menu(filemenu, name="abrir")
    filemenu.add_command(label="Abrir ficheiro de texto", command=abrirTxt)
    
    guardarmenu = Menu(filemenu, name="guardar")
    guardarmenu.add_command(label="Ficheiro binário (.pkl)", command=guardarBin)
    guardarmenu.add_command(label="Ficheiro texto (.txt)", command=guardarTxt)
    filemenu.add_cascade(label="Guardar", menu=guardarmenu)
    menu.add_cascade(label="Ficheiro", menu=filemenu)

    aboutmenu = Menu(menu)
    
    aboutmenu.add_command(label="Mostrar créditos", command=creditos)
    menu.add_cascade(label="Sobre", menu=aboutmenu)

def criarEmpresa(Nome, Investimento, Website): #Função de adicionar dados a uma lista independente
    emp = [Nome, Investimento, Website]
    return emp 

empresas=[]

if os.path.isfile('./empresas_bin.pkl') is False: #inicio ondição de verificação da existencia de um ficheiro binário com os dados das startups
        empresas.append(criarEmpresa("Prodsmart", 1447247.82, "www.prodsmart.com"))
        empresas.append(criarEmpresa("James", 3420767.57, "www.james.finance"))
        empresas.append(criarEmpresa("Talkdesk", 21489437.28, "www.talkdesk.com"))
        empresas.append(criarEmpresa("Codacy", 5876703.26, "www.codacy.com"))
        empresas.append(criarEmpresa("Veniam", 23594525.02, "www.veniam.com"))
        empresas.append(criarEmpresa("Sensei", 500000, "www.sensei.tech"))
        empresas.append(criarEmpresa("Definedcrowd", 964831.88, "www.definedcrowd.com"))
        empresas.append(criarEmpresa("Heptasense", 00000.00, "www.heptasense.com"))
        empresas.append(criarEmpresa("Aptoide", 1514575, "www.aptoide.com"))
        empresas.append(criarEmpresa("Probe.ly", 1055000, "www.probely.com"))
else:
        DesserializarListaPkl(empresas)

def menuLista():
    
    window9 = Toplevel()
    window9.title('Listagem de StartUps')
    window9.geometry("600x450+517+216")
    frame1 = Frame(window9)
    frame1.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=0.508)
    frame1.configure(relief='raised', borderwidth="2", width=305)
    
    labeltitle = Label(frame1)
    labeltitle.place(relx=0.213, rely=0.088, height=31, width=159)
    labeltitle.configure(relief="ridge", text="""Listagem de Startups:""", fg='white', background="#0082ba")
    
    t = Text(frame1)
        
    for i in range(len(empresas)):
        lista = " {:14s} [{}]".format(empresas[i][0], i+1) + "\n"
        t.insert(END, lista)
    t.place(relx=0.197, rely=0.176, relheight=0.624, relwidth=0.56)
    t.configure(width=174, state='disabled')
    
    frame2 = Frame(window9)
    frame2.place(relx=0.5, rely=0.0, relheight=1.011, relwidth=0.508)
    frame2.configure(relief='raised', borderwidth="2", width=305)
    
    frameopt = Frame(frame2)
    frameopt.place(relx=0.016, rely=0.418, relheight=0.385, relwidth=0.934)
    frameopt.configure(relief='groove', borderwidth="2", width=285)
    
    frame21 = Frame(frameopt)
    frame21.place(relx=0.035, rely=0.086, relheight=0.194, relwidth=0.902)
    frame21.configure(borderwidth="2", width=257, relief='raised')
    
    label1 = Label(frame21)
    label1.place(relx=0.0, rely=-0.020, height=30, width=63)
    label1.configure(borderwidth="2", relief='raised', text='''Nº Startup:''')
    
    global spinbox1
    spinbox1 = Spinbox(frame21, from_=1.0, to=len(empresas))
    spinbox1.place(relx=0.272, rely=0.22, relheight=0.559, relwidth=0.097)
    
    button1 = Button(frame21)
    button1.place(relx=0.389, rely=-0.020, height=30, width=153)
    button1.configure(pady="0")
    button1.configure(text='Abrir Selecionado', command=menuStartupSel)
    
    button2 = Button(frameopt)
    button2.place(relx=0.035, rely=0.543, height=24, width=257)
    button2.configure(pady="0", text='Visualizar Gráfico Linear de Investimentos', command=mostrarGrafLin)
    
    button3 = Button(frameopt)
    button3.place(relx=0.035, rely=0.743, height=24, width=257)
    button3.configure(pady="0", text='Visualizar Gráfico Circular de Investimentos', command=grafStartupCircular)
    
    button4 = Button(frameopt)
    button4.place(relx=0.035, rely=0.343, height=24, width=257)
    button4.configure(pady="0", text='Adicionar nova Startup', command=addEmp)
    
    img1 = ImageTk.PhotoImage(file="./Files/Image/img1.png")
    labelimg = Label(frame2, image=img1)
    labelimg.place(relx=0.131, rely=0.085, height=111, width=214)
    labelimg.configure(relief="ridge", width=199)
    labelimg.image=img1
    
    labeltitleopt = Label(frame2)
    labeltitleopt.place(relx=1, rely=0.363, height=31, width=250)
    labeltitleopt.configure(background="#0082ba", fg='white', text='''Menu de Opções:''', relief='groove', width=150)
    
    window9.mainloop()
    
def currency(x, pos): #Função de conversão de um valor em euros inteiro para milhar e milhão abreviado
    if x >= 1e6:
        s = '€{:1.1f}M'.format(x*1e-6)
    else:
        s = '€{:1.0f}K'.format(x*1e-3)
    return s

def mostrarGrafLin():
    nome = []
    invest = []
    formatter = FuncFormatter(currency)
    for i in range(len(empresas)):
        nome.append(empresas[i][0])
        invest.append(empresas[i][1])
        
    window5 = Tk()
    window5.resizable(False, False)
    window5.title('Gráfico de Barras Horizontal')
    Data1 = {'StartUps': nome,
            'Investimento': invest}
    
    df1 = DataFrame(Data1, columns= ['StartUps', 'Investimento'])
    df1 = df1[['StartUps', 'Investimento']].groupby('StartUps').sum()
    
    figure1 = plt.Figure(figsize=(10.5,5), dpi=100)
    ax1 = figure1.add_subplot(111)
    ax1.set_title('Investimento Total das StartUps')
    bar1 = FigureCanvasTkAgg(figure1, window5)
    bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
    ax1.set_xticks([0, 1000e3, 2500e3, 5000e3, 7500e3, 10000e3, 12500e3, 15000e3, 17500e3, 20000e3, 22500e3, 25000e3])
    ax1.xaxis.set_major_formatter(formatter)
    df1.plot(kind='barh', legend=False, ax=ax1)
    
    window5.mainloop()
    
def grafStartupCircular():
    startups = []
    sizes = []
    explode = []
    for i in range(0, len(empresas)):
        startups.append(empresas[i][0])
        sizes.append(empresas[i][1])
        explode.append(0.11)
     
    window6 = Tk()
    window6.resizable(False, False)
    window6.title('Gráfico Circular - Pie Chart')
    window6.geometry('700x650')
    Data1 = {'StartUps': startups,
            'Investimento': sizes}
    
    df1 = DataFrame(Data1, columns= ['StartUps', 'Investimento'])
    df1 = df1[['StartUps', 'Investimento']].groupby('StartUps').sum()
    
    figure1 = plt.Figure(figsize=(7,7), dpi=100)
    ax1 = figure1.add_subplot(111)
    ax1.set_title('Investimento Total das StartUps')
    ax1.pie(sizes, explode=explode, autopct='%1.1f%%',
            shadow=True, startangle=-20)
    ax1.legend(startups, title='Startups', loc='best', bbox_to_anchor=(0.13,0.38,0,0))
    bar1 = FigureCanvasTkAgg(figure1, window6)
    bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
     
    window6.mainloop()
    
def menuStartupSel():
    window7 = Toplevel()
    window7.title('Informação da StartUp')
    window7.geometry("600x450+517+216")
    window7.resizable(False, False)
    
    frame1 = Frame(window7)
    frame1.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=0.508)
    frame1.configure(width=305, relief='raised', borderwidth="2")
    
    frame2 = Frame(window7)
    frame2.place(relx=0.5, rely=0.0, relheight=1.011, relwidth=0.508)
    frame2.configure(width=305, relief='raised', borderwidth="2")
    
    frameopt = Frame(frame2)
    frameopt.place(relx=0.016, rely=0.418, relheight=0.341, relwidth=0.934)
    frameopt.configure(relief='groove', borderwidth="2", width=285)
    
    n = int(spinbox1.get())
    
    labeltitle = Label(frame1)
    labeltitle.place(relx=0.213, rely=0.088, height=31, width=159)
    labeltitle.configure(background="#0082ba", foreground="white", text='''Startup Nº{}'''.format(n), relief="groove")

    frametxt = Frame(frame1)
    frametxt.place(relx=0.016, rely=0.286, relheight=0.473, relwidth=0.944)
    frametxt.configure(relief='groove', width=285, borderwidth="2")

    labelweb = Label(frametxt)
    labelweb.place(relx=0.017, rely=0.721, height=31, width=109)
    labelweb.configure(background="#0082ba", foreground="white", relief='ridge', text='''Website:''')
    
    labelinvest = Label(frametxt)
    labelinvest.place(relx=0.017, rely=0.419, height=31, width=109)
    labelinvest.configure(background="#0082ba", foreground="white", relief='ridge', text='''Investimento:''')
    
    labelname = Label(frametxt)
    labelname.place(relx=0.017, rely=0.116, height=31, width=109)
    labelname.configure(background="#0082ba", foreground="white", relief='ridge', text='''Nome da Startup:''')
    
    nome = empresas[n-1][0]
    invest = "{} €".format(empresas[n-1][1])
    web = empresas[n-1][2]
    
    textnome = Text(frametxt)
    textnome.place(relx=0.415, rely=0.14, relheight=0.112, relwidth=0.569)
    textnome.configure(width=164)
    textnome.insert(END, nome)
    textnome.configure(state='disabled')
    
    textinvest = Text(frametxt)
    textinvest.place(relx=0.415, rely=0.442, relheight=0.112, relwidth=0.569)
    textinvest.configure(width=164)
    textinvest.insert(END, invest)
    textinvest.configure(state='disabled')
    
    textweb = Text(frametxt)
    textweb.place(relx=0.415, rely=0.744, relheight=0.112, relwidth=0.569)
    textweb.configure(width=164)
    textweb.insert(END, web)
    textweb.configure(state='disabled')
    
    img1 = PhotoImage(file="./Files/Image/img1.png")
    labelimg = Label(frame2)
    labelimg.place(relx=0.164, rely=0.088, height=109, width=199)
    labelimg.configure(relief='ridge', image=img1)

    def abrirWebsite():
        webbrowser.open(empresas[n-1][2])   
    
    def eliClose():
        def eliminarStartup():
            empresas.remove(empresas[n-1])
        def closeWindow():
            window7.destroy()
            window9.destroy()
            menuLista()
        r = messagebox.askyesno("Confirmar", "Tem a certeza que pretende eliminar a startup selecionada?\n")
        if r == True:
            eliminarStartup()
            closeWindow()
        else:
            quit
        
    def grafIndividual():
        window12 = Tk()
        window12.resizable(False, False)
        window12.title('Gráfico de Barras Individual')
        
        nome = []
        invest = []
        nome.append(empresas[n-1][0])
        invest.append(empresas[n-1][1])
        
        formatter = FuncFormatter(currency)
        Data1 = {'Startup': nome,
                'Investimento': invest}
        
        df1 = DataFrame(Data1, columns= ['Startup', 'Investimento'])
        df1 = df1[['Startup', 'Investimento']].groupby('Startup').sum()
        
        figure1 = plt.Figure(figsize=(10.5,5), dpi=100)
        ax1 = figure1.add_subplot(111)
        ax1.set_title('Investimento Total da Startup')
        bar1 = FigureCanvasTkAgg(figure1, window12)
        bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
        ax1.set_xticks([0, 1000e3, 2500e3, 5000e3, 7500e3, 10000e3, 12500e3, 15000e3, 17500e3, 20000e3, 22500e3, 25000e3])
        ax1.xaxis.set_major_formatter(formatter)
        df1.plot(kind='barh', legend=False, ax=ax1)
        
        window5.mainloop()

    buttondel = Button(frameopt)
    buttondel.place(relx=0.035, rely=0.645, height=24, width=257)
    buttondel.configure(pady="0", text='''Eliminar Startup''', command=eliClose)
    
    buttongraf = Button(frameopt)
    buttongraf.place(relx=0.035, rely=0.387, height=24, width=257)
    buttongraf.configure(pady="0", text='''Visualizar Gráfico de Investimento Invididual''', command=grafIndividual)
    
    buttonweb = Button(frameopt)
    buttonweb.place(relx=0.035, rely=0.129, height=24, width=257)
    buttonweb.configure(pady="0", text='''Abrir Website''', command=abrirWebsite)
    
    labelopt = Label(frame2)
    labelopt.place(relx=0.016, rely=0.352, height=31, width=109)
    labelopt.configure(text='''Menu de Opções:''', relief="groove", background="#0082ba", foreground="white")
    
    window7.mainloop()
    
def addEmp():
    window4 = Tk()
    window4.resizable(False, False)
    window4.geometry('400x320+1080+268')
    window4.title('Adicionar Startup')
    
    frame1 = Frame(window4)
    frame1.place(relx=0.05, rely=0.25, relheight=0.578, relwidth=0.913)
    frame1.configure(relief='groove', borderwidth="2", width=365)
    
    labelnome = Label(frame1)
    labelnome.place(relx=0.055, rely=0.081, height=31, width=134)
    labelnome.configure(relief='ridge', text='''Nome da Startup:''', background="#0082ba", foreground="white")
    
    labelinvest = Label(frame1)
    labelinvest.place(relx=0.055, rely=0.432, height=31, width=134)
    labelinvest.configure(relief='ridge', text='''Investimento:''', background="#0082ba", foreground="white")
    
    labelweb = Label(frame1)
    labelweb.place(relx=0.055, rely=0.757, height=31, width=134)
    labelweb.configure(relief='ridge', text='''Website:''', background="#0082ba", foreground="white")
                          
    entrynome = Entry(frame1, bd=5)
    entrynome.place(relx=0.460, rely=0.108,height=23, relwidth=0.477)
    
    entryinvest = Entry(frame1, bd=5)
    entryinvest.place(relx=0.460, rely=0.460,height=23, relwidth=0.477)

    entrywebsite = Entry(frame1, bd=5)
    entrywebsite.place(relx=0.460, rely=0.784,height=23, relwidth=0.477)
    
    labeltitle = Label(window4)
    labeltitle.place(relx=0.25, rely=0.031, height=31, width=204)
    labeltitle.configure(background="#0082ba", foreground="white", relief='ridge', text='''Adicionar Startup:''')
                         
    labelopt = Label(window4)
    labelopt.place(relx=0.05, rely=0.156, height=31, width=109)
    labelopt.configure(background="#0082ba", foreground="white", relief='groove', text='''Menu de Opções:''')
         
    def closeWindow():
            window4.destroy()
            window9.destroy()
            menuLista()
            
    def addClose():
        def addicioEmp(): 
            nome = entrynome.get()
            invest = float(entryinvest.get())
            website = entrywebsite.get()
            empresas.append(criarEmpresa(nome, invest, website))
        addicioEmp()
        closeWindow()
        
    buttonconf = Button(window4)
    buttonconf.place(relx=0.35, rely=0.875, height=24, width=117)
    buttonconf.configure(text='''Confirmar''', pady="0", command=addClose)
    
    buttoncan = Button(window4)
    buttoncan.place(relx=0.663, rely=0.875, height=24, width=117)
    buttoncan.configure(text='''Cancelar''', pady="0", command=closeWindow)
    
aplicacao()                