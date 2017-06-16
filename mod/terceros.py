#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from ttk import Combobox
from tkMessageBox import*
import MySQLdb
from controller import *
        
class Terceros(Frame):
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)
                
                global cedula, codigo, ref, nombre, direccion, ciudad, telefono, gcontribuyente, gcheque, titular, banco, tipocuenta, numcuenta, notas, busqueda
                global ccE, codE, tituloE, nameE, locacionE, cityE, niE, ch1, ch2, tnameE, bankCbx, tbankCbx, tcuentaE, note, lb, add, clean, delete, update
                global info
                        
                #VARIABLES
                cedula = StringVar()
                codigo = IntVar()
                ref = StringVar()
                nombre = StringVar()
                direccion = StringVar()
                ciudad = StringVar()
                telefono = StringVar()
                gcontribuyente = IntVar()
                gcheque = IntVar()
                titular = StringVar()
                banco = StringVar()
                tipocuenta = StringVar()
                numcuenta = StringVar()
                notas = StringVar()
                
                tbancos = ['Bancolombia', "Banco Bogotá", "Banco Agrario", "Banco Occidente"]

                tbanktype = ['Corriente','Ahorro']
                
                #BUSQUEDA = ["Nombre","CC/Nit"]
                busqueda = StringVar()
                busqueda.trace("w", lambda name, index, mode: buscar())
                info = IntVar()
                dato = StringVar()

                #WIDGETS

                #========================= HEADER ==============================
                
                self.titleL = Label(self, text="GESTIÓN DE TERCEROS", font="bold")
                self.titleL.pack(pady=20, side=TOP)
                
                #========================== WRAPPER ============================
                
                self.wrapper = Frame (self)
                self.wrapper.pack(side=LEFT, fill=Y)
                #Esto centro el wrapper
                #self.wrapper.pack(side=LEFT, fill=BOTH, expand=True)
                
                self.f1 = Frame(self.wrapper)
                self.f1.pack(pady=5, fill=X)#-----------------------------------
                
                self.niL = Label(self.f1, text='CC/Nit:')
                self.niL.pack(side=LEFT)
                ccE = Entry(self.f1, textvariable=cedula)
                ccE.pack(side=LEFT)
                ccE.focus_set()
                
                l3 = Label(self.f1, text='Codigo:')
                l3.pack(side=LEFT)
                codE = Entry(self.f1, textvariable=codigo)
                codE.pack(side=LEFT)
                codE.bind("<KeyRelease>", caps)
                
                self.tituloL = Label(self.f1, text='Título:')
                self.tituloL.pack(side=LEFT)
                tituloE = Entry(self.f1, textvariable=ref)
                tituloE.pack(side=LEFT)
                #tituloE.bind("<KeyRelease>", caps)
                
                self.f2 = Frame (self.wrapper)
                self.f2.pack(fill=X)#-------------------------------------------
                
                self.nameL = Label(self.f2, text='Nombre:')
                self.nameL.pack(side=LEFT)
                nameE = Entry(self.f2, textvariable=nombre)
                nameE.pack(side=LEFT, fill=X, expand=1)
                nameE.bind("<KeyRelease>", caps)
                
                self.f3 = Frame (self.wrapper)
                self.f3.pack(pady=5,fill=X)#------------------------------------
                
                self.locacionL = Label(self.f3, text='Dirección:')
                self.locacionL.pack(side=LEFT)
                locacionE = Entry(self.f3, textvariable=direccion)
                locacionE.pack(side=LEFT, fill=X, expand=1)
                locacionE.bind("<KeyRelease>", caps)
                
                self.f4 = Frame (self.wrapper)
                self.f4.pack(pady=5,fill=X)#------------------------------------
                
                self.cityL = Label(self.f4, text='Ciudad de residencia:')
                self.cityL.pack(side=LEFT)
                cityE = Entry(self.f4, textvariable=ciudad)
                cityE.pack(side=LEFT, fill=X, expand=1)
                cityE.bind("<KeyRelease>", caps)
                
                self.niL = Label(self.f4, text='Teléfono:')
                self.niL.pack(side=LEFT)
                niE = Entry(self.f4, textvariable=telefono)
                niE.pack(side=LEFT, fill=X, expand=1)

                self.f5 = Frame (self.wrapper)
                self.f5.pack(pady=5,fill=X)#------------------------------------
                
                ch1 = Checkbutton(self.f5, text="Gran Contribuyente", variable=gcontribuyente, state=DISABLED)
                ch1.pack(side=RIGHT)

                ch2 = Checkbutton(self.f5, text="Genera Cheque", variable=gcheque, state=DISABLED)
                ch2.pack(side=RIGHT)
                
                self.lf = LabelFrame(self.wrapper, text="Datos Titular")#=======
                                
                self.f6 = Frame (self.lf)
                self.f6.pack(pady=5,fill=X)#------------------------------------
                
                self.tnameL = Label(self.f6, text='Nombres:')
                self.tnameL.pack(side=LEFT)
                tnameE = Entry(self.f6, textvariable=titular)
                tnameE.pack(side=LEFT, fill=X, expand=1)
                tnameE.bind("<KeyRelease>", caps)
                
                self.f7 = Frame (self.lf)
                self.f7.pack(fill=X)#-------------------------------------------------
                
                self.tbancpL = Label(self.f7, text='Banco:')
                self.tbancpL.pack(side=LEFT)
                bankCbx = Combobox(self.f7, textvariable=banco, values=tbancos, width=12)
                bankCbx.set('')
                bankCbx.pack(side=LEFT)

                self.tbancpL = Label(self.f7, text='Tipo Cuenta:')
                self.tbancpL.pack(side=LEFT)
                tbankCbx = Combobox(self.f7, textvariable=tipocuenta, values=tbanktype, width=8)
                tbankCbx.set('')
                tbankCbx.pack(side=LEFT)

                self.tcuentaL = Label(self.f7, text='# Cuenta:')
                self.tcuentaL.pack(side=LEFT)
                tcuentaE = Entry(self.f7, textvariable=numcuenta)
                tcuentaE.pack(side=LEFT, fill=X, expand=1)
                
                self.lf.pack(fill=X, ipady=5)#================================
                
                self.f9 = Frame(self.wrapper)
                self.f9.pack(pady=5,fill=X)#--------------------

                self.notesL = Label(self.f9, text='Observaciones:')
                self.notesL.pack(side=LEFT)

                self.f10 = Frame(self.wrapper)
                self.f10.pack(pady=5,fill=X)#-------------------

                note = Text(self.f10, height=5)
                note.pack(fill=X, side=LEFT)
                
                self.fBtn = Frame(self.wrapper)
                self.fBtn.pack()#-------------------------------
        
                clean = Button(self.fBtn, text='Limpiar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=limpiar)
                clean.pack(side=RIGHT)
                
                update = Button(self.fBtn, text='Actualizar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=None, state=DISABLED)
                update.pack(side=RIGHT)
                
                add = Button(self.fBtn, text='Agregar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=Agregar)
                add.pack(side=RIGHT)
                
                #========================= ASIDE ===========================
                
                self.aside = Frame(self)
                self.aside.pack(side=TOP, fill=BOTH)
                
                self.wrap1 = Frame(self.aside)
                self.wrap1.pack()
                
                self.viewer = Label(self.wrap1, text="LISTA DE TERCEROS")
                self.viewer.pack()

                scroll = Scrollbar(self.wrap1, orient=VERTICAL)
                scroll.pack(side=RIGHT, fill=Y)
                lb = Listbox(self.wrap1, yscrollcommand=scroll.set, height=20, width=30, bg='#d8ecf3')
                scroll.config (command=lb.yview)
                lb.pack(fill=BOTH)
                lb.bind("<Double-Button-1>", callback)
                
                self.wrap2 = Frame(self.aside)
                self.wrap2.pack()
                
                self.updateBP = Button(self.wrap2, text='Cargar lista', width=20,bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=cargar_lista)
                self.updateBP.pack(fill=X)
                
                delete = Button(self.wrap2, text='Borrar', bg='navy', width=20, foreground='white', activebackground='red3', activeforeground='white', command=borrar)
                delete.pack(fill=X)
                
                edit = Button(self.wrap2, text='Modificar', bg='navy', width=20, foreground='white', activebackground='red3', activeforeground='white', command=modificar)
                edit.pack(fill=X)

                self.wrap3 = Frame(self.aside)
                self.wrap3.pack()
                
                buscador = Label(self.wrap3, text="Buscar por:")
                buscador.pack(side=LEFT)

                R1 = Radiobutton(self.wrap3, text="CC", variable=info, value=1)
                R1.pack(side=LEFT)
                R2 = Radiobutton (self.wrap3, text="Nombre", variable=info, value=2)
                R2.pack(side=LEFT)
                info.set(1)

                self.wrap4 = Frame(self.aside)
                self.wrap4.pack()
                
                E = Entry(self.wrap4, textvariable=busqueda, width=24)
                E.pack()
                E.bind("<KeyRelease>", caps)

def cargar_lista():
        try:
                connect.commit()
                display = "SELECT t_nombre FROM terceros ORDER BY t_id;"
                cursor.execute(display)
                registros = cursor.fetchall()
                lb.delete(0, END)
                for item in registros:
                        #print item
                        nombre = item[0]
                        lb.insert(END, nombre)
        except:
                showinfo ("Mensaje", "Ha ocurrido un error")
                
def limpiar():
        cedula.set("")
        codigo.set(0)
        ref.set("")
        nombre.set("")
        direccion.set("")
        ciudad.set("")
        telefono.set("")

        titular.set("")
        banco.set("")
        tipocuenta.set("")
        numcuenta.set("")
        #note.delete('1.0', '2.0')
        note.delete('1.0', END)
        
        habilitar()
        
        ccE.configure(state="normal")
        add.configure(state="normal")
        update.configure(state="disabled")
        
        ch1.configure(state="disabled")
        ch2.configure(state="disabled")

def Agregar():
        v1 = cedula.get()
        v2 = codigo.get()
        v3 = ref.get()
        v4 = nombre.get()
        v5 = direccion.get()
        v6 = ciudad.get()
        v7 = telefono.get()

        v9 = titular.get()
        v10 = banco.get()
        v11 = tipocuenta.get()
        v12 = numcuenta.get()
        v13 = note.get("1.0",END)
        
        connect.commit()
        sql = "INSERT INTO terceros (t_cc, t_cod, t_titulo, t_nombre, t_direccion, t_reside, t_telefono, t_titular, t_banco, t_tcuenta, t_numcuenta, t_notas) VALUES ('%s','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (v1,v2,v3,v4,v5,v6,v7,v9,v10,v11,v12,v13)
        cursor.execute(sql)
        showinfo ("Mensaje", "Datos guardados")
        
        limpiar()
        cargar_lista()
        
def borrar():
        try:
                t = lb.curselection()
                value = lb.get(t[0])
                delete = """DELETE FROM terceros WHERE t_nombre=("%s");""" % (value)
                cursor.execute(delete)
                connect.commit()
                lb.delete(t)
                showinfo("mensaje", "Dato Borrado!")
                lb.delete(0, END)
                cargar_lista()
                limpiar()
                
        except MySQLdb.IntegrityError, e:
                showerror("Error", e)
                #showerror ('Mensaje', "No se puede borrar o actualizar porque hace parte de una relación.")
        except IndexError, i:
                showerror("Error", i)

def bloquear():
        ccE.configure(state="disabled")
        codE.configure(state="disabled")
        tituloE.configure(state="disabled")
        nameE.configure(state="disabled")
        locacionE.configure(state="disabled")
        cityE.configure(state="disabled")
        niE.configure(state="disabled")
        ch1.configure(state="disabled")
        ch2.configure(state="disabled")
        tnameE.configure(state="disabled")
        bankCbx.configure(state="disabled")
        tbankCbx.configure(state="disabled")
        tcuentaE.configure(state="disabled")
        note.configure(state="disabled")

# LLENAR CAMPOS CON DOBLE CLIC
def callback(event):
    llenar_campos()
    
def llenar_campos():
        limpiar()
        limpiar()
        i = lb.curselection()[0]
        valor = lb.get(i)
        edit = """SELECT * FROM terceros WHERE t_nombre=("%s");""" % (valor)
        cursor.execute(edit)
        result = cursor.fetchall()
        connect.commit()
        for item in result:
                d1 = item[1] #CC/nit
                d2 = item[2] #Codigo
                d3 = item[3] #título
                d4 = item[4] #nombre
                d5 = item[5] #direccion
                d6 = item[6] #ciudad
                d7 = item[7] #telefono
                d8 = item[8] #titular
                d9 = item[9] #banco
                d10 = item[10] #tipo de cuenta
                d11 = item[11] #numero de cuenta
                d12 = item[12] #notas
                
                cedula.set(d1)
                codigo.set(d2)
                ref.set(d3)
                nombre.set(d4)
                direccion.set(d5)
                ciudad.set(d6)
                telefono.set(d7)
                titular.set(d8)
                banco.set(d9)
                tipocuenta.set(d10)
                numcuenta.set(d11)
                note.insert('1.0',d12)
                
                bloquear()
                
def habilitar():
        ccE.configure(state="normal")
        codE.configure(state="normal")
        tituloE.configure(state="normal")
        nameE.configure(state="normal")
        locacionE.configure(state="normal")
        cityE.configure(state="normal")
        niE.configure(state="normal")
        ch1.configure(state="normal")
        ch2.configure(state="normal")
        tnameE.configure(state="normal")
        bankCbx.configure(state="normal")
        tbankCbx.configure(state="normal")
        tcuentaE.configure(state="normal")
        note.configure(state="normal")
        
def modificar():
        try:
                llenar_campos()
                habilitar()
                ccE.configure(state="disabled")
                add.configure(state="disabled")
                update.configure(state="normal")
                clean.config(text='Cancelar')
                
        except IndexError, e:
                showerror("Error", e)

def actualizar():
        try:
                v1 = cedula.get()
                v2 = codigo.get()
                v3 = ref.get()
                v4 = nombre.get()
                v5 = direccion.get()
                v6 = ciudad.get()
                v7 = telefono.get()
                #v7 = gcontribuyente.get()
                #v8 = gcheque.get()
                v9 = titular.get()
                v10 = banco.get()
                v11 = tipocuenta.get()
                v12 = numcuenta.get()
                v13 = note.get("1.0",END)
                
                connect.commit()
                sql = "UPDATE terceros SET t_cod='%d', t_titulo='%s', t_nombre='%s', t_direccion='%s', t_reside='%s', t_telefono='%s', t_titular='%s', t_banco='%s', t_tcuenta='%s', t_numcuenta='%s', t_notas='%s' WHERE t_cc='%s'" %(v2,v3,v4,v5,v6,v7,v9,v10,v11,v12,v13,v1)
                cursor.execute(sql)
                showinfo ("Mensaje", "Datos actualizados!")
                
                cargar_lista()
                limpiar()
                #habilitar()
                
                ccE.configure(state="normal")
                add.configure(state="normal")
                update.configure(state="disabled")
        except TypeError, e:
                showerror("Error", e)
                
        except MySQLdb.IntegrityError, e:
                showerror("Error", e)
        
def buscar():
        r = info.get()
        if r == 1:
                dato = busqueda.get()
                connect.commit()
                display = """SELECT t_nombre FROM terceros WHERE t_cc=("%s")""" % (dato)
                cursor.execute(display)
                registros = cursor.fetchall()
                lb.delete(0, END)
                for item in registros:
                        lb.insert(END, item)
        else:
                dato = busqueda.get()
                connect.commit()
                display = """SELECT t_nombre FROM terceros WHERE t_nombre LIKE '%s';""" % (dato + "%")
                cursor.execute(display)
                registros = cursor.fetchall()
                lb.delete(0, END)
                for item in registros:
                        lb.insert(END, item)
                        
        #try:
        #        dato = busqueda.get()
        #        connect.commit()
        #        display = """SELECT t_nombre FROM terceros WHERE t_cc=("%s");""" % (dato)
        #        cursor.execute(display)
        #        registros = cursor.fetchall()
        #        lb.delete(0, END)
        #        for item in registros:
        #                lb.insert(END, item)
        #except TypeError, e:
        #        showerror("Error", e)
        #        
        #except MySQLdb.IntegrityError, e:
        #        showerror("Error", e)
                
# CONVIERTE LA ENTRADA DE LOS ENTRIES EN MAYÚSCULA
def caps(event):
        cedula.set(cedula.get().upper())
        ref.set(ref.get().upper())
        nombre.set(nombre.get().upper())
        direccion.set(direccion.get().upper())
        ciudad.set(ciudad.get().upper())
        telefono.set(telefono.get().upper())
        titular.set(titular.get().upper())
        banco.set(banco.get().upper())
        tipocuenta.set(tipocuenta.get().upper())
        numcuenta.set(numcuenta.get().upper())
        busqueda.set(busqueda.get().upper())
