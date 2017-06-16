#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from ttk import Combobox, Notebook
from tkMessageBox import*
import MySQLdb
from controller import *

class Arrendatarios(Frame):
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)
                
                #VARIABLES GLOBALES
                global cedula, titulo, residencia, nombres, apellidos, direccion, telefono, envio, correo, celular, dia, mes, profesion, empresa, oficina, tel, telfax, banco, tcuenta, numcuenta, tipopersona, retefuente, reteiva, gcontribuyente, gfactura, gcheque, notas, co1cc, co1nombres, co1dir, co1tel1, co1cargo, co1empresa, co1oficina, co1tel2, co2cc, co2nombres, co2dir, co2tel1, co2cargo, co2empresa, co2oficina, co2tel2, co3cc, co3nombres, co3dir, co3tel1, co3cargo, co3empresa, co3oficina, co3tel2, lb, note, busqueda, dato, E
                
                #INSTANCIEAS DE LOS WIDGETS
                global codeE, refE, cityE, nameE, lastnameE, adressE, phoneE, mailE, emailE, mobileE, birthdayE, birthdayCbx, ocupationE, companyE, ofiE, officetelE, faxE, bankCbx, banktypeCbx, numbankE, personR1, personR2, Ch1, Ch2, Ch3, Ch4, Ch5, note, cc1E, name1E, adress1E, phone1E, job1E, jobphone1E, office1E, officetel1E, cc2E, name2E, adress2E, phone2E, job2E, jobphone2E, office2E, officetel2E, cc3E, name3E, adress3E, phone3E, job3E, jobphone3E, office3E, officetel3E, add, update, delete, clean, cancel
                global info, _arrendatarios

                _arrendatarios = dict()
                
                #Variables
                cedula = StringVar()
                titulo = StringVar()
                residencia = StringVar()
                nombres = StringVar()
                apellidos = StringVar()
                direccion = StringVar()
                telefono = StringVar()
                envio = StringVar()
                correo = StringVar()
                celular = StringVar()
                dia = IntVar()
                mes = StringVar()
                meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto","Septiembre", "Octubre", "Noviembre", "Diciembre"]
                profesion = StringVar()
                empresa = StringVar()
                oficina = StringVar()
                tel = StringVar()
                telfax = StringVar()
                banco = StringVar()
                bancos = ['Bancolombia', "Banco Bogotá", "Banco Agrario", "Banco Occidente"]
                banktype = ['Corriente','Ahorro']
                tcuenta = StringVar()
                numcuenta = StringVar()
                tipopersona = IntVar()  
                retefuente = IntVar()
                reteiva = IntVar()
                gcontribuyente = IntVar()
                gfactura = IntVar()
                gcheque = IntVar()
                notas = StringVar()
                
                #----------------------------
                
                co1cc = StringVar()
                co1nombres = StringVar()
                co1dir = StringVar()
                co1tel1 = StringVar()
                co1cargo = StringVar()
                co1empresa = StringVar()
                co1oficina = StringVar()
                co1tel2 = StringVar()
                
                co2cc = StringVar()
                co2nombres = StringVar()
                co2dir = StringVar()
                co2tel1 = StringVar()
                co2cargo = StringVar()
                co2empresa = StringVar()
                co2oficina = StringVar()
                co2tel2 = StringVar()
                
                co3cc = StringVar()
                co3nombres = StringVar()
                co3dir = StringVar()
                co3tel1 = StringVar()
                co3cargo = StringVar()
                co3empresa = StringVar()
                co3oficina = StringVar()
                co3tel2 = StringVar()
                
                #BUSQUEDA = ["Nombre","CC/Nit"]
                busqueda = StringVar()
                busqueda.trace("w", lambda name, index, mode: buscar())
                info = IntVar()
                dato = StringVar()

                #WIDGETS
                
                #========================= HEADER ===========================
                
                self.header = Label(self, text="GESTIÓN DE ARRENDATARIOS", font="bold")
                self.header.pack(pady=20, side=TOP)
                
                #========================= WRAPPER ===========================
                
                self.wrapper = Frame (self)
                self.wrapper.pack(side=LEFT, fill=Y)
                #Esto centro el wrapper
                #self.wrapper.pack(side=LEFT, fill=BOTH, expand=True)
                
                #================ NOTEBOOK =============>
                
                self.nb = Notebook(self.wrapper)
                
                #-----------------------> TAB 1
                
                self.tab1 = Frame (self.nb)
                
                self.f0 = Frame(self.tab1)#Para dejar espacio entre Tab y Label
                self.f0.pack(fill=X, pady=10)#-------------------------------

                #======================= DATOS GENERALES =======================
                
                self.f0 = Frame(self.tab1)
                self.f0.pack(pady=5,fill=X)#------------------------------------
                
                self.codeL = Label(self.f0, text='CC:')
                self.codeL.pack(side=LEFT)
                codeE = Entry(self.f0, textvariable=cedula, width=10)
                codeE.pack(side=LEFT, fill=X, expand=1)
                codeE.focus_set()

                self.refL = Label(self.f0, text='Título:')
                self.refL.pack(side=LEFT)
                refE = Entry(self.f0, textvariable=titulo, width=10)
                refE.pack(side=LEFT)
                #refE.bind("<KeyRelease>", caps)

                self.cityL = Label(self.f0, text='Ciudad de residencia:')
                self.cityL.pack(side=LEFT)
                cityE = Entry(self.f0, textvariable=residencia, width=10)
                cityE.pack(side=LEFT)
                cityE.bind("<KeyRelease>", caps)

                self.f1 = Frame(self.tab1)#-------------------------------
                self.f1.pack(pady=5,fill=X)

                self.nameL = Label(self.f1, text='Nombres:')
                self.nameL.pack(side=LEFT)
                nameE = Entry(self.f1, textvariable=nombres)
                nameE.pack(side=LEFT, fill=X, expand=1)
                nameE.bind("<KeyRelease>", caps)

                self.lastnameL = Label(self.f1, text='Apellidos:')
                self.lastnameL.pack(side=LEFT)
                lastnameE = Entry(self.f1, textvariable=apellidos)
                lastnameE.pack(side=LEFT, fill=X, expand=1)
                lastnameE.bind("<KeyRelease>", caps)

                self.f2 = Frame(self.tab1)
                self.f2.pack(pady=5,fill=X)#------------------------------------

                self.adressL = Label(self.f2, text='Dir. Casa:')
                self.adressL.pack(side=LEFT)
                adressE = Entry(self.f2, textvariable=direccion)
                adressE.pack(side=LEFT, fill=X, expand=1)
                adressE.bind("<KeyRelease>", caps)

                self.phoneL = Label(self.f2, text='Teléfono:')
                self.phoneL.pack(side=LEFT)
                phoneE = Entry(self.f2, textvariable=telefono, width=20)
                phoneE.pack(side=LEFT)

                self.f3 = Frame(self.tab1)
                self.f3.pack(pady=5,fill=X)#---------------------------

                self.mailL = Label(self.f3, text='Dir. Correspondencia:')
                self.mailL.pack(side=LEFT)
                mailE = Entry(self.f3, textvariable=envio)
                mailE.pack(side=LEFT, fill=X, expand=1)
                mailE.bind("<KeyRelease>", caps)

                self.emailL = Label(self.f3, text='Email:')
                self.emailL.pack(side=LEFT)
                emailE = Entry(self.f3, textvariable=correo, width=15)
                emailE.pack(side=LEFT, fill=X, expand=1)

                self.f4 = Frame(self.tab1)
                self.f4.pack(pady=5,fill=X)#---------------------------
                
                self.mobileL = Label(self.f4, text='Celular:')
                self.mobileL.pack(side=LEFT)
                mobileE = Entry(self.f4, textvariable=celular, width=10)
                mobileE.pack(side=LEFT, fill=X, expand=1)

                self.birthdayL = Label(self.f4, text='Cumpleaños:')
                self.birthdayL.pack(side=LEFT)

                self.birthdayL2 = Label(self.f4, text='Día:')
                self.birthdayL2.pack(padx=5,side=LEFT)

                birthdayE = Entry(self.f4, textvariable=dia, width=3)
                birthdayE.pack(side=LEFT)
                
                #s = Spinbox(self.f4, from_=1, to=31,textvariable=dia, width=3)
                #s.pack(side=LEFT)

                self.birthdayL3 = Label(self.f4, text='Mes:')
                self.birthdayL3.pack(padx=5,side=LEFT)

                birthdayCbx = Combobox(self.f4, textvariable=mes, values=meses, width=10)
                birthdayCbx.set('Enero')
                birthdayCbx.pack(side=LEFT)

                self.lf = LabelFrame(self.tab1, text="Info laboral")#========

                self.f5 = Frame(self.lf)
                self.f5.pack(pady=5,fill=X)#---------------------------

                self.ocupationL = Label(self.f5, text='Profesión:')
                self.ocupationL.pack(side=LEFT)
                ocupationE = Entry(self.f5, textvariable=profesion, width=20)
                ocupationE.pack(side=LEFT, fill=X, expand=1)
                ocupationE.bind("<KeyRelease>", caps)

                self.companyL = Label(self.f5, text='Empresa:')
                self.companyL.pack(side=LEFT)
                companyE = Entry(self.f5, textvariable=empresa, width=24)
                companyE.pack(side=LEFT, fill=X, expand=1)
                companyE.bind("<KeyRelease>", caps)

                self.f6 = Frame(self.lf)
                self.f6.pack(pady=5,fill=X)#--------------------

                self.ofiL = Label(self.f6, text='Dir. Oficina:')
                self.ofiL.pack(side=LEFT)
                ofiE = Entry(self.f6, textvariable=oficina)
                ofiE.pack(side=LEFT, fill=X, expand=1)
                ofiE.bind("<KeyRelease>", caps)

                self.officetelL = Label(self.f6, text='Tel:')
                self.officetelL.pack(side=LEFT)
                officetelE = Entry(self.f6, textvariable=tel, width=10)
                officetelE.pack(fill=X, side=LEFT)

                self.faxL = Label(self.f6, text='Fax:')
                self.faxL.pack(side=LEFT)
                faxE = Entry(self.f6, textvariable=telfax, width=10)
                faxE.pack(side=LEFT)
                
                self.lf.pack(fill=X)#===========================================
        
                self.f7 = Frame(self.tab1)
                self.f7.pack(pady=5,fill=X)#-----------------

                self.bankL = Label(self.f7, text='Banco:')
                self.bankL.pack(side=LEFT)

                bankCbx = Combobox(self.f7, textvariable=banco, values=bancos, width=12)
                bankCbx.set('')
                bankCbx.pack(side=LEFT)

                self.bankL = Label(self.f7, text='Tipo Cuenta:')
                self.bankL.pack(side=LEFT)

                banktypeCbx = Combobox(self.f7, textvariable=tcuenta, values=banktype, width=10)
                banktypeCbx.set('')
                banktypeCbx.pack(side=LEFT)

                self.numbankL = Label(self.f7, text="# Cuenta:")
                self.numbankL.pack(side=LEFT)
                numbankE = Entry(self.f7, textvariable=numcuenta, width=13)
                numbankE.pack(side=LEFT, fill=X, expand=1)

                self.f8 = Frame(self.tab1)
                self.f8.pack(pady=5,fill=X)#--------------------

                self.personL = Label(self.f8, text='Tipo Persona:')
                self.personL.pack(side=LEFT)
                personR1 = Radiobutton(self.f8, text="Natural", variable=tipopersona, value=1)
                personR1.pack(padx=20,side=LEFT)
                personR2 = Radiobutton (self.f8, text="Jurídica", variable=tipopersona, value=2)
                personR2.pack(padx=20,side=LEFT)
                
                self.f = Frame(self.tab1)
                self.f.pack(pady=5,fill=X)#------------------------------------

                Ch1 = Checkbutton(self.f, text="Retefuente", variable=retefuente)
                Ch1.pack(side=LEFT)
                
                Ch2 = Checkbutton(self.f, text="Rete IVA", variable=reteiva)
                Ch2.pack(side=LEFT)
                
                Ch3 = Checkbutton(self.f, text="Gran Contribuyente", variable=gcontribuyente)
                Ch3.pack(side=LEFT)
                
                Ch4 = Checkbutton(self.f, text="Genera Factura", variable=gfactura)
                Ch4.pack(side=LEFT)
                
                Ch5 = Checkbutton(self.f, text="Genera Cheque", variable=gcheque)
                Ch5.pack(side=LEFT)

                self.f9 = Frame(self.tab1)
                self.f9.pack(pady=5,fill=X)#--------------------

                self.notesL = Label(self.f9, text='Observaciones:')
                self.notesL.pack(side=LEFT)

                self.f10 = Frame(self.tab1)
                self.f10.pack(pady=5,fill=X)#-------------------

                note = Text(self.f10, height=5)
                note.pack(fill=X, side=LEFT)
                #note.bind("<KeyRelease>", caps)
                
                #-----------------------> TAB 2
                
                self.tab2 = Frame (self.nb)
                self.tab2.pack()
                
                self.f0 = Frame(self.tab2)#Para dejar espacio entre Tab y Label
                self.f0.pack(fill=X, pady=10)#----------------------------------
                
                #===================== INFORMACIÓN CODEUDOR ====================
                
                self.lf1 = LabelFrame(self.tab2, text="Codeudor 1")
                
                self.f0 = Frame(self.lf1)
                self.f0.pack(fill=X, pady=5)#-------------------------------
                
                self.ccL = Label(self.f0, text='CC:')
                self.ccL.pack(side=LEFT)
                cc1E = Entry(self.f0, textvariable= co1cc, width=10)
                cc1E.pack(side=LEFT, fill=X, expand=1)
                
                self.nameL = Label(self.f0, text='Nombres:')
                self.nameL.pack(side=LEFT)
                name1E = Entry(self.f0, textvariable=co1nombres)
                name1E.pack(side=LEFT, fill=X, expand=1)
                name1E.bind("<KeyRelease>", caps)
                
                self.f1 = Frame(self.lf1)
                self.f1.pack(fill=X, pady=5)#-------------------------------
                
                self.adressL = Label(self.f1, text='Dir. Casa:')
                self.adressL.pack(side=LEFT)
                adress1E = Entry(self.f1, textvariable=co1dir)
                adress1E.pack(side=LEFT, fill=X, expand=1)
                adress1E.bind("<KeyRelease>", caps)

                self.phoneL = Label(self.f1, text='Tel:')
                self.phoneL.pack(side=LEFT)
                phone1E = Entry(self.f1, textvariable=co1tel1, width=20)
                phone1E.pack(side=LEFT)
                
                self.f2 = Frame(self.lf1)
                self.f2.pack(fill=X, pady=5)#-------------------------------
                
                self.jobL = Label(self.f2, text='Cargo:')
                self.jobL.pack(side=LEFT)
                job1E = Entry(self.f2, textvariable=co1cargo, width=20)
                job1E.pack(side=LEFT, fill=X, expand=1)
                job1E.bind("<KeyRelease>", caps)

                self.phoneL = Label(self.f2, text='Empresa:')
                self.phoneL.pack(side=LEFT)
                jobphone1E = Entry(self.f2, textvariable=co1empresa)
                jobphone1E.pack(side=LEFT)
                jobphone1E.bind("<KeyRelease>", caps)
                
                self.f3 = Frame(self.lf1)
                self.f3.pack(fill=X, pady=5)#-------------------------------
                
                self.officeL = Label(self.f3, text='Dir. Oficina:')
                self.officeL.pack(side=LEFT)
                office1E = Entry(self.f3, textvariable=co1oficina)
                office1E.pack(side=LEFT, fill=X, expand=1)
                office1E.bind("<KeyRelease>", caps)

                self.officetelL = Label(self.f3, text='Tel:')
                self.officetelL.pack(side=LEFT)
                officetel1E = Entry(self.f3, textvariable=co1tel2, width=20)
                officetel1E.pack(fill=X, side=LEFT)
                
                self.lf1.pack(fill=X, ipady=5)#=================================
                
                self.lf2 = LabelFrame(self.tab2, text="Codeudor 2")
                
                self.f0 = Frame(self.lf2)
                self.f0.pack(fill=X, pady=5)#-------------------------------
                
                self.ccL = Label(self.f0, text='CC:')
                self.ccL.pack(side=LEFT)
                cc2E = Entry(self.f0, textvariable=co2cc, width=10)
                cc2E.pack(side=LEFT, fill=X, expand=1)
                
                self.nameL = Label(self.f0, text='Nombres:')
                self.nameL.pack(side=LEFT)
                name2E = Entry(self.f0, textvariable=co2nombres)
                name2E.pack(side=LEFT, fill=X, expand=1)
                name2E.bind("<KeyRelease>", caps)
                
                self.f1 = Frame(self.lf2)
                self.f1.pack(fill=X, pady=5)#-------------------------------
                
                self.adressL = Label(self.f1, text='Dir. Casa:')
                self.adressL.pack(side=LEFT)
                adress2E = Entry(self.f1, textvariable=co2dir)
                adress2E.pack(side=LEFT, fill=X, expand=1)
                adress2E.bind("<KeyRelease>", caps)

                self.phoneL = Label(self.f1, text='Tel:')
                self.phoneL.pack(side=LEFT)
                phone2E = Entry(self.f1, textvariable=co2tel1, width=20)
                phone2E.pack(side=LEFT)
                
                self.f2 = Frame(self.lf2)
                self.f2.pack(fill=X, pady=5)#-------------------------------
                
                self.adressL = Label(self.f2, text='Cargo:')
                self.adressL.pack(side=LEFT)
                job2E = Entry(self.f2, textvariable=co2cargo, width=20)
                job2E.pack(side=LEFT, fill=X, expand=1)
                job2E.bind("<KeyRelease>", caps)

                self.phoneL = Label(self.f2, text='Empresa:')
                self.phoneL.pack(side=LEFT)
                jobphone2E = Entry(self.f2, textvariable=co2empresa)
                jobphone2E.pack(side=LEFT)
                jobphone2E.bind("<KeyRelease>", caps)
                
                self.f3 = Frame(self.lf2)
                self.f3.pack(fill=X, pady=5)#-------------------------------
                
                self.officeL = Label(self.f3, text='Dir. Oficina:')
                self.officeL.pack(side=LEFT)
                office2E = Entry(self.f3, textvariable=co2oficina)
                office2E.pack(side=LEFT, fill=X, expand=1)
                office2E.bind("<KeyRelease>", caps)

                self.officetelL = Label(self.f3, text='Tel:')
                self.officetelL.pack(side=LEFT)
                officetel2E = Entry(self.f3, textvariable=co2tel2, width=20)
                officetel2E.pack(fill=X, side=LEFT)
                
                self.lf2.pack(fill=X, ipady=5)#=================================
                
                self.lf3 = LabelFrame(self.tab2, text="Codeudor 3")
                
                self.f0 = Frame(self.lf3)
                self.f0.pack(fill=X, pady=5)#-------------------------------
                
                self.ccL = Label(self.f0, text='CC:')
                self.ccL.pack(side=LEFT)
                cc3E = Entry(self.f0, textvariable=co3cc, width=10)
                cc3E.pack(side=LEFT, fill=X, expand=1)
                
                self.nameL = Label(self.f0, text='Nombres:')
                self.nameL.pack(side=LEFT)
                name3E = Entry(self.f0, textvariable=co3nombres)
                name3E.pack(side=LEFT, fill=X, expand=1)
                name3E.bind("<KeyRelease>", caps)
                
                self.f1 = Frame(self.lf3)
                self.f1.pack(fill=X, pady=5)#-------------------------------
                
                self.adressL = Label(self.f1, text='Dir. Casa:')
                self.adressL.pack(side=LEFT)
                adress3E = Entry(self.f1, textvariable=co3dir)
                adress3E.pack(side=LEFT, fill=X, expand=1)
                adress3E.bind("<KeyRelease>", caps)

                self.phoneL = Label(self.f1, text='Tel:')
                self.phoneL.pack(side=LEFT)
                phone3E = Entry(self.f1, textvariable=co3tel1, width=20)
                phone3E.pack(side=LEFT)
                
                self.f2 = Frame(self.lf3)
                self.f2.pack(fill=X, pady=5)#-------------------------------
                
                self.adressL = Label(self.f2, text='Cargo:')
                self.adressL.pack(side=LEFT)
                job3E = Entry(self.f2, textvariable=co3cargo, width=20)
                job3E.pack(side=LEFT, fill=X, expand=1)
                job3E.bind("<KeyRelease>", caps)

                self.phoneL = Label(self.f2, text='Empresa:')
                self.phoneL.pack(side=LEFT)
                jobphone3E = Entry(self.f2, textvariable=co3empresa)
                jobphone3E.pack(side=LEFT)
                jobphone3E.bind("<KeyRelease>", caps)
                
                self.f3 = Frame(self.lf3)
                self.f3.pack(fill=X, pady=5)#-------------------------------
                
                self.officeL = Label(self.f3, text='Dir. Oficina:')
                self.officeL.pack(side=LEFT)
                office3E = Entry(self.f3, textvariable=co3oficina)
                office3E.pack(side=LEFT, fill=X, expand=1)
                office3E.bind("<KeyRelease>", caps)

                self.officetelL = Label(self.f3, text='Tel:')
                self.officetelL.pack(side=LEFT)
                officetel3E = Entry(self.f3, textvariable=co3tel2, width=20)
                officetel3E.pack(fill=X, side=LEFT)
                
                self.lf3.pack(fill=X, ipady=5)#=================================
                
                #---------------------------------------------------------------
                
                self.nb.add (self.tab1, text="Datos Generales")
                self.nb.add(self.tab2, text="Información Codeudor")
                
                self.nb.pack()

                #=========================== BOTONES ===========================
                
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
                
                self.viewer = Label(self.wrap1, text="LISTA DE ARRENDATARIOS")
                self.viewer.pack()

                scroll = Scrollbar(self.wrap1, orient=VERTICAL)
                scroll.pack(side=RIGHT, fill=Y)
                
                lb = Listbox(self.wrap1, yscrollcommand=scroll.set, height=20, width=30, bg='#d8ecf3')
                scroll.config (command=lb.yview)
                lb.pack(fill=BOTH)
                lb.bind("<Double-Button-1>", callback)
                
                self.wrap2 = Frame(self.aside)
                self.wrap2.pack()
                
                load = Button(self.wrap2, text='Cargar lista', width=20, bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=cargar_lista)
                load.pack(fill=X)
                
                delete = Button(self.wrap2, text='Borrar', width=20, bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=borrar)
                delete.pack(fill=X)
                
                edit = Button(self.wrap2, text='Modificar', width=20, bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=modificar)
                edit.pack(fill=X)
                
                self.wrap3 = Frame(self.aside)
                self.wrap3.pack()
                
                buscador = Label(self.wrap3, text="Buscar por:")
                buscador.pack(side=LEFT)
                
                R1 = Radiobutton(self.wrap3, text="CC", variable=info, value=1)
                R1.pack(side=LEFT)
                R2 = Radiobutton (self.wrap3, text="Apellido", variable=info, value=2)
                R2.pack(side=LEFT)
                info.set(1)
                
                self.wrap4 = Frame(self.aside)
                self.wrap4.pack()
                
                E = Entry(self.wrap4, textvariable=busqueda, width=24)
                E.pack()
                E.bind("<KeyRelease>", caps)
                
                """
                buscador = Label(self.wrap2, text="Buscar por CC:")
                buscador.pack()
                E = Entry(self.wrap2, textvariable=busqueda, width=24)
                E.pack()
                E.bind("<KeyRelease>", caps)
                """

def cargar_lista():
        try:
                connect.commit()
                cursor.execute("SELECT a_nombres, a_apellidos FROM arrendatarios order by a_nombres")
                registros = cursor.fetchall()
                lb.delete(0, END)
                for item in registros:
                        nombres = item[0]
                        apellidos = item[1]
                        nombre_completo = nombres + ' ' + apellidos
                        _arrendatarios[nombre_completo] = [nombres, apellidos]
                        lb.insert(END, nombre_completo)
        except:
                showerror("Mensaje", "Ha ocurrido un error")
                
# NUEVO / CANCELAR
def limpiar():
        clean.config(text='Limpiar')
        cedula.set("")
        titulo.set("")
        residencia.set("")
        nombres.set("")
        apellidos.set("")
        direccion.set("")
        telefono.set("")
        envio.set("")
        correo.set("")
        celular.set("")
        dia.set(0)
        mes.set('Enero')
        profesion.set("")
        empresa.set("")
        oficina.set("")
        tel.set("")
        telfax.set("")
        banco.set("")
        tcuenta.set("")
        numcuenta.set("")
        tipopersona.set(0)
        retefuente.set(0)
        reteiva.set(0)
        gcontribuyente.set(0)
        gfactura.set(0)
        gcheque.set(0)
        #note.delete('1.0', '2.0')
        note.delete('1.0', END)
        
        co1cc.set("")
        co1nombres.set("")
        co1dir.set("")
        co1tel1.set("")
        co1cargo.set("")
        co1empresa.set("")
        co1oficina.set("")
        co1tel2.set("")
        
        co2cc.set("")
        co2nombres.set("")
        co2dir.set("")
        co2tel1.set("")
        co2cargo.set("")
        co2empresa.set("")
        co2oficina.set("")
        co2tel2.set("")
        
        co3cc.set("")
        co3nombres.set("")
        co3dir.set("")
        co3tel1.set("")
        co3cargo.set("")
        co3empresa.set("")
        co3oficina.set("")
        co3tel2.set("")
        
        habilitar()
        note.delete('1.0', END)
        
        codeE.configure(state="normal")
        add.configure(state="normal")
        update.configure(state="disabled")
        
def agregar():
        d1 = cedula.get()
        d2 = titulo.get()
        d3 = residencia.get()
        d4 = nombres.get()
        d5 = apellidos.get()
        d6 = direccion.get()
        d7 = telefono.get()
        d8 = envio.get()
        d9 = correo.get()
        d10 = celular.get()
        d11 = dia.get()
        d12 = mes.get()
        anio = 0
        y = anio
        if d12 == 'Enero':
                d12 = 1
        if d12 == 'Febrero':
                d12 = 2
        if d12 == 'Marzo':
                d12 = 3
        if d12 == 'Abril':
                d12 = 4
        if d12 == 'Mayo':
                d12 = 5
        if d12 == 'Junio':
                d12 = 6
        if d12 == 'Julio':
                d12 = 7
        if d12 == 'Agosto':
                d12 = 8
        if d12 == 'Septiembre':
                d12 = 9
        if d12 == 'Octubre':
                d12 = 10
        if d12 == 'Noviembre':
                d12 = 11
        if d12 == 'Diciembre':
                d12 = 12
        cumple = "%d-%d-%s" %(y,d12,d11)
        d13 = profesion.get()
        d14 = empresa.get()
        d15 = oficina.get()
        d16 = tel.get()
        d17 = telfax.get()
        d18 = banco.get()
        d19 = tcuenta.get()
        d20 = numcuenta.get()
        d21 = tipopersona.get()
        d22 = retefuente.get()
        d23 = reteiva.get()
        d24 = gcontribuyente.get()
        d25 = gfactura.get()
        d26 = gcheque.get()
        d27 = note.get("1.0",END)
        
        d28 = co1cc.get()
        d29 = co1nombres.get()
        d30 = co1dir.get()
        d31 = co1tel1.get()
        d32 = co1cargo.get()
        d33 = co1empresa.get()
        d34 = co1oficina.get()
        d35 = co1tel2.get()
        
        d36 = co2cc.get()
        d37 = co2nombres.get()
        d38 = co2dir.get()
        d39 = co2tel1.get()
        d40 = co2cargo.get()
        d41 = co2empresa.get()
        d42 = co2oficina.get()
        d43 = co2tel2.get()
        
        d44 = co3cc.get()
        d45 = co3nombres.get()
        d46 = co3dir.get()
        d47 = co3tel1.get()
        d48 = co3cargo.get()
        d49 = co3empresa.get()
        d50 = co3oficina.get()
        d51 = co3tel2.get()
        
        connect.commit()
        sql = "INSERT INTO arrendatarios (a_cc, a_titulo, a_reside, a_nombres, a_apellidos, a_direccion, a_telefono, a_envio, a_email, a_celular, a_dia, a_mes, a_cumple, a_profesion, a_empresa, a_oficina, a_tel, a_fax, a_banco, a_tcuenta, a_numcuenta, a_tpersona, a_retefuente, a_reteiva, a_contribuyente, a_gfactura, a_gcheque, a_nota, co1_cc, co1_nombres, co1_dir, co1_tel1, co1_cargo, co1_empresa, co1_oficina, co1_tel2, co2_cc, co2_nombres, co2_dir, co2_tel1, co2_cargo, co2_empresa, co2_oficina, co2_tel2, co3_cc, co3_nombres, co3_dir, co3_tel1, co3_cargo, co3_empresa, co3_oficina, co3_tel2) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%d', '%d', '%d', '%d', '%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, cumple, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27, d28, d29, d30, d31, d32, d33, d34, d35, d36, d37, d38, d39, d40, d41, d42, d43, d44, d45, d46, d47, d48, d49, d50, d51)
        cursor.execute(sql)
        showinfo ("Mensaje", "Datos guardados")
        cargar_lista()
        limpiar()
        
        #except MySQLdb.IntegrityError, e:
        #       showerror("Error", e)
                #showerror ('Mensaje', "Debe llenar los campos obligatorios!")
                
def borrar():
        try:
                k = lb.curselection()
                value = lb.get(k[0])
                if askyesno("Salir", "¿Desea borrar este inquilino?"):
                        delete = """DELETE FROM arrendatarios WHERE a_nombres=("%s");""" % (value)
                        cursor.execute(delete)
                        connect.commit()
                        lb.delete(k)
                        showinfo("mensaje", "Dato Borrado!")
                        lb.delete(0, END)
                        cargar_lista()
                        limpiar()
                        
        except MySQLdb.IntegrityError, e:
                showerror("Error", e)
                #showerror ('Mensaje', "No se puede borrar o actualizar porque hace parte de una relación.")
        except IndexError, i:
                showerror("Error", i)

# BLOQUEAR LOS CAMPO CUANDO SE CARGAN CON DOBLE CLIC (LLENAR):
def bloquear():
        codeE.configure(state="disabled")
        refE.configure(state="disabled")
        cityE.configure(state="disabled")
        nameE.configure(state="disabled")
        lastnameE.configure(state="disabled")
        adressE.configure(state="disabled")
        phoneE.configure(state="disabled")
        mailE.configure(state="disabled")
        emailE.configure(state="disabled")
        mobileE.configure(state="disabled")
        birthdayE.configure(state="disabled")
        birthdayCbx.configure(state="disabled")
        ocupationE.configure(state="disabled")
        companyE.configure(state="disabled")
        ofiE.configure(state="disabled")
        officetelE.configure(state="disabled")
        faxE.configure(state="disabled")
        bankCbx.configure(state="disabled")
        banktypeCbx.configure(state="disabled")
        numbankE.configure(state="disabled")
        personR1.configure(state="disabled")
        personR2.configure(state="disabled")
        Ch1.configure(state="disabled")
        Ch2.configure(state="disabled")
        Ch3.configure(state="disabled")
        Ch4.configure(state="disabled")
        Ch5.configure(state="disabled")
        note.configure(state="disabled")

        cc1E.configure(state="disabled")
        name1E.configure(state="disabled")
        adress1E.configure(state="disabled")
        phone1E.configure(state="disabled")
        job1E.configure(state="disabled")
        jobphone1E.configure(state="disabled")
        office1E.configure(state="disabled")
        officetel1E.configure(state="disabled")

        cc2E.configure(state="disabled")
        name2E.configure(state="disabled")
        adress2E.configure(state="disabled")
        phone2E.configure(state="disabled")
        job2E.configure(state="disabled")
        jobphone2E.configure(state="disabled")
        office2E.configure(state="disabled")
        officetel2E.configure(state="disabled")

        cc3E.configure(state="disabled")
        name3E.configure(state="disabled")
        adress3E.configure(state="disabled")
        phone3E.configure(state="disabled")
        job3E.configure(state="disabled")
        jobphone3E.configure(state="disabled")
        office3E.configure(state="disabled")
        officetel3E.configure(state="disabled")

# LLENAR CAMPOS CON DOBLE CLIC
def callback(event):
    llenar_campos()

def llenar_campos():
        limpiar()
        limpiar()
        i = lb.curselection()[0]
        valor = lb.get(i)
        nombs, apells = _arrendatarios[valor]
        cursor.execute("SELECT * FROM arrendatarios WHERE a_nombres = %s AND a_apellidos = %s", (nombs, apells))
        #edit = """SELECT * FROM arrendatarios WHERE a_nombres=("%s");""" % (valor)
        #cursor.execute(edit)
        result = cursor.fetchall()
        connect.commit()
        for item in result:
                d1 = item[1] #Cedula
                d2 = item[2] #Titulo
                d3 = item[3] #Ciudad residencia
                d4 = item[4] #Nombres
                d5 = item[5] #Apellidos
                d6 = item[6] #Casa
                d7 = item[7] #Teléfono
                d8 = item[8] #Dir Envío
                d9 = item[9] #Email
                d10 = item[10] #Celular
                d11 = item[11] #Dia
                d12 = item[12] #Mes
                #d13 = item[13] #Cumple
                d14 = item[15] #Profesion
                d15 = item[14] #Empresa
                d16 = item[16] #Oficina
                d17 = item[17] #Tel
                d18 = item[18] #Fax
                d19 = item[19] #Banco
                d20 = item[20] #Tipo cuenta
                d21 = item[21] #Num Cuenta
                d22 = item[22] #Tipo persona
                d23 = item[23] #Retefuente
                d24 = item[24] #ReteIVa
                d25 = item[25] #Gran contribuyente
                d26 = item[26] #Genera factura
                d27 = item[27] #Genera cheque
                d28 = item[28] #Notas
                
                d29 = item[29] #Codeudo 1 CC
                d30 = item[30] #Codeudo 1 Nombre
                d31 = item[31] #Codeudo 1 Direccion
                d32 = item[32] #Codeudo 1 Telefono
                d33 = item[33] #Codeudo 1 Cargo
                d34 = item[34] #Codeudo 1 Empresa
                d35 = item[35] #Codeudo 1 Oficina
                d36 = item[36] #Codeudo 1 Telefono Oficina
                
                d37 = item[37]
                d38 = item[38]
                d39 = item[39]
                d40 = item[40]
                d41 = item[41]
                d42 = item[42]
                d43 = item[43]
                d44 = item[44]
                
                d45 = item[45] 
                d46 = item[46] 
                d47 = item[47] 
                d48 = item[48] 
                d49 = item[49] 
                d50 = item[50] 
                d51 = item[51] 
                d52 = item[52] 
                
                #VARIABLES TOMAN VALOR DE LOS ITEMS DEL FOR
                cedula.set(d1)
                titulo.set(d2)
                residencia.set(d3)
                nombres.set(d4)
                apellidos.set(d5)
                direccion.set(d6)
                telefono.set(d7)
                envio.set(d8)
                correo.set(d9)
                celular.set(d10)
                dia.set(d11)
                if d12 == '1':
                        d12 = 'Enero'
                if d12 == '2':
                        d12 = 'Febrero'
                if d12 == '3':
                        d12 = 'Marzo'
                if d12 == '4':
                        d12 = 'Abril'
                if d12 == '5':
                        d12 = 'Mayo'
                if d12 == '6':
                        d12 = 'Junio'
                if d12 == '7':
                        d12 = 'Julio'
                if d12 == '8':
                        d12 = 'Agosto'
                if d12 == '9':
                        d12 = 'Septiembre'
                if d12 == '10':
                        d12 = 'Octubre'
                if d12 == '11':
                        d12 = 'Noviembre'
                if d12 == '12':
                        d12 = 'Diciembre'
                mes.set(d12)
                #cumple.set(d13)
                profesion.set(d15)
                empresa.set(d14)
                oficina.set(d16)
                tel.set(d17)
                telfax.set(d18)
                banco.set(d19)
                tcuenta.set(d20)
                numcuenta.set(d21)
                tipopersona.set(d22)
                retefuente.set(d23)
                reteiva.set(d24)
                gcontribuyente.set(d25)
                gfactura.set(d26)
                gcheque.set(d27)
                note.insert('1.0',d28)
        
                co1cc.set(d29)
                co1nombres.set(d30)
                co1dir.set(d31)
                co1tel1.set(d32)
                co1cargo.set(d33)
                co1empresa.set(d34)
                co1oficina.set(d35)
                
                co2cc.set(d37)
                co2nombres.set(d38)
                co2dir.set(d39)
                co2tel1.set(d40)
                co2cargo.set(d41)
                co2empresa.set(d42)
                co2oficina.set(d43)
                co2tel2.set(d44)
                
                co3cc.set(d45)
                co3nombres.set(d46)
                co3dir.set(d47)
                co3tel1.set(d48)
                co3cargo.set(d49)
                co3empresa.set(d50)
                co3oficina.set(d51)
                co3tel2.set(d52)
                
                bloquear()
                
def habilitar():
        codeE.configure(state="normal")
        refE.configure(state="normal")
        cityE.configure(state="normal")
        nameE.configure(state="normal")
        lastnameE.configure(state="normal")
        adressE.configure(state="normal")
        phoneE.configure(state="normal")
        mailE.configure(state="normal")
        emailE.configure(state="normal")
        mobileE.configure(state="normal")
        birthdayE.configure(state="normal")
        birthdayCbx.configure(state="normal")
        ocupationE.configure(state="normal")
        companyE.configure(state="normal")
        ofiE.configure(state="normal")
        officetelE.configure(state="normal")
        faxE.configure(state="normal")
        bankCbx.configure(state="normal")
        banktypeCbx.configure(state="normal")
        numbankE.configure(state="normal")
        personR1.configure(state="normal")
        personR2.configure(state="normal")
        Ch1.configure(state="normal")
        Ch2.configure(state="normal")
        Ch3.configure(state="normal")
        Ch4.configure(state="normal")
        Ch5.configure(state="normal")
        note.configure(state="normal")
        
        cc1E.configure(state="normal")
        nameE.configure(state="normal")
        adress1E.configure(state="normal")
        phone1E.configure(state="normal")
        job1E.configure(state="normal")
        jobphone1E.configure(state="normal")
        office1E.configure(state="normal")
        officetel1E.configure(state="normal")
        
        cc2E.configure(state="normal")
        nameE.configure(state="normal")
        adress2E.configure(state="normal")
        phoneE.configure(state="normal")
        job2E.configure(state="normal")
        jobphone2E.configure(state="normal")
        office2E.configure(state="normal")
        officetel2E.configure(state="normal")
        
        cc3E.configure(state="normal")
        nameE.configure(state="normal")
        adress3E.configure(state="normal")
        phoneE.configure(state="normal")
        job3E.configure(state="normal")
        jobphone3E.configure(state="normal")
        office3E.configure(state="normal")
        officetel3E.configure(state="normal")
        
def modificar():
        try:
                llenar_campos()
                habilitar()
                codeE.configure(state="disabled")
                add.configure(state="disabled")
                update.configure(state="normal")
                clean.config(text='Cancelar')
                
        except IndexError, e:
                showerror("Error", e)

def actualizar():
        d1 = cedula.get()
        d2 = titulo.get()
        d3 = residencia.get()
        d4 = nombres.get()
        d5 = apellidos.get()
        d6 = direccion.get()
        d7 = telefono.get()
        d8 = envio.get()
        d9 = correo.get()
        d10 = celular.get()
        d11 = dia.get()
        d12 = mes.get()
        anio = 0
        y = anio
        if d12 == 'Enero':
                d12 = 1
        if d12 == 'Febrero':
                d12 = 2
        if d12 == 'Marzo':
                d12 = 3
        if d12 == 'Abril':
                d12 = 4
        if d12 == 'Mayo':
                d12 = 5
        if d12 == 'Junio':
                d12 = 6
        if d12 == 'Julio':
                d12 = 7
        if d12 == 'Agosto':
                d12 = 8
        if d12 == 'Septiembre':
                d12 = 9
        if d12 == 'Octubre':
                d12 = 10
        if d12 == 'Noviembre':
                d12 = 11
        if d12 == 'Diciembre':
                d12 = 12
        cumple = "%d-%d-%s" %(y,d12,d11)
        d13 = profesion.get()
        d14 = empresa.get()
        d15 = oficina.get()
        d16 = tel.get()
        d17 = telfax.get()
        d18 = banco.get()
        d19 = tcuenta.get()
        d20 = numcuenta.get()
        d21 = tipopersona.get()
        d22 = retefuente.get()
        d23 = reteiva.get()
        d24 = gcontribuyente.get()
        d25 = gfactura.get()
        d26 = gcheque.get()
        d27 = note.get("1.0",END)
        
        d28 = co1cc.get()
        d29 = co1nombres.get()
        d30 = co1dir.get()
        d31 = co1tel1.get()
        d32 = co1cargo.get()
        d33 = co1empresa.get()
        d34 = co1oficina.get()
        d35 = co1tel2.get()
        
        d36 = co2cc.get()
        d37 = co2nombres.get()
        d38 = co2dir.get()
        d39 = co2tel1.get()
        d40 = co2cargo.get()
        d41 = co2empresa.get()
        d42 = co2oficina.get()
        d43 = co2tel2.get()
        
        d44 = co3cc.get()
        d45 = co3nombres.get()
        d46 = co3dir.get()
        d47 = co3tel1.get()
        d48 = co3cargo.get()
        d49 = co3empresa.get()
        d50 = co3oficina.get()
        d51 = co3tel2.get()
        
        connect.commit()
        sql = "UPDATE arrendatarios SET a_titulo='%s', a_reside='%s', a_nombres='%s', a_apellidos='%s', a_direccion='%s', a_telefono='%s', a_envio='%s', a_email='%s', a_celular='%s', a_dia='%d', a_mes='%s', a_cumple='%s', a_profesion='%s', a_empresa='%s', a_oficina='%s', a_tel='%s', a_fax='%s', a_banco='%s', a_tcuenta='%s', a_numcuenta='%s', a_tpersona='%d', a_retefuente='%d', a_reteiva='%d', a_contribuyente='%d', a_gfactura='%d', a_gcheque='%d', a_nota='%s', co1_cc='%s', co1_nombres='%s', co1_dir='%s', co1_tel1='%s', co1_cargo='%s', co1_empresa='%s', co1_oficina='%s', co1_tel2='%s', co2_cc='%s', co2_nombres='%s', co2_dir='%s', co2_tel1='%s', co2_cargo='%s', co2_empresa='%s', co2_oficina='%s', co2_tel2='%s', co3_cc='%s', co3_nombres='%s', co3_dir='%s', co3_tel1='%s', co3_cargo='%s', co3_empresa='%s', co3_oficina='%s', co3_tel2='%s' WHERE a_cc='%s';" % (d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, cumple, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27, d28, d29, d30, d31, d32, d33, d34, d35, d36, d37, d38, d39, d40, d41, d42, d43, d44, d45, d46, d47, d48, d49, d50, d51, d1)
        cursor.execute(sql)
        showinfo ("Mensaje", "Datos actualizados!")
        
        cargar_lista()
        limpiar()
        #habilitar()
        
        codeE.configure(state="normal")
        add.configure(state="normal")
        update.configure(state="disabled")

def buscar():
        r = info.get()
        if r == 1:
                dato = busqueda.get()
                connect.commit()
                display = """SELECT a_nombres FROM arrendatarios WHERE a_cc LIKE '%s';""" % (dato + "%")
                cursor.execute(display)
                registros = cursor.fetchall()
                lb.delete(0, END)
                for item in registros:
                        lb.insert(END, item)
        else:
                dato = busqueda.get()
                connect.commit()
                display = """SELECT a_nombres FROM arrendatarios WHERE a_apellidos LIKE '%s';""" % (dato + "%")
                cursor.execute(display)
                registros = cursor.fetchall()
                lb.delete(0, END)
                for item in registros:
                        lb.insert(END, item)
        
# CONVIERTE LA ENTRADA DE LOS ENTRIES EN MAYÚSCULA
def caps(event):
        titulo.set(titulo.get().upper())
        residencia.set(residencia.get().upper())
        nombres.set(nombres.get().upper())
        apellidos.set(apellidos.get().upper())
        direccion.set(direccion.get().upper())
        envio.set(envio.get().upper())
        profesion.set(profesion.get().upper())
        empresa.set(empresa.get().upper())
        oficina.set(oficina.get().upper())
        #note.insert('1.0',note.get("1.0",END).upper())
        
        co1nombres.set(co1nombres.get().upper())
        co1dir.set(co1dir.get().upper())
        co1cargo.set(co1cargo.get().upper())
        co1empresa.set(co1empresa.get().upper())
        co1oficina.set(co1oficina.get().upper())

        co2nombres.set(co2nombres.get().upper())
        co2dir.set(co2dir.get().upper())
        co2cargo.set(co2cargo.get().upper())
        co2empresa.set(co2empresa.get().upper())
        co2oficina.set(co2oficina.get().upper())

        co3nombres.set(co3nombres.get().upper())
        co3dir.set(co3dir.get().upper())
        co3cargo.set(co3cargo.get().upper())
        co3empresa.set(co3empresa.get().upper())
        co3oficina.set(co3oficina.get().upper())
        
        busqueda.set(busqueda.get().upper())
