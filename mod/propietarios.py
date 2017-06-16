#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from ttk import Combobox, Notebook
from tkMessageBox import*
import MySQLdb
from controller import *

class Propietarios(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		#VARIABLES GLOBALES
		global cedula, titulo, ingreso, rsocial, residencia, nombres, apellidos, direccion, telefono, oficina, tel, telfax, correo, cumpleanos, dia, mes, envio, celular, tipopersona, comision, retefuente, reteiva, gcontribuyente, gfactura, gcheque, reprecc, reprenombres, repredireccion, repretelefono, repreoficina, repretel, reprebanco, repretcuenta, reprenumcuenta, tit1cc, tit1nombres, tit1banco, tit1tcuenta, tit1numcuenta, tit2cc, tit2nombres, tit2banco, tit2tcuenta, tit2numcuenta, lb, note, popmenu, busqueda, dato, E
		#INSTANCIEAS DE LOS WIDGETS
		global ccE, refE, dateinE, socialE, cityE, nameE, lnameE, adressE, phoneE, officeE, officetelE, telfaxE, emailE, birthdayE, birthdayCbx, mailE, mobileE, personR1, personR2, comisionE, Ch1, Ch2, Ch3, Ch4, Ch5, note, cc0E, name0E, adress0E, phone0E, office0E, officetel0E, bank0Cbx, tbank0Cbx, tcuenta0E, cc1E, name1E, bank1Cbx, tbank1Cbx, tcuenta1E, cc2E, name2E, bank2Cbx, tbank2Cbx, tcuenta2E, add, update, delete, clean
		global info, lists, _propietarios
		
		_propietarios = dict()
		lists = []
			
		#Variables
		cedula = StringVar()
		titulo = StringVar()
		ingreso = StringVar()
		rsocial = StringVar()
		residencia = StringVar()
		nombres = StringVar()
		apellidos = StringVar()
		direccion = StringVar()
		telefono = StringVar()
		oficina = StringVar()
		tel = StringVar()
		telfax = StringVar()
		correo = StringVar()
		dia = IntVar()
		mes = StringVar()
		envio = StringVar()
		celular = StringVar()
		tipopersona = IntVar()
		comision = DoubleVar()
		retefuente = IntVar()
		reteiva = IntVar()
		gcontribuyente = IntVar()
		gfactura = IntVar()
		gcheque = IntVar()
		notas = StringVar()
		
		#----------------------------
		
		reprecc = StringVar()
		reprenombres = StringVar()
		repredireccion = StringVar()
		repretelefono = StringVar()
		repreoficina = StringVar()
		repretel = StringVar()
		reprebanco = StringVar()
		repretcuenta = StringVar()
		reprenumcuenta = StringVar()
		
		tit1cc = StringVar()
		tit1nombres = StringVar()
		tit1banco = StringVar()
		tit1tcuenta = StringVar()
		tit1numcuenta = StringVar()
		
		tit2cc = StringVar()
		tit2nombres = StringVar()
		tit2banco = StringVar()
		tit2tcuenta = StringVar()
		tit2numcuenta = StringVar()
		
		meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto","Septiembre", "Octubre", "Noviembre", "Diciembre"]
		tbancos = ['Bancolombia', "Banco Bogotá", "Banco Agrario", "Banco Occidente"]

		tbanktype = ['Corriente','Ahorro']
		
		#BUSQUEDA = ["Nombre","CC/Nit"]
		busqueda = StringVar()
		busqueda.trace("w", lambda name, index, mode: buscar())
		info = IntVar()
		#eleccion = IntVar()
		dato = StringVar()
		
		# MENU DEL MOUSE
		
		popmenu = Menu(self, tearoff=0)
		popmenu.add_command(label="Imprimir", command=hello)
		popmenu.add_command(label="Cargar", command=modificar)
		popmenu.add_command(label="Eliminar", command=borrar)
		#popmenu.add_separator()
		popmenu.bind('<Escape>', release)

		#WIDGETS
		
		#========================= HEADER ==============================
		
		self.header = Label(self, text="GESTIÓN DE PROPIETARIOS", font="bold")
		self.header.pack(pady=20, side=TOP)

		#========================== WRAPPER ============================
		#Contiene los Notebooks con los campos formulario

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
		
		#========================= PERSONALES ==========================
		
		self.f1 = Frame(self.tab1)#-------------------------------
		self.f1.pack(pady=5,fill=X)
		
		self.ccL = Label(self.f1, text='CC/Nit:')
		self.ccL.pack(side=LEFT)
		ccE = Entry(self.f1, textvariable=cedula)
		ccE.pack(side=LEFT, fill=X, expand=1)
		ccE.focus_set()

		self.refL = Label(self.f1, text='Título:')
		self.refL.pack(side=LEFT)
		refE = Entry(self.f1, textvariable=titulo, width=10)
		refE.pack(side=LEFT)
		#refE.bind("<KeyRelease>", caps)

		self.dateinL = Label(self.f1, text='Fecha Ingreso:')
		self.dateinL.pack(side=LEFT)
		dateinE = Entry(self.f1, textvariable=ingreso, width=10, state=DISABLED)
		ingreso.set("0000-00-00")
		dateinE.pack(side=LEFT)

		self.f2 = Frame(self.tab1)#-------------------------------
		self.f2.pack(pady=5,fill=X)

		self.socialL = Label(self.f2, text='Razón Social:')
		self.socialL.pack(side=LEFT)
		socialE = Entry(self.f2, textvariable=rsocial)
		socialE.pack(side=LEFT, fill=X, expand=1)
		socialE.bind("<KeyRelease>", caps)

		self.cityL = Label(self.f2, text='Ciudad de residencia:')
		self.cityL.pack(side=LEFT)
		cityE = Entry(self.f2, textvariable=residencia, width=15)
		cityE.pack(side=LEFT)
		cityE.bind("<KeyRelease>", caps)

		self.f3 = Frame(self.tab1)
		self.f3.pack(pady=5,fill=X)#-----------------------------------------

		self.nameL = Label(self.f3, text='Nombres:')
		self.nameL.pack(side=LEFT)
		nameE = Entry(self.f3, textvariable=nombres)
		nameE.pack(side=LEFT, fill=X, expand=1)
		nameE.bind("<KeyRelease>", caps)

		self.lnameL = Label(self.f3, text='Apellidos:')
		self.lnameL.pack(side=LEFT)
		lnameE = Entry(self.f3, textvariable=apellidos)
		lnameE.pack(side=LEFT, fill=X, expand=1)
		lnameE.bind("<KeyRelease>", caps)

		self.f4 = Frame(self.tab1)
		self.f4.pack(pady=5,fill=X)#-----------------------------------------

		self.adressL = Label(self.f4, text='Dir. Casa:')
		self.adressL.pack(side=LEFT)
		adressE = Entry(self.f4, textvariable=direccion)
		adressE.pack(side=LEFT, fill=X, expand=1)
		adressE.bind("<KeyRelease>", caps)

		self.phoneL = Label(self.f4, text='Tel:')
		self.phoneL.pack(side=LEFT)
		phoneE = Entry(self.f4, textvariable=telefono, width=20)
		phoneE.pack(side=LEFT)

		self.f5 = Frame(self.tab1)
		self.f5.pack(pady=5,fill=X)#------------------------------------
		
		self.officeL = Label(self.f5, text='Dir. Oficina:')
		self.officeL.pack(side=LEFT)
		officeE = Entry(self.f5, textvariable=oficina, width=20)
		officeE.pack(side=LEFT, fill=X, expand=1)
		officeE.bind("<KeyRelease>", caps)

		self.officetelL = Label(self.f5, text='Tel:')
		self.officetelL.pack(side=LEFT)
		officetelE = Entry(self.f5, textvariable=tel, width=15)
		officetelE.pack(fill=X, side=LEFT)

		self.telfaxL = Label(self.f5, text='Tel. Fax:')
		self.telfaxL.pack(side=LEFT)
		telfaxE = Entry(self.f5, textvariable=telfax, width=10)
		telfaxE.pack(side=LEFT)

		self.f6 = Frame(self.tab1)
		self.f6.pack(pady=5,fill=X)#------------------------------------

		self.emailL = Label(self.f6, text='Email:')
		self.emailL.pack(side=LEFT)
		emailE = Entry(self.f6, textvariable=correo, width=30)
		emailE.pack(side=LEFT)

		self.birthdayL = Label(self.f6, text='Cumpleaños:')
		self.birthdayL.pack(side=LEFT)

		self.birthdayL2 = Label(self.f6, text='Día:')
		self.birthdayL2.pack(padx=5,side=LEFT)
		
		#s = Spinbox(self.f6, from_=1, to=31,textvariable=dia, width=3)
		#s.pack(side=LEFT)

		birthdayE = Entry(self.f6, textvariable=dia, width=3)
		birthdayE.pack(side=LEFT)

		self.birthdayL3 = Label(self.f6, text='Mes:')
		self.birthdayL3.pack(padx=5,side=LEFT)

		birthdayCbx = Combobox(self.f6, textvariable=mes, values=meses, width=10)
		birthdayCbx.set('Enero')
		birthdayCbx.pack(side=LEFT)
		
		self.f7 = Frame(self.tab1)
		self.f7.pack(pady=5,fill=X)#------------------------------------

		self.mailL = Label(self.f7, text='Dir. Correspondencia:')
		self.mailL.pack(side=LEFT)
		mailE = Entry(self.f7, textvariable=envio)
		mailE.pack(side=LEFT, fill=X, expand=1)
		mailE.bind("<KeyRelease>", caps)

		self.mobileL = Label(self.f7, text='Celular:')
		self.mobileL.pack(side=LEFT)
		mobileE = Entry(self.f7, textvariable=celular, width=10)
		mobileE.pack(side=LEFT, fill=X, expand=1)
		
		self.f8 = Frame(self.tab1)
		self.f8.pack(pady=5,fill=X)#------------------------------------

		self.personL = Label(self.f8, text='Tipo Persona:')
		self.personL.pack(side=LEFT)
		
		personR1 = Radiobutton(self.f8, text="Natural", variable=tipopersona, value=1)
		personR1.pack(padx=20,side=LEFT)
		
		personR2 = Radiobutton (self.f8, text="Jurídica", variable=tipopersona, value=2)
		personR2.pack(padx=20,side=LEFT)

		self.comisionL = Label(self.f8, text='$ Comisión:')
		self.comisionL.pack(side=LEFT)
		
		comisionE = Entry(self.f8, textvariable=comision, width=5)
		comisionE.pack(side=LEFT)
		
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
		self.f9.pack(pady=5,fill=X)#------------------------------------

		self.notesL = Label(self.f9, text='Observaciones:')
		self.notesL.pack(side=LEFT)

		self.f10 = Frame(self.tab1)
		self.f10.pack(pady=5,fill=X)#------------------------------------

		note = Text(self.f10, height=5)
		note.pack(side=LEFT, fill=X, expand=1)
		
		self.tab1.pack()
		
		#-----------------------> TAB 2
		
		self.tab2 = Frame (self.nb)
		self.tab2.pack()
		
		self.f0 = Frame(self.tab2)#Para dejar espacio entre Tab y Label
		self.f0.pack(fill=X, pady=10)#----------------------------------
		
		#======================= COMPLEMENTARIOS =======================
		
		self.lf = LabelFrame(self.tab2, text="Datos Representante")
		
		self.f0 = Frame(self.lf)
		self.f0.pack(fill=X, pady=5)#-------------------------------
		
		self.ccRL = Label(self.f0, text='CC:')
		self.ccRL.pack(side=LEFT)
		cc0E = Entry(self.f0, textvariable=reprecc, width=10)
		cc0E.pack(side=LEFT, fill=X, expand=1)
		
		self.nameL = Label(self.f0, text='Nombres:')
		self.nameL.pack(side=LEFT)
		name0E = Entry(self.f0, textvariable=reprenombres)
		name0E.pack(side=LEFT, fill=X, expand=1)
		name0E.bind("<KeyRelease>", caps)
		
		self.f1 = Frame(self.lf)
		self.f1.pack(fill=X, pady=5)#-------------------------------
		
		self.adressL = Label(self.f1, text='Dir. Casa:')
		self.adressL.pack(side=LEFT)
		adress0E = Entry(self.f1, textvariable=repredireccion)
		adress0E.pack(side=LEFT, fill=X, expand=1)
		adress0E.bind("<KeyRelease>", caps)

		self.phoneL = Label(self.f1, text='Tel:')
		self.phoneL.pack(side=LEFT)
		phone0E = Entry(self.f1, textvariable=repretelefono, width=20)
		phone0E.pack(side=LEFT)
		
		self.f2 = Frame(self.lf)
		self.f2.pack(fill=X, pady=5)#-------------------------------
		
		self.officeL = Label(self.f2, text='Dir. Oficina:')
		self.officeL.pack(side=LEFT)
		office0E = Entry(self.f2, textvariable=repreoficina)
		office0E.pack(side=LEFT, fill=X, expand=1)
		office0E.bind("<KeyRelease>", caps)

		self.officetelL = Label(self.f2, text='Tel:')
		self.officetelL.pack(side=LEFT)
		officetel0E = Entry(self.f2, textvariable=repretel, width=20)
		officetel0E.pack(fill=X, side=LEFT)
		
		self.f3 = Frame (self.lf)
		self.f3.pack(fill=X)#-------------------------------------------
		
		self.tbancpL = Label(self.f3, text='Banco:')
		self.tbancpL.pack(side=LEFT)
		bank0Cbx = Combobox(self.f3, textvariable=reprebanco, values=tbancos, width=12)
		bank0Cbx.set('')
		bank0Cbx.pack(side=LEFT)

		self.tbancpL = Label(self.f3, text='Tipo Cuenta:')
		self.tbancpL.pack(side=LEFT)
		tbank0Cbx = Combobox(self.f3, textvariable=repretcuenta, values=tbanktype, width=8)
		tbank0Cbx.set('')
		tbank0Cbx.pack(side=LEFT)

		self.tcuentaL = Label(self.f3, text='# Cuenta:')
		self.tcuentaL.pack(side=LEFT)
		tcuenta0E = Entry(self.f3, textvariable=reprenumcuenta)
		tcuenta0E.pack(side=LEFT, fill=X, expand=1)
		
		self.lf.pack(fill=X, ipady=5)#==================================
		
		self.f0 = Frame(self.tab2)#Para dejar espacio entre Tab y Label
		self.f0.pack(fill=X, pady=10)#-------------------------------
		
		#---------------------------------------------------------------
		
		self.lf1 = LabelFrame(self.tab2, text="Datos Titular 1")
		
		self.f4 = Frame(self.lf1)
		self.f4.pack(fill=X, pady=5)#-------------------------------
		
		self.ccL = Label(self.f4, text='CC:')
		self.ccL.pack(side=LEFT)
		cc1E = Entry(self.f4, textvariable=tit1cc)
		cc1E.pack(side=LEFT, fill=X, expand=1)
		
		self.nameL = Label(self.f4, text='Nombres:')
		self.nameL.pack(side=LEFT)
		name1E = Entry(self.f4, textvariable=tit1nombres)
		name1E.pack(side=LEFT, fill=X, expand=1)
		name1E.bind("<KeyRelease>", caps)
		
		self.f5 = Frame (self.lf1)
		self.f5.pack(fill=X)#-------------------------------------------
		
		self.tbancpL = Label(self.f5, text='Banco:')
		self.tbancpL.pack(side=LEFT)
		bank1Cbx = Combobox(self.f5, textvariable=tit1banco, values=tbancos, width=12)
		bank1Cbx.set('')
		bank1Cbx.pack(side=LEFT)

		self.tbancpL = Label(self.f5, text='Tipo Cuenta:')
		self.tbancpL.pack(side=LEFT)
		tbank1Cbx = Combobox(self.f5, textvariable=tit1tcuenta, values=tbanktype, width=8)
		tbank1Cbx.set('')
		tbank1Cbx.pack(side=LEFT)

		self.tcuentaL = Label(self.f5, text='# Cuenta:')
		self.tcuentaL.pack(side=LEFT)
		tcuenta1E = Entry(self.f5, textvariable=tit1numcuenta)
		tcuenta1E.pack(side=LEFT, fill=X, expand=1)
		
		self.lf1.pack(fill=X, ipady=5)#================================
		
		self.f0 = Frame(self.tab2)#Para dejar espacio entre Tab y Label
		self.f0.pack(fill=X, pady=10)#-------------------------------
		
		#---------------------------------------------------------------
		
		self.lf2 = LabelFrame(self.tab2, text="Datos Titular 2")
		
		self.f5 = Frame(self.lf2)
		self.f5.pack(fill=X, pady=5)#-------------------------------
		
		self.ccL = Label(self.f5, text='CC:')
		self.ccL.pack(side=LEFT)
		cc2E = Entry(self.f5, textvariable=tit2cc)
		cc2E.pack(side=LEFT, fill=X, expand=1)
		
		self.nameL = Label(self.f5, text='Nombres:')
		self.nameL.pack(side=LEFT)
		name2E = Entry(self.f5, textvariable=tit2nombres)
		name2E.pack(side=LEFT, fill=X, expand=1)
		name2E.bind("<KeyRelease>", caps)
		
		self.f6 = Frame (self.lf2)
		self.f6.pack(fill=X)#-------------------------------------------
		
		self.tbancpL = Label(self.f6, text='Banco:')
		self.tbancpL.pack(side=LEFT)
		bank2Cbx = Combobox(self.f6, textvariable=tit2banco, values=tbancos, width=12)
		bank2Cbx.set('')
		bank2Cbx.pack(side=LEFT)

		self.tbancpL = Label(self.f6, text='Tipo Cuenta:')
		self.tbancpL.pack(side=LEFT)
		tbank2Cbx = Combobox(self.f6, textvariable=tit2tcuenta, values=tbanktype, width=8)
		tbank2Cbx.set('')
		tbank2Cbx.pack(side=LEFT)

		self.tcuentaL = Label(self.f6, text='# Cuenta:')
		self.tcuentaL.pack(side=LEFT)
		tcuenta2E = Entry(self.f6, textvariable=tit2numcuenta)
		tcuenta2E.pack(side=LEFT, fill=X, expand=1)
		
		self.lf2.pack(fill=X, ipady=5)#================================
		
		#---------------------------------------------------------------
		
		self.nb.add (self.tab1, text="Personales")
		self.nb.add(self.tab2, text="Complementarios")
		
		self.nb.pack()
		
		#=========================== BOTONES ===========================

		self.btns = Frame(self.wrapper)
		self.btns.pack()#-------------------------------
	
		clean = Button(self.btns, text='Limpiar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=limpiar)
		clean.pack(side=RIGHT)

		update = Button(self.btns, text='Actualizar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=actualizar, state=DISABLED)
		update.pack(side=RIGHT)
		
		add = Button(self.btns, text='Agregar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=Agregar)
		add.pack(side=RIGHT)
		
		#========================= ASIDE ===========================
		
		self.aside = Frame(self)
		self.aside.pack(side=LEFT, fill=BOTH, expand=True)
		
		self.wrap1 = Frame(self.aside)
		self.wrap1.pack()
		
		self.viewer = Label(self.wrap1, text="LISTA DE PROPIETARIOS")
		self.viewer.pack()

		scroll = Scrollbar(self.wrap1, orient=VERTICAL)
		scroll.pack(side=RIGHT, fill=Y)
		
		lb = Listbox(self.wrap1, yscrollcommand=scroll.set, height=20, width=30, bg='#d8ecf3')
		scroll.config (command=lb.yview)
		lb.pack(fill=BOTH)
		lb.bind("<Double-Button-1>", callback)
		lb.bind("<Button-3>", popup)
		#lb.bind('<Escape>', release)
		
		self.wrap2 = Frame(self.aside)
		self.wrap2.pack()
		
		self.updateBP = Button(self.wrap2, text='Cargar lista', width=20, bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=cargar_lista)
		self.updateBP.pack()
		
		delete = Button(self.wrap2, text='Borrar', bg='navy', width=20, foreground='white', activebackground='red3', activeforeground='white', command=borrar)
		delete.pack()
		
		edit = Button(self.wrap2, text='Modificar', bg='navy', width=20, foreground='white', activebackground='red3', activeforeground='white', command=modificar)
		edit.pack()
		
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

def cargar_lista():
	try:
		connect.commit()
		cursor.execute("SELECT p_nombres, p_apellidos FROM propietarios order by p_nombres")
		registros = cursor.fetchall()
		lb.delete(0, END)
		for item in registros:
			nombres = item[0]
			apellidos = item[1]
			nombre_completo = nombres + ' ' + apellidos
			_propietarios[nombre_completo] = [nombres, apellidos]
			lb.insert(END, nombre_completo)
	except:
		showerror ("Mensaje", "Error al cargar los propietarios.")
		
# NUEVO / CANCELAR
def limpiar():
	clean.config(text='Limpiar')
	#print note.get("1.0",END)
	cedula.set("")
	titulo.set("")
	ingreso.set("0000-00-00")
	rsocial.set("")
	residencia.set("")
	nombres.set("")
	apellidos.set("")
	direccion.set("")
	telefono.set("")
	oficina.set("")
	tel.set("")
	telfax.set("")
	correo.set("")
	mes.set('Enero')
	dia.set(0)
	envio.set("")
	celular.set("")
	tipopersona.set(0)
	comision.set(0.0)
	retefuente.set(0)
	reteiva.set(0)
	gcontribuyente.set(0)
	gfactura.set(0)
	gcheque.set(0)
	#note.delete('1.0', '2.0')
	note.delete('1.0', END)
	
	reprecc.set("")
	reprenombres.set("")
	repredireccion.set("")
	repretelefono.set("")
	repreoficina.set("")
	repretel.set("")
	reprebanco.set("")
	repretcuenta.set("")
	reprenumcuenta.set("")
	
	tit1cc.set("")
	tit1nombres.set("")
	tit1banco.set("")
	tit1tcuenta.set("")
	tit1numcuenta.set("")
	
	tit2cc.set("")
	tit2nombres.set("")
	tit2banco.set("")
	tit2tcuenta.set("")
	tit2numcuenta.set("")
	
	habilitar()
	note.delete('1.0', END)
	
	ccE.configure(state="normal")
	add.configure(state="normal")
	update.configure(state="disabled")
	dateinE.configure(state="disabled")

def Agregar():
	try:
		cc = cedula.get()
		ref = titulo.get()
		fi = ingreso.get()
		rs = rsocial.get()
		loc1 = residencia.get()
		n = nombres.get()
		a = apellidos.get()
		loc2 = direccion.get()
		tel1 = telefono.get()
		of = oficina.get()
		tel2 = tel.get()
		fax = telfax.get()
		email = correo.get()
		anio = 0
		y = anio
		m = mes.get()
		if m == 'Enero':
			m = 1
		if m == 'Febrero':
			m = 2
		if m == 'Marzo':
			m = 3
		if m == 'Abril':
			m = 4
		if m == 'Mayo':
			m = 5
		if m == 'Junio':
			m = 6
		if m == 'Julio':
			m = 7
		if m == 'Agosto':
			m = 8
		if m == 'Septiembre':
			m = 9
		if m == 'Octubre':
			m = 10
		if m == 'Noviembre':
			m = 11
		if m == 'Diciembre':
			m = 12
		d = dia.get()
		cumple = "%d-%d-%s" %(y,m,d)
		e = envio.get()
		cel = celular.get()
		tp = tipopersona.get()
		c = comision.get()
		rf = retefuente.get()
		ri = reteiva.get()
		gc = gcontribuyente.get()
		gf = gfactura.get()
		gch =gcheque.get()
		o = note.get("1.0",END)
		
		rcc = reprecc.get()
		rn = reprenombres.get()
		rd = repredireccion.get()
		rt1 = repretelefono.get()
		ro = repreoficina.get()
		rt2 = repretel.get()
		rb = reprebanco.get()
		rtc = repretcuenta.get()
		rnc = reprenumcuenta.get()
		
		t1cc = tit1cc.get()
		t1n = tit1nombres.get()
		t1b = tit1banco.get()
		t1tc = tit1tcuenta.get()
		t1nc = tit1numcuenta.get()
		
		t2cc = tit1cc.get()
		t2n = tit1nombres.get()
		t2b = tit1banco.get()
		t2tc = tit1tcuenta.get()
		t2nc = tit1numcuenta.get()
		
		connect.commit()
		sql = "INSERT INTO propietarios (p_cc, p_titulo, p_ingreso, p_rsocial, p_reside, p_nombres, p_apellidos, p_direccion, p_telefono, p_oficina, p_tel, p_fax, p_email, p_dia, p_mes, p_cumple, p_envio, p_celular, p_tpersona, p_comision, p_retefuente, p_reteiva, p_contribuyente, p_gfactura, p_gcheque, p_nota, cc_represent, nombres_represent, dir_represent, tel_represent, oficina_represent, telofi_represent, banco_represent, tcuenta_represent, numcuenta_represent, cc_titular1, nombres_titular1, banco_titular1, tcuenta_titular1, numcuenta_titular1, cc_titular2, nombres_titular2, banco_titular2, tcuenta_titular2, numcuenta_titular2) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%s', '%s', '%s', '%s', '%d', '%f', '%d', '%d', '%d', '%d', '%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (cc, ref, fi, rs, loc1, n, a, loc2, tel1, of, tel2, fax, email, d, m, cumple, e, cel, tp, c, rf, ri, gc, gf, gch, o, rcc, rn, rd, rt1, ro, rt2, rb, rtc, rnc, t1cc, t1n, t1b, t1tc, t1nc, t2cc, t2n, t2b, t2tc, t2nc)
		cursor.execute(sql)
		showinfo ("Mensaje", "Datos guardados")
		limpiar()
		cargar_lista()
		
	except MySQLdb.IntegrityError, e:
		showerror("Error",e)
		
def borrar():
	try:
		i = lb.curselection()
		value = lb.get(i[0])
		if askyesno("Salir", "¿Desea borrar este propietario?"):
			delete = """DELETE FROM propietarios WHERE p_nombres=("%s");""" % (value)
			cursor.execute(delete)
			connect.commit()
			lb.delete(i)
			showinfo("mensaje", "Dato Borrado!")
			lb.delete(0, END)
			cargar_lista()
			limpiar()
			
	except MySQLdb.IntegrityError, e:
		showerror("Error", e)
		#showerror ('Mensaje', "No se puede borrar o actualizar porque hace parte de una relación.")

def bloquear():
	ccE.configure(state="disabled")
	refE.configure(state="disabled")
	dateinE.configure(state="disabled")
	socialE.configure(state="disabled")
	cityE.configure(state="disabled")
	nameE.configure(state="disabled")
	lnameE.configure(state="disabled")
	adressE.configure(state="disabled")
	phoneE.configure(state="disabled")
	officeE.configure(state="disabled")
	officetelE.configure(state="disabled")
	telfaxE.configure(state="disabled")
	emailE.configure(state="disabled")
	birthdayE.configure(state="disabled")
	birthdayCbx.configure(state="disabled")
	mailE.configure(state="disabled")
	mobileE.configure(state="disabled")
	personR1.configure(state="disabled")
	personR2.configure(state="disabled")
	comisionE.configure(state="disabled")
	Ch1.configure(state="disabled")
	Ch2.configure(state="disabled")
	Ch3.configure(state="disabled")
	Ch4.configure(state="disabled")
	Ch5.configure(state="disabled")
	note.configure(state="disabled")
	
	cc0E.configure(state="disabled")
	name0E.configure(state="disabled")
	adress0E.configure(state="disabled")
	phone0E.configure(state="disabled")
	office0E.configure(state="disabled")
	officetel0E.configure(state="disabled")
	bank0Cbx.configure(state="disabled")
	tbank0Cbx.configure(state="disabled")
	tcuenta0E.configure(state="disabled")
	
	cc1E.configure(state="disabled")
	name1E.configure(state="disabled")
	bank1Cbx.configure(state="disabled")
	tbank1Cbx.configure(state="disabled")
	tcuenta1E.configure(state="disabled")
	
	cc2E.configure(state="disabled")
	name2E.configure(state="disabled")
	bank2Cbx.configure(state="disabled")
	tbank2Cbx.configure(state="disabled")
	tcuenta2E.configure(state="disabled")

# LLENAR CAMPOS CON DOBLE CLIC
def callback(event):
	#note.delete('1.0', END)
	llenar_campos()
	
def llenar_campos():
        limpiar()
        limpiar()
	i = lb.curselection()[0]
	valor = lb.get(i)
	nombs, apells = _propietarios[valor]
	cursor.execute("SELECT * FROM propietarios WHERE p_nombres = %s AND p_apellidos = %s", (nombs, apells))
	result = cursor.fetchall()
	connect.commit()
	for item in result:
		d1 = item[1] #CC/nit
		d2 = item[2] #título
		d3 = item[3] #Fingreso
		d4 = item[4] #razón social
		d5 = item[5] #Ciudad
		d6 = item[6] #Nombres
		d7 = item[7] #Apellidos
		d8 = item[8] #Dir casa
		d9 = item[9] #Teléfono
		d10 = item[10] #Dir oficina
		d11 = item[11] #Tel oficina
		d12 = item[12] #Fax
		d13 = item[13] #Email
		d14 = item[15] #Día
		d15 = item[14] #Mes
		#d16 = item[16] #Cumple
		d17 = item[17] #Correspondencia
		d18 = item[18] #Celular
		d19 = item[19] #Tipo persona
		d20 = item[20] #Comisión
		d21 = item[21] #Retefuente
		d22 = item[22] #ReteIVA
		d23 = item[23] #Contribuyente
		d24 = item[24] #Gen Factura
		d25 = item[25] #Gen Cheque
		d26 = item[26] #Observaciones
		
		d27 = item[27] #CC Repre
		d28 = item[28] #Nombre Repre
		d29 = item[29] #Dir casa Repre
		d30 = item[30] #Tel casa Repre
		d31 = item[31] #Dir oficina Repre
		d32 = item[32] #Tel ofi Repre
		d33 = item[33] #Banco Repre
		d34 = item[34] #Tipo cuenta Repre
		d35 = item[35] #Num cuenta Repre
		
		d36 = item[36]
		d37 = item[37]
		d38 = item[38]
		d39 = item[39]
		d40 = item[40]
		
		d41 = item[41]
		d42 = item[42]
		d43 = item[43]
		d44 = item[44]
		d45 = item[45]
		
		cedula.set(d1)
		titulo.set(d2)
		ingreso.set(d3)
		rsocial.set(d4)
		residencia.set(d5)
		nombres.set(d6)
		apellidos.set(d7)
		direccion.set(d8)
		telefono.set(d9)
		oficina.set(d10)
		tel.set(d11)
		telfax.set(d12)
		correo.set(d13)
		if d14 == '1':
			d14 = 'Enero'
		if d14 == '2':
			d14 = 'Febrero'
		if d14 == '3':
			d14 = 'Marzo'
		if d14 == '4':
			d14 = 'Abril'
		if d14 == '5':
			d14 = 'Mayo'
		if d14 == '6':
			d14 = 'Junio'
		if d14 == '7':
			d14 = 'Julio'
		if d14 == '8':
			d14 = 'Agosto'
		if d14 == '9':
			d14 = 'Septiembre'
		if d14 == '10':
			d14 = 'Octubre'
		if d14 == '11':
			d14 = 'Noviembre'
		if d14 == '12':
			d14 = 'Diciembre'
		mes.set(d14)
		dia.set(d15)
		#cumple.set(d15)
		envio.set(d17)
		celular.set(d18)
		tipopersona.set(d19)
		comision.set(d20)
		retefuente.set(d21)
		reteiva.set(d22)
		gcontribuyente.set(d23)
		gfactura.set(d24)
		gcheque.set(d25)
		note.insert('1.0',d26)
	
		reprecc.set(d27)
		reprenombres.set(d28)
		repredireccion.set(d29)
		repretelefono.set(d30)
		repreoficina.set(d31)
		repretel.set(d32)
		reprebanco.set(d33)
		repretcuenta.set(d34)
		reprenumcuenta.set(d35)
	
		tit1cc.set(d36)
		tit1nombres.set(d37)
		tit1banco.set(d38)
		tit1tcuenta.set(d39)
		tit1numcuenta.set(d40)
	
		tit2cc.set(d41)
		tit2nombres.set(d42)
		tit2banco.set(d43)
		tit2tcuenta.set(d44)
		tit2numcuenta.set(d45)
		
		bloquear()

def habilitar():
	ccE.configure(state="normal")
	refE.configure(state="normal")
	dateinE.configure(state="normal")
	socialE.configure(state="normal")
	cityE.configure(state="normal")
	nameE.configure(state="normal")
	lnameE.configure(state="normal")
	adressE.configure(state="normal")
	phoneE.configure(state="normal")
	officeE.configure(state="normal")
	officetelE.configure(state="normal")
	telfaxE.configure(state="normal")
	emailE.configure(state="normal")
	birthdayE.configure(state="normal")
	birthdayCbx.configure(state="normal")
	mailE.configure(state="normal")
	mobileE.configure(state="normal")
	personR1.configure(state="normal")
	personR2.configure(state="normal")
	comisionE.configure(state="normal")
	Ch1.configure(state="normal")
	Ch2.configure(state="normal")
	Ch3.configure(state="normal")
	Ch4.configure(state="normal")
	Ch5.configure(state="normal")
	note.configure(state="normal")
	
	cc0E.configure(state="normal")
	name0E.configure(state="normal")
	adress0E.configure(state="normal")
	phone0E.configure(state="normal")
	office0E.configure(state="normal")
	officetel0E.configure(state="normal")
	bank0Cbx.configure(state="normal")
	tbank0Cbx.configure(state="normal")
	tcuenta0E.configure(state="normal")
	
	cc1E.configure(state="normal")
	name1E.configure(state="normal")
	tbank1Cbx.configure(state="normal")
	tbank1Cbx.configure(state="normal")
	tcuenta1E.configure(state="normal")
	
	cc2E.configure(state="normal")
	name2E.configure(state="normal")
	tbank2Cbx.configure(state="normal")
	tbank2Cbx.configure(state="normal")
	tcuenta2E.configure(state="normal")
	
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
	cc = cedula.get()
	ref = titulo.get()
	fi = ingreso.get()
	rs = rsocial.get()
	loc1 = residencia.get()
	n = nombres.get()
	a = apellidos.get()
	loc2 = direccion.get()
	tel1 = telefono.get()
	of = oficina.get()
	tel2 = tel.get()
	fax = telfax.get()
	email = correo.get()
	anio = 0
	y = anio
	m = mes.get()
	if m == 'Enero':
		m = 1
	if m == 'Febrero':
		m = 2
	if m == 'Marzo':
		m = 3
	if m == 'Abril':
		m = 4
	if m == 'Mayo':
		m = 5
	if m == 'Junio':
		m = 6
	if m == 'Julio':
		m = 7
	if m == 'Agosto':
		m = 8
	if m == 'Septiembre':
		m = 9
	if m == 'Octubre':
		m = 10
	if m == 'Noviembre':
		m = 11
	if m == 'Diciembre':
		m = 12
	d = dia.get()
	cumple = "%d-%d-%s" %(y,m,d)
	e = envio.get()
	cel = celular.get()
	tp = tipopersona.get()
	c = comision.get()
	rf = retefuente.get()
	ri = reteiva.get()
	gc = gcontribuyente.get()
	gf = gfactura.get()
	gch =gcheque.get()
	o = note.get("1.0",END)
	
	rcc = reprecc.get()
	rn = reprenombres.get()
	rd = repredireccion.get()
	rt1 = repretelefono.get()
	ro = repreoficina.get()
	rt2 = repretel.get()
	rb = reprebanco.get()
	rtc = repretcuenta.get()
	rnc = reprenumcuenta.get()
	
	t1cc = tit1cc.get()
	t1n = tit1nombres.get()
	t1b = tit1banco.get()
	t1tc = tit1tcuenta.get()
	t1nc = tit1numcuenta.get()
	
	t2cc = tit1cc.get()
	t2n = tit1nombres.get()
	t2b = tit1banco.get()
	t2tc = tit1tcuenta.get()
	t2nc = tit1numcuenta.get()
	
	connect.commit()
	sql = "UPDATE propietarios SET p_titulo='%s', p_ingreso='%s', p_rsocial='%s', p_reside='%s', p_nombres='%s', p_apellidos='%s', p_direccion='%s', p_telefono='%s', p_oficina='%s', p_tel='%s', p_fax='%s', p_email='%s', p_dia='%d', p_mes='%s', p_cumple='%s', p_envio='%s', p_celular='%s', p_tpersona='%d', p_comision='%f', p_retefuente='%d', p_reteiva='%d', p_contribuyente='%d', p_gfactura='%d', p_gcheque='%d', p_nota='%s', cc_represent='%s', nombres_represent='%s', dir_represent='%s', tel_represent='%s', oficina_represent='%s', telofi_represent='%s', banco_represent='%s', tcuenta_represent='%s', numcuenta_represent='%s', cc_titular1='%s', nombres_titular1='%s', banco_titular1='%s', tcuenta_titular1='%s', numcuenta_titular1='%s', cc_titular2='%s', nombres_titular2='%s', banco_titular2='%s', tcuenta_titular2='%s', numcuenta_titular2='%s' WHERE p_cc='%s';" % (ref, fi, rs, loc1, n, a, loc2, tel1, of, tel2, fax, email, d, m, cumple, e, cel, tp, c, rf, ri, gc, gf, gch, o, rcc, rn, rd, rt1, ro, rt2, rb, rtc, rnc, t1cc, t1n, t1b, t1tc, t1nc, t2cc, t2n, t2b, t2tc, t2nc, cc)
	cursor.execute(sql)
	showinfo ("Mensaje", "Datos actualizados!")
	
	cargar_lista()
	limpiar()
	#habilitar()
	
	ccE.configure(state="normal")
	add.configure(state="normal")
	update.configure(state="disabled")
	
def buscar():
	r = info.get()
	if r == 1:
		dato = busqueda.get()
		connect.commit()
		display = """SELECT p_nombres FROM propietarios WHERE p_cc LIKE '%s';""" % (dato + "%")
		cursor.execute(display)
		registros = cursor.fetchall()
		lb.delete(0, END)
		for item in registros:
			lb.insert(END, item)
	else:
		dato = busqueda.get()
		connect.commit()
		display = """SELECT p_nombres FROM propietarios WHERE p_apellidos LIKE '%s';""" % (dato + "%")
		cursor.execute(display)
		registros = cursor.fetchall()
		lb.delete(0, END)
		for item in registros:
			lb.insert(END, item)
	"""
	for item in registros:
		if dato in item:
			#lb.insert(END, item)
			nombres = item[0]
			lb.insert(END, nombres)"""
	
def caps(event):
	titulo.set(titulo.get().upper())
	rsocial.set(rsocial.get().upper())
	residencia.set(residencia.get().upper())
	nombres.set(nombres.get().upper())
	apellidos.set(apellidos.get().upper())
	direccion.set(direccion.get().upper())

	oficina.set(oficina.get().upper())

	envio.set(envio.get().upper())
	
	reprenombres.set(reprenombres.get().upper())
	repredireccion.set(repredireccion.get().upper())
	repreoficina.set(repreoficina.get().upper())
	
	tit1nombres.set(tit1nombres.get().upper())
	
	tit2nombres.set(tit2nombres.get().upper())
	busqueda.set(busqueda.get().upper())

#DESPLIEGA UN MENU CONTEXTUAL
def popup(event):
	try:
		popmenu.post(event.x_root, event.y_root)
	finally:
		popmenu.grab_release()
	
def hello():
	print "Hola"

def release(event):
	#exit(0)#CIERRA TODO EL PROGRAMA
	popmenu.grab_release()
