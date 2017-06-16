#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from ttk import Combobox, Notebook
from tkMessageBox import*
import MySQLdb
from controller import *
import calendar
import datetime
import time

class Contratos(Frame):
        def __init__(self, parent, controller):
                        Frame.__init__(self, parent)
                        
                        #VARIABLES GLOBALES
                        global cod, cc, inquilino, codinm, inmueble, nit, owner, rel, vlrenta, duracion 
                        global contratos, tcontrato, incremento, gfacturaIni, facturaSgte, fecha, hoy 
                        global notas, anexos, destinacion, servicios, conexos, tercero, nombret, fecha
                        global aplicado, cc_aplicado, n_aplicado, inm_aplicado, novedad, n_nombre, n_valor
                        global h, busqueda, clean, update, add
                        
                        #INSTANCIEAS DE LOS WIDGETS
                        global e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, Cbx1, chkb1, chkb2, lb, cedulaE, notas
                        
                        fecha = datetime.date.today()
                        hoy = "%s" %fecha #ESTE NUESTRA LA FECHA EN FORMATO AÑO-MES-DIA (YYYY/MM/DD)
                        #hoy = time.strftime("%d/%m/%y") #ESTO PARA VER FORMATO FECHA EN DIA/MES/AÑO
                        #hoy = time.strftime("%y/%m/%d")
                        h = hoy
                        
                        #VARIABLES
                        lupa = PhotoImage(file='img/lupa.png')
                        schedule = PhotoImage(file='img/calendar.gif')
                        
                        cod = IntVar()
                        cc = StringVar()
                        inquilino = StringVar()
                        codinm = IntVar()
                        inmueble = StringVar()
                        nit = StringVar()
                        owner = StringVar()
                        rel = IntVar()
                        
                        vlrenta = DoubleVar()
                        duracion = IntVar()
                        contratos = ['Vivienda', 'Comercial', 'Mixta']
                        tcontrato = StringVar()
                        incremento = DoubleVar()
                        gfacturaIni = IntVar()
                        facturaSgte = IntVar()
                        fecha = StringVar()
                        
                        notas = StringVar()
                        anexos = StringVar()
                        destinacion = StringVar()
                        servicios = StringVar()
                        conexos = StringVar()
                        
                        tercero = StringVar()
                        nombret = StringVar()
                        
                        aplicado = IntVar()
                        cc_aplicado = StringVar()
                        n_aplicado = StringVar()
                        inm_aplicado = StringVar()
                        novedad = StringVar()
                        n_nombre = StringVar()
                        n_valor = DoubleVar()
                        
                        #BUSQUEDA = ["Nombre","CC/Nit"]
                        busqueda = StringVar()
                        busqueda.trace("w", lambda name, index, mode: buscar())
                        dato = StringVar()
                        
                        #WIDGETS
                        
                        #========================= HEADER ===========================
                        
                        self.header = Label(self, text="CONTRATOS", font="bold")
                        self.header.pack(pady=20, side=TOP)
                        
                        #========================== WRAPPER ==========================
                        
                        self.wrapper = Frame (self)
                        self.wrapper.pack(side=LEFT, fill=Y)
                        
                        #================ NOTEBOOK =============>
                        
                        self.nb = Notebook(self.wrapper)
                        
                        #-----------------------> TAB 1
                        
                        self.tab1 = Frame (self.nb)
                        
                        self.f0 = Frame(self.tab1)#-------------------------------------
                        self.f0.pack(pady=5,fill=X)
                        
                        l1 = Label(self.f0, text='Código:')
                        l1.pack(side=LEFT)
                        
                        e1 = Entry(self.f0, textvariable=cod, width=10)
                        e1.pack(side=LEFT)
                        
                        self.f1 = Frame(self.tab1)#-------------------------------------
                        self.f1.pack(pady=5,fill=X)
                        
                        l2 = Label(self.f1, text='Arrendatario:')
                        l2.pack(side=LEFT, fill=X)
                        
                        e2 = Entry(self.f1, textvariable=cc, width=15)
                        e2.pack(side=LEFT)
                        e2.bind('<Return>', buscarA)
                        
                        b1 = Button(self.f1, image=lupa, command=topArrendatario)
                        b1.image = lupa
                        b1.pack(side=LEFT)
                        
                        e3 = Entry(self.f1, textvariable=inquilino, state=DISABLED)
                        e3.pack(side=LEFT, fill=X, expand=1)
                        
                        self.f2 = Frame(self.tab1)
                        self.f2.pack(pady=5,fill=X)#------------------------------------
                        
                        l3 = Label(self.f2, text='Inmueble:')
                        l3.pack(side=LEFT)
                        
                        e4 = Entry(self.f2, textvariable=codinm, width=10)
                        e4.pack(side=LEFT)
                        e4.bind('<Return>', buscarR)
                        
                        b2 = Button(self.f2, image=lupa, command=topRelacion)
                        b2.pack(side=LEFT)
                        
                        e5 = Entry(self.f2, textvariable=inmueble, state=DISABLED)
                        e5.pack(side=LEFT, fill=X, expand=1)
                        
                        self.f3 = Frame(self.tab1)
                        self.f3.pack(pady=5,fill=X)#------------------------------------
                        
                        l4 = Label(self.f3, text='Propietario:')
                        l4.pack(side=LEFT)
                        
                        e6 = Entry(self.f3, width=15, textvariable=nit, state=DISABLED)
                        e6.pack(side=LEFT)
                        e7 = Entry(self.f3, width=5, textvariable=owner, state=DISABLED)
                        e7.pack(side=LEFT, fill=X, expand=1)
                        
                        self.f4 = Frame(self.tab1)
                        self.f4.pack(pady=5,fill=X)#------------------------------------
                        
                        self.arriendo = Label(self.f4, text='Arriendo $:')
                        self.arriendo.pack(side=LEFT)
                        e8 = Entry(self.f4, textvariable=vlrenta, state=DISABLED, width=20)
                        e8.pack(side=LEFT)
                        
                        self.duracion = Label(self.f4, text='Duración Contrato:')
                        self.duracion.pack(side=LEFT)
                        e9 = Entry(self.f4, textvariable=duracion, width=5)
                        e9.pack(side=LEFT)
                        
                        self.meses = Label(self.f4, text='Meses')
                        self.meses.pack(side=LEFT)
                        
                        self.f5 = Frame(self.tab1)
                        self.f5.pack(pady=5,fill=X)#------------------------------------
                        
                        self.tcontrato = Label(self.f5, text='Tipo Contrato:')
                        self.tcontrato.pack(side=LEFT)
                        
                        Cbx1 = Combobox(self.f5, textvariable=tcontrato, values=contratos, width=10)
                        Cbx1.set('')
                        Cbx1.pack(side=LEFT)
                        
                        self.incremento = Label(self.f5, text='Incremento:')
                        self.incremento.pack(side=LEFT)
                        e10 = Entry(self.f5, textvariable=incremento, width=5)
                        e10.pack(side=LEFT)
                        
                        chkb1 = Checkbutton(self.f5, text="General factura\n inicial", variable=gfacturaIni)
                        chkb1.pack(side=LEFT)
                        chkb2 = Checkbutton(self.f5, text="Facturar príodo\n siguiente", variable=facturaSgte)
                        chkb2.pack(side=LEFT)
                        
                        self.f6 = Frame(self.tab1)
                        self.f6.pack(pady=5,fill=X)#------------------------------------
                        
                        btime = Button(self.f6, image=schedule, command=calendario)
                        btime.image = schedule
                        btime.pack(side=RIGHT)
                        
                        etime = Entry(self.f6, textvariable=fecha, width=10)
                        fecha.set(hoy)
                        etime.pack(side=RIGHT)
                        
                        #ltime = Label(self.f6, text=hoy, font="bold", foreground='red')
                        #ltime.pack(side=RIGHT)
                        
                        self.fi = Label(self.f6, text='Fecha Inicio: ')
                        self.fi.pack(side=RIGHT)
                        
                        self.tab1.pack()
                        
                        #-----------------------> TAB 2
                        
                        self.tab2 = Frame (self.nb)
                        self.tab2.pack()
                        
                        self.f7 = Frame(self.tab2)#-------------------------------------
                        self.f7.pack(fill=X, pady=10)
                        
                        notas = Text(self.f7, height=5)
                        notas.pack(side=LEFT, fill=X, expand=1)
                        
                        self.f8 = Frame(self.tab2)
                        self.f8.pack(pady=5,fill=X)#-------------------------------------------
                        
                        self.destino = Label(self.f8, text='Destinación:')
                        self.destino.pack(side=LEFT)
                        self.destinoE = Entry(self.f8, textvariable=destinacion, width=5)
                        self.destinoE.pack(side=LEFT, fill=X, expand=1)
                        
                        self.f9 = Frame(self.tab2)
                        self.f9.pack(pady=5,fill=X)#-------------------------------------------
                        
                        self.servicios = Label(self.f9, text='Servicios adicionales:')
                        self.servicios.pack(side=LEFT)
                        self.serviciosE = Entry(self.f9, textvariable=servicios, width=5)
                        self.serviciosE.pack(side=LEFT, fill=X, expand=1)
                        
                        self.f10 = Frame(self.tab2)
                        self.f10.pack(pady=5,fill=X)#-------------------------------------------
                        
                        self.conexos = Label(self.f10, text='Conexos:')
                        self.conexos.pack(side=LEFT)
                        self.conexosE = Entry(self.f10, textvariable=conexos, width=5)
                        self.conexosE.pack(side=LEFT, fill=X, expand=1)
                        
                        #-----------------------> TAB 3
                        
                        self.tab3 = Frame (self.nb)
                        self.tab3.pack()
                        
                        self.f11 = Frame(self.tab3)#-------------------------------------
                        self.f11.pack(fill=X, pady=5)
                        
                        self.cedula = Label (self.f11, text='CC/Nit: ')
                        self.cedula.pack(side=LEFT)
                        
                        cedulaE = Entry(self.f11, textvariable=tercero, width=15)
                        cedulaE.pack(side=LEFT)
                        cedulaE.bind('<Return>', buscarT)
                        
                        b4 = Button(self.f11, image=lupa, command=topTercero)
                        b4.image = lupa
                        b4.pack(side=LEFT)
                        
                        self.f12 = Frame(self.tab3) #-------------------------------------
                        self.f12.pack(fill=X, pady=5)
                        
                        self.tercero = Label (self.f12, text='Nombre: ')
                        self.tercero.pack(side=LEFT)
                        
                        self.terceroE = Entry(self.f12, textvariable=nombret, width=5, state=DISABLED)
                        self.terceroE.pack(side=LEFT, fill=X, expand=1)
                        
                        #-----------------------> TAB 4
                        
                        self.tab4 = Frame (self.nb)
                        self.tab4.pack()
                        
                        self.f13 = Frame(self.tab4) #-------------------------------------
                        self.f13.pack(fill=X, pady=5)
                        
                        l = Label (self.f13, text='Aplicar a: ')
                        l.pack(side=LEFT)
                        
                        Ch = Checkbutton(self.f13, text="Propietario", variable=aplicado)
                        Ch.pack(side=LEFT)
                        
                        self.f14 = Frame(self.tab4) #-------------------------------------
                        self.f14.pack(fill=X, pady=5)
                        
                        l13 = Label (self.f14, text='CC/Nit: ')
                        l13.pack(side=LEFT)
                        
                        e13 = Entry(self.f14, textvariable=cc_aplicado, width=15)
                        e13.pack(side=LEFT)
                        
                        b13 = Button(self.f14, image=lupa, command=None)
                        b13.image = lupa
                        b13.pack(side=LEFT)
                        
                        e13 = Entry(self.f14, textvariable=n_aplicado, state=DISABLED)
                        e13.pack(side=LEFT, fill=X, expand=1)
                        
                        self.f15 = Frame(self.tab4)
                        self.f15.pack(fill=X, pady=5)#------------------------------------
                        
                        l14 = Label(self.f15, text='Cod.Inmueble:')
                        l14.pack(side=LEFT)
                        
                        e14 = Entry(self.f15, textvariable=inm_aplicado, width=5, state=DISABLED)
                        e14.pack(side=LEFT, fill=X, expand=1)
                        
                        self.f16 = Frame(self.tab4)
                        self.f16.pack(fill=X, pady=5)#------------------------------------
                        
                        l16 = Label(self.f16, text='Novedad:')
                        l16.pack(side=LEFT, fill=X)
                        
                        e16 = Entry(self.f16, textvariable=novedad, width=15)
                        e16.pack(side=LEFT)
                        
                        b16 = Button(self.f16, image=lupa, command=None)
                        b16.image = lupa
                        b16.pack(side=LEFT)
                        
                        e16 = Entry(self.f16, textvariable=n_nombre, state=DISABLED)
                        e16.pack(side=LEFT, fill=X, expand=1)
                        
                        self.f17 = Frame(self.tab4)
                        self.f17.pack(fill=X, pady=5)#------------------------------------
                        
                        l17 = Label(self.f17, text='Vlr Novedad:')
                        l17.pack(side=LEFT, fill=X)
                        
                        e17 = Entry(self.f17, textvariable=n_valor, width=15)
                        e17.pack(side=LEFT)
                        
                        #---------------------------------------------------------------
                        
                        self.nb.add (self.tab1, text="General")
                        self.nb.add(self.tab2, text="Anexos")
                        self.nb.add(self.tab3, text="Tercero")
                        self.nb.add(self.tab4, text="Gasto fijo")
                        
                        self.nb.pack()
                        
                        self.fBtn = Frame(self.wrapper)
                        self.fBtn.pack()#-------------------------------
                        
                        clean = Button(self.fBtn, text='Limpiar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=limpiar)
                        clean.pack(side=RIGHT)
                        
                        update = Button(self.fBtn, text='Actualizar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=actualizar, state=DISABLED)
                        update.pack(side=RIGHT)
                        
                        add = Button(self.fBtn, text='Agregar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=agregar)
                        add.pack(side=RIGHT)
                        
                        #========================= ASIDE ===========================
                        
                        self.aside = Frame(self)
                        self.aside.pack(side=TOP, fill=BOTH)
                        
                        self.wrap1 = Frame(self.aside)
                        self.wrap1.pack()
                        
                        self.viewer = Label(self.wrap1, text="LISTA DE CONTRATOS")
                        self.viewer.pack()
                        
                        scroll = Scrollbar(self.wrap1, orient=VERTICAL)
                        scroll.pack(side=RIGHT, fill=Y)
                        lb = Listbox(self.wrap1, yscrollcommand=scroll.set, height=20, width=30)
                        scroll.config (command=lb.yview)
                        lb.pack(fill=BOTH)
                        lb.bind("<Double-Button-1>", callback)
                        
                        self.wrap2 = Frame(self.aside)
                        self.wrap2.pack()
                        
                        show = Button(self.wrap2, text='Cargar lista', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=cargar)
                        show.pack(fill=X)
                        
                        delete = Button(self.wrap2, text='Borrar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=borrar)
                        delete.pack(fill=X)
                        
                        edit = Button(self.wrap2, text='Modificar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=modificar)
                        edit.pack(fill=X)
                        
                        buscador = Label(self.wrap2, text="Buscar por CC:")
                        buscador.pack()
                        E = Entry(self.wrap2, textvariable=busqueda, width=24)
                        E.pack()
                        
def buscarA(event):
        connect.commit()
        try:
                v = cc.get()
                search = "SELECT a_nombres, a_apellidos FROM arrendatarios WHERE a_cc='%s';" % (v)
                cursor.execute(search)
                connect.commit()
                dato = cursor.fetchall()
                for n, a in dato:
                        v = n + " " + a
                        inquilino.set(v)

        except TypeError, e:
                showerror("Error", e)
                e2.focus()
                cc.set("")

        except MySQLdb.IntegrityError, e:
                showerror("Error", e)
                e2.focus()
                cc.set("")

        except:
                showerror ("Mensaje", "No se encuentra!")
                e2.focus()
                cc.set("")

def topArrendatario():
        global topB, topB_scroll, topB_lb
        
        topB = Toplevel()
        topB.title("Arrendatarios")
        topB.geometry("300x300")
        
        topB.wm_attributes("-topmost", 1)#Inabilitar este en WIN
        topB.focus_set()#Mantiene el toplevel sobre root/w
        topB.transient() #Se minimiza solo cuando root lo hace
        topB.grab_set() #Impite que se interactue con la ventana root/w
                        
        topB_scroll = Scrollbar(topB, orient=VERTICAL)
        topB_scroll.pack(side=RIGHT, fill=Y)
        topB_lb = Listbox(topB, yscrollcommand=topB_scroll.set, height=20, width=20)
        topB_scroll.config (command=topB_lb.yview)
        topB_lb.pack(fill=BOTH)
        topB_lb.bind("<Double-Button-1>", cargarArrendatario)
        
        try:
                connect.commit()
                display = "SELECT a_nombres FROM arrendatarios;"
                cursor.execute(display)
                registros = cursor.fetchall()
                topB_lb.delete(0, END)
                for item in registros:
                        nombre = item[0]
                        topB_lb.insert(END, nombre)

        except TypeError, e:
                showerror("Error al cargar los arrendatarios", e)
                
        except MySQLdb.IntegrityError, e:
                showerror("Error", e)

def cargarArrendatario(event):
        i = topB_lb.curselection()[0]
        val = topB_lb.get(i)
        connect.commit()
        edit = "SELECT a_nombres, a_apellidos, a_cc FROM arrendatarios WHERE a_nombres='%s';" % (val)
        cursor.execute(edit)
        sol = cursor.fetchall()
        for n, a, c in sol:
                v = n + " " + a
                inquilino.set(v)
                cc.set(c)
                
        topB.destroy()
                
def buscarR(event):
        try:
                v1 = codinm.get()
                sql = "SELECT r_id, inmueble, p_cc, dueño, inmuebles.i_vlrenta FROM inmuebles INNER JOIN relacionip ON inmuebles.i_cod=relacionip.i_cod WHERE relacionip.i_cod=%d;" % (v1)
                #sql = "SELECT inmueble, p_cc, dueño from relacionip WHERE i_cod='%d';" % (v1)
                cursor.execute(sql)
                query = cursor.fetchall()
                for c, i, p, d, r in query:
                        rel.set(c)
                        inmueble.set(i)
                        nit.set(p)
                        owner.set(d)
                        vlrenta.set(r)
        except:
                showerror ("Mensaje", "No se encuentra!")

def topRelacion():
        global topB, topB_scroll, topB_lb
        
        topB = Toplevel()
        topB.title("Inmueble Propietario")
        topB.geometry("300x300")
        
        topB.wm_attributes("-topmost", 1)#Inabilitar este en WIN
        topB.focus_set()#Mantiene el toplevel sobre root/w
        topB.transient() #Se minimiza solo cuando root lo hace
        topB.grab_set() #Impite que se interactue con la ventana root/w
                        
        topB_scroll = Scrollbar(topB, orient=VERTICAL)
        topB_scroll.pack(side=RIGHT, fill=Y)
        topB_lb = Listbox(topB, yscrollcommand=topB_scroll.set, height=20, width=20)
        topB_scroll.config (command=topB_lb.yview)
        topB_lb.pack(fill=BOTH)
        topB_lb.bind("<Double-Button-1>", cargarRelacion)
        
        try:
                connect.commit()
                display = "SELECT i_cod FROM relacionip;"
                cursor.execute(display)
                registros = cursor.fetchall()
                topB_lb.delete(0, END)
                for item in registros:
                        codigos = item[0]
                        topB_lb.insert(END, codigos)

        except TypeError, e:
                showerror("Error al cargar los inmuebles", e)
                
        except MySQLdb.IntegrityError, e:
                showerror("Error", e)

def cargarRelacion(event):
        i = topB_lb.curselection()[0]
        val = topB_lb.get(i)
        connect.commit()
        sql = "SELECT relacionip.i_cod, r_id, inmueble, p_cc, dueño, inmuebles.i_vlrenta FROM inmuebles INNER JOIN relacionip ON inmuebles.i_cod=relacionip.i_cod WHERE relacionip.i_cod=%d;" % (val)
        cursor.execute(sql)
        query = cursor.fetchall()
        for o, c, i, p, d, r in query:
                codinm.set(o)
                rel.set(c)
                inmueble.set(i)
                nit.set(p)
                owner.set(d)
                vlrenta.set(r)
                
        topB.destroy()
                
def buscarT(event):
        connect.commit()
        try:
                v2 = tercero.get()
                sql = "SELECT t_nombre from terceros WHERE t_cc='%s';" % (v2)
                cursor.execute(sql)
                result = cursor.fetchone()
                for t in result:
                        nombret.set(t)
        except:
                showerror ("Mensaje", "No se encuentra!")

def topTercero():
        global topB, topB_scroll, topB_lb
        
        topB = Toplevel()
        topB.title("Terceros")
        topB.geometry("300x300")
        
        topB.wm_attributes("-topmost", 1)#Inabilitar este en WIN
        topB.focus_set()#Mantiene el toplevel sobre root/w
        topB.transient() #Se minimiza solo cuando root lo hace
        topB.grab_set() #Impite que se interactue con la ventana root/w
                        
        topB_scroll = Scrollbar(topB, orient=VERTICAL)
        topB_scroll.pack(side=RIGHT, fill=Y)
        topB_lb = Listbox(topB, yscrollcommand=topB_scroll.set, height=20, width=20)
        topB_scroll.config (command=topB_lb.yview)
        topB_lb.pack(fill=BOTH)
        topB_lb.bind("<Double-Button-1>", cargarTercero)
        
        try:
                connect.commit()
                display = "SELECT t_nombre FROM terceros;"
                cursor.execute(display)
                registros = cursor.fetchall()
                topB_lb.delete(0, END)
                for item in registros:
                        nombre = item[0]
                        topB_lb.insert(END, nombre)

        except TypeError, e:
                showerror("Error al cargar los terceros", e)
                
        except MySQLdb.IntegrityError, e:
                showerror("Error", e)

def cargarTercero(event):
        i = topB_lb.curselection()[0]
        val = topB_lb.get(i)
        connect.commit()
        sql = "SELECT t_cc, t_nombre FROM terceros WHERE t_nombre='%s';" % (val)
        cursor.execute(sql)
        query = cursor.fetchall()
        for c, n in query:
                tercero.set(c)
                nombret.set(n)
                
        topB.destroy()
        
def agregar():
        v1 = cod.get()  #IntVar() = %d
        v2 = cc.get()   #StringVar() = %s
        v3 = inquilino.get()#StringVar() = %s
        v4 = rel.get()  #IntVar()
        v5 = duracion.get()     #IntVar() = %d
        v6 = tcontrato.get() #StringVar() = %d
        v7 = incremento.get()   #DoubleVar() = %f
        v8 = gfacturaIni.get()  #IntVar() = %d
        v9 = facturaSgte.get()  #IntVar() = %d
        #v10 = "%s"%(h)
        v11 = notas.get("1.0",END)      #StringVar() = %s
        v12 = destinacion.get() #StringVar() = %s
        v13 = servicios.get()   #StringVar() = %s
        v14 = conexos.get()     #StringVar() = %s
        v15 = tercero.get() #StringVar() = %s
        v16 = 1 #IntVar() = %d
        connect.commit()
        #sql = "INSERT INTO contratos (c_cod, a_cc, inquilino, r_id, c_duracion, c_tcontrato, c_incremento, c_gfacturaIni, c_facturaSgte, c_fecha, c_anexos, c_destino, c_servicios, c_conexos, t_cc, c_estado) values ('%d','%s','%s','%d','%d','%d','%f','%d','%d','%s','%s','%s','%s','%s','%s','%d');" %(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16)
        sql = "INSERT INTO contratos (c_cod, a_cc, inquilino, r_id, c_duracion, c_tcontrato, c_incremento, c_gfacturaIni, c_facturaSgte, c_anexos, c_destino, c_servicios, c_conexos, t_cc, c_estado) values ('%d','%s','%s', '%d', '%d', '%s', '%f', '%d', '%d', '%s', '%s', '%s', '%s', '%s', '%d');" %(v1, v2, v3, v4, v5, v6, v7, v8, v9, v11, v12, v13, v14, v15, v16)
        cursor.execute(sql)
        showinfo("Mensaje", "Contrato registrado!")
        cargar()
        limpiar()
        
        #except MySQLdb.IntegrityError, e:
                #showerror("Error", e)
                #showerror ('Mensaje', "Debe llenar los campos obligatorios!")
        
def factura_ini():
        doc = SimpleDocTemplate("facturas/factura_inicial.pdf", pagesize = letter,
                                                        #rightMargin=72,leftMargin=72,
                                                        topMargin=10)
        story=[]
        
        #-------------------------------------------- CABECERA DEL DOCUMENTO
        
        #VARIABLES
        logo = Image("img/logo.gif", width=150, height=45) #LOGO
        logo.hAlign ='LEFT' #Posicion de la img en la hoja
        
        info = Paragraph('''<para align=center leading=8><font size=6>CALLE 11A N°42-68 LOC,195<br/>
                TELEFONO: 3110513 FAX:2664154<br/>
                AA.75105 ED. EL DORADO<br/>
                AFILIADO A FENALCO<br/>
                M.A.V.U N°000078</font></para>''', styleSheet["BodyText"])
        
        tipoDoc = Paragraph ('''<para align=right><b>FACTURA DE VENTA<br/>N°</b></para>''', styleSheet["BodyText"])
        
        #TABLA
        tabla1 = Table([[logo, info, tipoDoc]], colWidths=160, rowHeights=None)
        tabla1.setStyle([
                ('VALIGN', (1,0), (2,0), 'TOP'),
                ('ALIGN', (2,0), (2,0), 'RIGHT')#ALINEAR A LA DER
                ])
                
        story.append(tabla1) #Construye la tabla 't' definida anteriormente
        story.append(Spacer(0,-10)) #Espacio del salto de línea con el siguiente Ejemplo
        
        #-------------------------------------------- DATOS GENERALES DEL DOCUMENTO
        
        #VARIABLES
        inquilino = Paragraph ('''<font size=6><b>Nombre Arrendatario:</b><br/></font>%s'''%d1, styleSheet["BodyText"])
        docID = Paragraph ('''<font size=6><b>CC/Nit: </b></font>       %s''' %d0, styleSheet["BodyText"])
        locImn = Paragraph ('''<font size=6><b>Dirección Inmueble:</b><br/></font>%s'''%d2, styleSheet["BodyText"])
        telefono = Paragraph ('''<font size=6><b>Teléfono:</b><br/></font>%s'''%d4, styleSheet["BodyText"])
        IDpropietario = Paragraph ('''<font size=6><b>CC/Nit:</b><br/></font>%s'''%d7, styleSheet["BodyText"])
        propietario = Paragraph ('''<font size=6><b>Propietario: </b></font>%s'''%d6, styleSheet["BodyText"])
        fechaFormato = Paragraph ('''<para align=center fontSize=6>Día Mes Año</para>''', styleSheet["BodyText"])
        hoy = time.strftime("%d/%m/%Y")
        fecha = Paragraph ('''<para align=center spaceBefore=0>%s</para>''' %hoy, styleSheet["BodyText"])
        codigoImn = Paragraph ('''<font size=6><b>Código Inmueble:</b><br/></font>%s'''%d3, styleSheet["BodyText"])
        
        #TABLA
        datos = [[inquilino,'','','','',[fechaFormato,fecha]],
                         [docID,'','',propietario,'',''],
                         [locImn,'',telefono,IDpropietario,'',codigoImn]]
                         
        tabla2 = Table(datos, 
                                   style=[('BOX',(0,0),(2,2),0.5,colors.black),
                                                  ('VALIGN', (0,0),(2,0),'TOP'),
                                                  ('SPAN',(0,0),(2,0)),#Combinar 3 filas (col0,row0) hasta (col2,row0) Arrendatario #0
                                                  ('SPAN',(0,1),(2,1)),#Combinar 3 filas CC/Nit #1
                                                  ('SPAN',(0,2),(1,2)),#Combinar 2 filas Dirección #2
                                                  ('SPAN',(3,1),(5,1)),#Combinar 3 filas Nombre Propietario #
                                                  ('SPAN',(3,2),(4,2)),#Combinar 2 filas CC/Nit Propietario #
                                                  ('GRID',(3,1),(4,2),0.5,colors.black),
                                                  ('GRID',(5,0),(5,2),0.5,colors.black)
                                                 ],colWidths=80, rowHeights=None)
                                                 
        #Constructor y espaciado
        story.append(Spacer(0,15)) #Espacio del salto de línea con el siguiente Ejemplo
        story.append(tabla2) #Construye la tabla 't' definida anteriormente
        
        #-------------------------------------------- DETALLES DEL DOCUMENTO
        
        #VARIABLES
        desc = Paragraph('''<para align=center><b>DESCRIPCION</b></para>''', styleSheet["BodyText"])
        vlr = Paragraph('''<para align=center><b>VALOR</b></para>''', styleSheet["BodyText"])
        item1 = Paragraph('''Valor Arrendamiento Mes: %s/%s''' % (d8,d9), styleSheet["BodyText"])
        item2 = Paragraph('''Valor Comisión Inical %s''' % (d8,d9), styleSheet["BodyText"])
        item3 = Paragraph('''Valor Iva Comisión Inical %s''' % (d8,d9), styleSheet["BodyText"])
        item4 = Paragraph('''Valor Papelería %s''' % (d8,d9), styleSheet["BodyText"])
        item5 = Paragraph('''Valor Iva Papelería %s''' % (d8,d9), styleSheet["BodyText"])
                
        resol = "Resolucion Dian N°110000658514 de Diciembre de 2015 Consectivo Facturacion 33001 al 36000. P"
        
        #TABLA
        data=[[desc, '', vlr],                  #0
                  [item1, '', vlrenta],         #1
                  [item2, '', vlComIni],        #2
                  [item3, '', vlIvaIni],        #3
                  [item4, '', vlPapel],         #4
                  [item5, '', vlIvaPapel],      #5
                  ['', '', ''],                         #6
                  ['Observaciones', 'SUBTOTAL', vlrenta], #7
                  [comentario, 'IVA', d5], #8
                  [resolucion, 'TOTAL', d10]] #9
                  
        #Formato de la tabla
        t=Table(data,
                style=[
                        ('GRID',(0,0),(2,0),0.5,colors.grey),#Color regilla de DESCRIPCION & VALOR
                        ('BOX',(2,1),(2,9),0.5,colors.grey), #Color & grosor de la tabla o marco externo de los VALORES
                        ('BACKGROUND',(0,0),(2,0), colors.pink), #Color de fondo de DESCRIPCION & VALOR #0
                        ('SPAN',(0,0),(1,0)), #Combinar filas DESCRIPCION #0
                        ('BOX',(0,1),(2,6),0.5,colors.grey), #Color & grosor de la tabla o marco externo de los DETALLES
                        ('ALIGN', (2,1), (2,1), 'CENTER'),#Centrar #1
                        ('SPAN',(0,1),(1,1)), #Combinar filas de Detalle #1
                        ('SPAN',(0,2),(1,2)), #Combinar filas de Detalle #2
                        ('SPAN',(0,3),(1,3)), #Combinar filas de Detalle #3
                        ('SPAN',(0,4),(1,4)), #Combinar filas de Detalle #4
                        ('SPAN',(0,5),(1,5)), #Combinar filas de Detalle #5
                        ('SPAN',(0,6),(1,6)), #Combinar filas de Detalle #6
                        ('GRID',(1,7),(2,8),0.5,colors.grey),#Color regilla de SUBTOTAL, IVA, TOTAL
                        ('BOX',(0,7),(0,9),0.5,colors.grey), #Color & grosor de la tabla o marco externo de los OBSERVACIONES Y RESOLUCION
                        ('FONTSIZE', (0,9),(0,9),7), #Tamaño de la Resolucion
                        ('BACKGROUND',(1,9),(1,9),colors.black),#Color de fondo de TOTAL
                        ('TEXTCOLOR',(1,9),(1,9),colors.white), #Color de letra de TOTAL
                        ('BACKGROUND',(2,9),(2,9),colors.grey)#Color de fondo de VALOR TOTAL
                        ])
        
        story.append(Spacer(0,15)) #Espacio del salto de línea con el siguiente Ejemplo
        story.append(t) #Construye la tabla 't' definida anteriormente
        
        #-------------------------------------------- FIN PDF
        
        doc.build(story) #Constructor del documento
        
        if sys.platform == 'linux2':
                os.system("xdg-open ~/SBIENES/facturas/factura_inicial.pdf")#DEBIAN
        elif sys.platform == 'linux2':
                os.system("/usr/bin/gnome-open facturas/factura_inicial.pdf")#UBUNTU
        else:
                os.startfile("F:/SBIENES/facturas/factura_inicial.pdf")#WINDOWS

def borrar():
        try:
                t = lb.curselection()
                value = lb.get(t[0])
                if askyesno("Salir", "¿Desea borrar este contrato?"):
                        delete = """DELETE FROM contratos WHERE c_cod=("%s");""" % (value)
                        cursor.execute(delete)
                        connect.commit()
                        lb.delete(t)
                        showinfo("mensaje", "Dato Borrado!")
                        lb.delete(0, END)
                        cargar()
                        limpiar()
        except:
                showerror ('Error', "No se puede borrar el contrato.")

def cargar():
        try:
                connect.commit()
                display = "SELECT c_cod FROM contratos;"
                cursor.execute(display)
                registros = cursor.fetchall()
                lb.delete(0, END)
                for item in registros:
                        #print item
                        nombres = item[0]
                        lb.insert(END, nombres)
        except:
                showerror("Error", "Error al cargar los contratos")
        
def limpiar():
        cod.set(0)
        cc.set("")
        inquilino.set("")
        codinm.set(0)
        inmueble.set("")
        nit.set("")
        owner.set("")
        rel.set(0)
        vlrenta.set(0.0)
        duracion.set(0)
        tcontrato.set("")
        incremento.set(0.0)
        gfacturaIni.set(0)
        facturaSgte.set(0)
        #notas.delete('1.0', '2.0')
        notas.delete('1.0', END)
        destinacion.set("")
        servicios.set("")
        conexos.set("")
        tercero.set("")
        nombret.set("")

        habilitar()
        
def calendario():
        top = Toplevel()
        top.title("Calendario")
        
        top.wm_attributes("-topmost", 1)#Inabilitar este en WIN
        top.focus_set()#Mantiene el toplevel sobre root/w
        top.transient() #Se minimiza solo cuando root lo hace
        top.grab_set() #Impite que se interactue con la ventana root/w

# BLOQUEAR LOS CAMPO CUANDO SE CARGAN CON DOBLE CLIC (LLENAR):
def bloquear():
        e1.configure(state="disabled")
        e2.configure(state="disabled")
        e3.configure(state="disabled")
        e4.configure(state="disabled")
        e5.configure(state="disabled")
        e6.configure(state="disabled")
        e7.configure(state="disabled")
        e8.configure(state="disabled")
        e9.configure(state="disabled")
        e10.configure(state="disabled")
        Cbx1.configure(state="disabled")
        chkb1.configure(state="disabled")
        chkb2.configure(state="disabled")
        notas.configure(state="disabled")#Anexos
        cedulaE.configure(state="disabled")#CC del Tercero
        
# LLENAR CAMPOS CON DOBLE CLIC
def callback(event):
    llenar_campos()

def llenar_campos():
        limpiar()
        limpiar()
        i = lb.curselection()[0]
        valor = lb.get(i)
        cursor.execute("""SELECT c_cod, a_cc, inquilino, relacionip.i_cod, inmueble, p_cc, dueño, i_vlrenta, c_duracion, c_tcontrato, c_incremento, c_gfacturaIni, c_facturaSgte, c_fecha, c_anexos, c_destino, c_servicios, c_conexos, contratos.t_cc, t_nombre, c_codnovedad, c_novedad from contratos INNER JOIN relacionip on contratos.r_id = relacionip.r_id INNER JOIN inmuebles ON relacionip.i_cod = inmuebles.i_cod INNER JOIN terceros ON contratos.t_cc = terceros.t_cc WHERE c_cod=("%s");""" % (valor))
        result = cursor.fetchall()
        connect.commit()
        for item in result:
                d1 = item[0] #Código
                d2 = item[1] #CC Inquilino
                d3 = item[2] #Nombre Inquilino
                d4 = item[3] #Cód Inmueble
                d5 = item[4] #Inmueble
                d6 = item[5] #CC Propietario
                d7 = item[6] #Nombre Propietario
                d8 = item[7] #Valor Arriendo
                d9 = item[8] #Duración Contrato
                d10 = item[9] #Tipo de Contrato
                d11 = item[10] #Valor Incremento
                d12 = item[11] #Generar Factura Inicial
                d13 = item[12] #Factura Siguiente
                d14 = item[13] #Fecha
                d15 = item[14] #Anexos
                d16 = item[15] #Destino
                d17 = item[16] #Servicios
                d18 = item[17] #Conexos
                d19 = item[18] #CC Tercero
                d20 = item[19] #Nombre Tercero
                d21 = item[20] #Cod Novedad
                d22 = item[21] #Novedad
                
                #VARIABLES TOMAN VALOR DE LOS ITEMS DEL FOR
                cod.set(d1)
                cc.set(d2)
                inquilino.set(d3)
                codinm.set(d4)
                inmueble.set(d5)
                nit.set(d6)
                owner.set(d7)
                vlrenta.set(d8)
                duracion.set(d9)
                tcontrato.set(d10)
                incremento.set(d11)
                gfacturaIni.set(d12)
                facturaSgte.set(d13)
                fecha.set(d14)

                notas.insert('1.0',d15)
                destinacion.set(d16)
                servicios.set(d17)
                conexos.set(d18)

                tercero.set(d19)
                nombret.set(d20)
                
                bloquear()
                
def habilitar():
        e1.configure(state="normal")
        e2.configure(state="normal")
        #e3.configure(state="normal")
        e4.configure(state="normal")
        #e5.configure(state="normal")#Locacion
        #e6.configure(state="normal")
        #e7.configure(state="normal")
        #e8.configure(state="normal")#Vr renta
        e9.configure(state="normal")
        e10.configure(state="normal")
        Cbx1.configure(state="normal")
        chkb1.configure(state="normal")
        chkb2.configure(state="normal")
        notas.configure(state="normal")#Anexos
        cedulaE.configure(state="normal")#CC Tercero
        
def modificar():
        try:
                llenar_campos()
                habilitar()
                e1.configure(state="disabled")
                add.configure(state="disabled")
                update.configure(state="normal")
                clean.config(text='Cancelar')
                
        except IndexError, e:
                showerror("Error", e)
                
def actualizar():
        pass
                
def buscar():
        pass
