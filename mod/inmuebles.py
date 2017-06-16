#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from ttk import Combobox, Notebook
from tkMessageBox import*
import MySQLdb
from controller import *

class Inmuebles(Frame):
	
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)
		
		#VARIABLES GLOBALES
		global codigo, direccion, piso, telefono, ciudad, zona, barrio, estrato, llaves, preguntarx, fin, vlrenta, vladmon, incluida, vlventa, vlavaluo, comiventa, pagoprop, fpagoprop, fpagoadmin, tpropiedad, area, lineas, habitaciones, closets, lamparas, duchas, lavamanos, tsala, tcocina, tpiso, tgarage, rutabus, aservicio, ascensor, citofono, aguacaliente, biblioteca, zverdes, terraza, trifilar, parqueadero, observaciones, lb, Cbx1, Cbx2, zona1, zona2, zona3, zona4, zona5, busqueda, dato, E
		#INSTANCIAS DE LOS WIDGETS
		global codE, adressE, comisionE, phoneE, cityCbx, Cbx1, Cbx2, estratoE, keysE, askforE, rent, arriendoE, admonE, include, sale, ventaE, avaluadoE, comiE, pagopropietarioE, diapagopropietarioE, diapagoadmonE, propertyCbx, areaE, lineasE, roomE, closetE, lampE, bathE, sinkE, salasCbx, cocinaCbx, pisoCbx, garageCbx, rutaE, chkb0, chkb1, chkb2, chkb3, chkb4, chkb5, chkb6, chkb7, chkb8, observaciones, add, delete, edit, clean, update
		
		#Variables
		codigo = IntVar()
		direccion =  StringVar()
		piso = IntVar()
		telefono = StringVar()
		ciudad = StringVar()
		zona = StringVar()
		barrio = StringVar()
		estrato = StringVar()
		llaves = StringVar()
		preguntarx = StringVar()
		fin = IntVar()
		vlrenta = IntVar()
		vladmon = IntVar()
		incluida = IntVar()
		vlventa = IntVar()
		vlavaluo = IntVar()
		comiventa = DoubleVar()
		pagoprop = IntVar()
		fpagoprop = IntVar()
		fpagoadmin = IntVar()
		
		tpropiedad = StringVar()
		area = IntVar()
		lineas = IntVar()
		habitaciones = IntVar()
		closets = IntVar()
		lamparas = IntVar()
		duchas = IntVar()
		lavamanos = IntVar()
		tsala = StringVar()
		tcocina = StringVar()
		tpiso = StringVar()
		tgarage = StringVar()
		rutabus = StringVar()
		
		aservicio = IntVar()
		ascensor = IntVar()
		citofono = IntVar()
		aguacaliente = IntVar()
		biblioteca = IntVar()
		zverdes = IntVar()
		terraza = IntVar()
		trifilar = IntVar()
		parqueadero = IntVar()
		
		ciudades = ['Medellín', 'Envigado', 'Caldas', 'El Retiro', 'Guatapé', 'Bogotá D.C', 'Bello', 'Copacabana', 'Rionegro', 'Sabaneta', "Girardot", "Itaguí"]
		zonas = ["Zona 1", "Zona 2", "Zona 3", "Zona 4", "Zona 5"]
		zona1 = ['Centro', 'Manrique', 'Aranjuez', 'Prado', 'Buenos Aires', 'Loreto', 'Milagrosa', 'Villa Hermosa', 'Boston', 'Campo Valdés']
		zona2 = ['Poblado','Patio  Bonito', 'Provenza', 'Castropol', 'Manila', 'San Lucas', 'Envigado', 'El Dorado', 'Loma de Escobero', 'Sabaneta', 'San Diego', 'Las Palmas', 'La Sebastiana']
		zona3 = ['Laureles', 'La América', 'Estadio', 'Santa Mónica', 'Floresta', 'Conquistadores', 'Florida Nueva', 'Robledo', 'Los Colores', 'San Joaquín', 'Castilla', 'Pedregal', 'Tricentenario', 'Bello', 'Florencia', 'Boyacá las Brisas', 'Barrio Nuevo', 'La Mota', 'Calazans', 'Simón Bolivar', 'El Portal', 'Envigado']
		zona4 = ['Rosales', 'Guayabal', 'Belén', 'Itaguí', 'La Estrella', 'Manzanares', 'El Carmelo', 'Mayorca']
		zona5 = ['El Retiro']
		
		negociacion = StringVar()
		propiedades = ['Casa','Apartamento','Local','Local comercial','Local industrial','Oficina','Bodega','Finca','Casa finca','Cabaña','Apartaestudio','Apartalock','Lote','Consultorio','Parqueadero']
		comodidades = ["ALCOBA DE SERVICIO", "ASCENDOR", "CITÓFONO", "AGUA CALIENTE", 
				"BIBLIOTECA", "ZONAS VERDES", "PARQUEADERO VISITANES", "TRIFILAR", 
				"TERRAZA"]
		salas = ['Salón','Salón comedor','Sala garage']
		cocina = ['Integral','Semintegral','Sencilla','Mixta','Cocineta','Integral a gas']
		pisos = ['Baldosa','Mármol','Cerámica','Alfombra','Mármol y Cerámica','Alfombra y Cerámica','Reforzado','Porcelanato','Madera']
		garage = ['Cubierto','Eléctrico','Descubierto','Paralelo']
		
		#busqueda = ["Código","Dirección"]
		busqueda = StringVar()
		busqueda.trace("w", lambda name, index, mode: buscar())
		dato = IntVar()
		
		#WIDGETS
		
		#========================= HEADER ===========================
		
		self.header = Label(self, text="GESTIÓN DE IMNUEBLES", font="bold")
		self.header.pack(pady=20, side=TOP)
		
		#========================== WRAPPER ==========================
		
		self.wrapper = Frame (self)
		self.wrapper.pack(side=LEFT, fill=Y)
		#Esto centro el wrapper
		#self.wrapper.pack(side=LEFT, fill=BOTH, expand=True)
		
		#================ NOTEBOOK =============>
		
		self.nb = Notebook(self.wrapper)
		
		#-----------------------> TAB 1
		
		self.tab1 = Frame (self.nb)
		
		self.f0 = Frame(self.tab1)#Es para dejar un espacio entre el Tab y el Label
		self.f0.pack(fill=X, pady=10)#-------------------------------
		
		self.f1 = Frame(self.tab1)#-------------------------------
		self.f1.pack(pady=5,fill=X)
		
		self.codL = Label(self.f1, text='Código:')
		self.codL.pack(side=LEFT)
		codE = Entry(self.f1, textvariable=codigo, width=5)
		codE.pack(side=LEFT)
		codE.focus_set()
		
		self.adressL = Label(self.f1, text='Dir. Casa:')
		self.adressL.pack(side=LEFT)
		adressE = Entry(self.f1, textvariable=direccion)
		adressE.pack(side=LEFT, fill=X, expand=1)
		adressE.bind("<KeyRelease>", caps)

		self.comisionL = Label(self.f1, text='Piso:')
		self.comisionL.pack(side=LEFT)
		comisionE = Entry(self.f1, textvariable=piso, width=5)
		comisionE.pack(side=LEFT)
		
		self.phoneL = Label(self.f1, text='Tel:')
		self.phoneL.pack(side=LEFT)
		phoneE = Entry(self.f1, textvariable=telefono, width=20)
		phoneE.pack(side=LEFT)
		
		self.f2 = Frame(self.tab1)
		self.f2.pack(pady=5,fill=X)#------------------------------------
		
		self.cityL = Label(self.f2, text='Ciudad:')
		self.cityL.pack(side=LEFT)

		cityCbx = Combobox(self.f2, textvariable=ciudad, values=ciudades, width=10)
		cityCbx.set('')
		cityCbx.pack(side=LEFT, fill=X, expand=1)
		
		self.zoneL = Label(self.f2, text='Zona:')
		self.zoneL.pack(side=LEFT)

		Cbx1 = Combobox(self.f2, textvariable=zona, values=zonas, width=10)
		Cbx1.set('')
		Cbx1.bind("<<ComboboxSelected>>", zone)
		Cbx1.pack(side=LEFT, fill=X, expand=1)
		
		self.neighborL = Label(self.f2, text='Barrio:')
		self.neighborL.pack(side=LEFT)

		Cbx2 = Combobox(self.f2, textvariable=barrio, width=10)
		Cbx2.set('')
		Cbx2.pack(side=LEFT, fill=X, expand=1)
		
		self.estratoL = Label(self.f2, text='Estrato:')
		self.estratoL.pack(side=LEFT)
		estratoE = Entry(self.f2, textvariable=estrato, width=5)
		estratoE.pack(side=LEFT)
		
		self.f3 = Frame(self.tab1)
		self.f3.pack(pady=5,fill=X)#------------------------------------
		
		self.keysL = Label(self.f3, text='Llaves en:')
		self.keysL.pack(side=LEFT)
		keysE = Entry(self.f3, textvariable=llaves, width=24)
		keysE.pack(side=LEFT, fill=X, expand=1)
		keysE.bind("<KeyRelease>", caps)
		
		self.askforL = Label(self.f3, text='Preguntar por:')
		self.askforL.pack(side=LEFT)
		askforE = Entry(self.f3, textvariable=preguntarx, width=24)
		askforE.pack(side=LEFT, fill=X, expand=1)
		askforE.bind("<KeyRelease>", caps)
		
		self.negociacionLF = LabelFrame(self.tab1, text="Valores Negociación")
		self.negociacionLF.pack(anchor=W, pady=5, fill=X)#----------------------

		self.f5a = Frame(self.negociacionLF)
		self.f5a.pack(pady=5,fill=X)#---------------------------

		rent = Radiobutton(self.f5a, text="Se Arrienda: ", variable=fin, value=1)
									
		rent.pack(side=LEFT)

		self.arriendoL = Label(self.f5a, text='Valor $')
		self.arriendoL.pack(side=LEFT)
		arriendoE = Entry(self.f5a, textvariable=vlrenta, width=15)
		arriendoE.pack(side=LEFT)
		
		self.admonL = Label(self.f5a, text='Administración $')
		self.admonL.pack(side=LEFT)
		admonE = Entry(self.f5a, textvariable=vladmon, width=15)
		admonE.pack(side=LEFT)
		
		include = Checkbutton(self.f5a, text="Admin. incluida", variable=incluida)
		include.pack(side=LEFT)
		
		self.f5b = Frame(self.negociacionLF)
		self.f5b.pack(pady=5,fill=X)#---------------------------
		
		sale = Radiobutton(self.f5b, text="Se Vende: ", variable=fin, value=2)
								
		sale.pack(side=LEFT)
		
		self.ventaL = Label(self.f5b, text='Valor $')
		self.ventaL.pack(side=LEFT)
		ventaE = Entry(self.f5b, textvariable=vlventa, width=15)
		ventaE.pack(side=LEFT)
		
		self.avaluadoL = Label(self.f5b, text='Avaluado $')
		self.avaluadoL.pack(side=LEFT)
		avaluadoE = Entry(self.f5b, textvariable=vlavaluo, width=15)
		avaluadoE.pack(side=LEFT)
		
		self.comiL = Label(self.f5b, text='Comisión Venta')
		self.comiL.pack(side=LEFT)
		comiE = Entry(self.f5b, textvariable=comiventa, width=5)
		comiE.pack(side=LEFT)
		self.porcentL = Label(self.f5b, text='%')
		self.porcentL.pack(side=LEFT)
		
		self.pagoLF = LabelFrame(self.tab1, text="Detalles de pago")
		self.pagoLF.pack(anchor=W, pady=5, fill=X)#-----------

		self.f6 = Frame(self.pagoLF)
		self.f6.pack(pady=5,fill=X)#---------------------------
		
		self.pagopropietarioL = Label(self.f6, text='$ Pago Propietario:')
		self.pagopropietarioL.pack(side=LEFT)
		pagopropietarioE = Entry(self.f6, textvariable=pagoprop, width=10)
		pagopropietarioE.pack(side=LEFT, fill=X, expand=1)
		
		self.diapagopropietarioL = Label(self.f6, text='Día Pago Propietario:')
		self.diapagopropietarioL.pack(side=LEFT)
		diapagopropietarioE = Entry(self.f6, textvariable=fpagoprop, width=5)
		diapagopropietarioE.pack(side=LEFT)
		
		self.diapagoadmonL = Label(self.f6, text='Día Pago Admon:')
		self.diapagoadmonL.pack(side=LEFT)
		diapagoadmonE = Entry(self.f6, textvariable=fpagoadmin, width=5)
		diapagoadmonE.pack(side=LEFT)
		
		self.tab1.pack()
		
		#-----------------------> TAB 2
		
		self.tab2 = Frame (self.nb)
		self.tab2.pack()
		
		self.f0 = Frame(self.tab2)
		self.f0.pack(fill=X, pady=10)#-------------------------------
		
		self.f1 = Frame(self.tab2)
		self.f1.pack(fill=X)#-------------------------------
		
		self.propertyL = Label(self.f1, text='Tipo Propiedad:')
		self.propertyL.pack(side=LEFT)
		
		propertyCbx = Combobox(self.f1, textvariable=tpropiedad, values=propiedades, width=15)
		propertyCbx.set('')
		propertyCbx.pack(side=LEFT)

		self.areaL = Label(self.f1, text='Área:')
		self.areaL.pack(side=LEFT)
		areaE = Entry(self.f1, textvariable=area, width=5)
		areaE.pack(side=LEFT)
		self.m2L = Label(self.f1, text='m2')
		self.m2L.pack(side=LEFT)
		
		self.emptyL = Label(self.f1)###VACIO###
		self.emptyL.pack(padx=5, side=LEFT)
		
		self.lineasL = Label(self.f1, text='# Líneas:')
		self.lineasL.pack(side=LEFT)
		lineasE = Entry(self.f1, textvariable=lineas, width=5)
		lineasE.pack(side=LEFT)
		
		self.roomL = Label(self.f1, text='# Habitaciones:')
		self.roomL.pack(side=LEFT)
		roomE = Entry(self.f1, textvariable=habitaciones, width=5)
		roomE.pack(side=LEFT)

		self.f2 = Frame(self.tab2)#-------------------------------
		self.f2.pack(pady=5,fill=X)

		self.closetL = Label(self.f2, text='# Closets:')
		self.closetL.pack(side=LEFT)
		closetE = Entry(self.f2, textvariable=closets, width=5)
		closetE.pack(side=LEFT)
		
		self.lampL = Label(self.f2, text='# Lámparas:')
		self.lampL.pack(side=LEFT)
		lampE = Entry(self.f2, textvariable=lamparas, width=5)
		lampE.pack(side=LEFT)
		
		self.bathL = Label(self.f2, text='# Baños:')
		self.bathL.pack(side=LEFT)
		bathE = Entry(self.f2, textvariable=duchas, width=5)
		bathE.pack(side=LEFT)
		
		self.sinkL = Label(self.f2, text='# Lavamanos:')
		self.sinkL.pack(side=LEFT)
		sinkE = Entry(self.f2, textvariable=lavamanos, width=5)
		sinkE.pack(side=LEFT)

		self.f4 = Frame(self.tab2)
		self.f4.pack(pady=5,fill=X)#-------------------------------
		
		self.salaL = Label(self.f4, text='Tipo Sala:')
		self.salaL.pack(side=LEFT)
		
		salasCbx = Combobox(self.f4, textvariable=tsala, values=salas)
		salasCbx.set('')
		salasCbx.pack(side=LEFT)
		
		self.cocinaL = Label(self.f4, text='Tipo Cocina:')
		self.cocinaL.pack(side=LEFT)
		
		cocinaCbx = Combobox(self.f4, textvariable=tcocina, values=cocina)
		cocinaCbx.set('')
		cocinaCbx.pack(side=LEFT)

		self.f5 = Frame(self.tab2)
		self.f5.pack(pady=5,fill=X)#-------------------------------

		self.pisoL = Label(self.f5, text='Tipo Piso:')
		self.pisoL.pack(side=LEFT)
		
		pisoCbx = Combobox(self.f5, textvariable=tpiso, values=pisos)
		pisoCbx.set('')
		pisoCbx.pack(side=LEFT)
		
		self.garageL = Label(self.f5, text='Tipo garage:')
		self.garageL.pack(side=LEFT)
		
		garageCbx = Combobox(self.f5, textvariable=tgarage, values=garage)
		garageCbx.set('')
		garageCbx.pack(side=LEFT)

		self.f6 = Frame(self.tab2)#-------------------------------
		self.f6.pack(pady=5,fill=X)

		self.rutaL = Label(self.f6, text='Ruta de Buses:')
		self.rutaL.pack(side=LEFT)
		rutaE = Entry(self.f6, textvariable=rutabus, width=30)
		rutaE.pack(side=LEFT)

		self.f7 = Frame(self.tab2)
		self.f7.pack(pady=5,fill=X)#-------------------------------
		
		self.comodidades = LabelFrame(self.f7, text="Comodidades:")
		self.comodidades.pack(anchor=W, pady=5, fill=X, expand=1)#----------------------
		
		chkb0 = Checkbutton(self.comodidades, text="ALCOBA DE SERVICIO", variable=aservicio)
		chkb0.grid(row=0, column=0, sticky=W)
		chkb1 = Checkbutton(self.comodidades, text="ASCENSOR", variable=ascensor)
		chkb1.grid(row=0, column=1, sticky=W)
		chkb2 = Checkbutton(self.comodidades, text="CITÓFONO", variable=citofono)
		chkb2.grid(row=0, column=2, sticky=W)
		chkb3 = Checkbutton(self.comodidades, text="AGUA CALIENTE", variable=aguacaliente)
		chkb3.grid(row=0, column=3, sticky=W)
		
		chkb4 = Checkbutton(self.comodidades, text="BIBLIOTECA", variable=biblioteca)
		chkb4.grid(row=1, column=0, sticky=W)
		chkb5 = Checkbutton(self.comodidades, text="ZONAS VERDES", variable=zverdes)
		chkb5.grid(row=1, column=1, sticky=W)
		chkb6 = Checkbutton(self.comodidades, text="TERRAZA", variable=terraza)
		chkb6.grid(row=1, column=2, sticky=W)
		chkb7 = Checkbutton(self.comodidades, text="TRIFILAR", variable=trifilar)
		chkb7.grid(row=1, column=3, sticky=W)
		
		chkb8 = Checkbutton(self.comodidades, text="PARQUEADERO VISITANTES", variable=parqueadero)
		chkb8.grid(row=2, column=0, sticky=W)
		
		self.f9 = Frame(self.tab2)
		self.f9.pack(pady=5,fill=X)#------------------------------------

		self.notesL = Label(self.f9, text='Observaciones:')
		self.notesL.pack(side=LEFT)

		self.f10 = Frame(self.tab2)
		self.f10.pack(pady=5,fill=X)#-----------------------------------

		observaciones = Text(self.f10, height=5)
		observaciones.pack(side=LEFT, fill=X, expand=1)
	
		#---------------------------------------------------------------
		
		self.nb.add (self.tab1, text="Datos Generales")
		self.nb.add(self.tab2, text="Inventario y Comodidades")
		
		self.nb.pack()
		
		#=========================== BOTONES ===========================
		
		self.fBtn = Frame(self.wrapper)
		self.fBtn.pack()#-------------------------------
	
		clean = Button(self.fBtn, text='Limpiar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=limpiar)
		clean.pack(side=RIGHT)
		
		update = Button(self.fBtn, text='Actualizar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=actualizar, state=DISABLED)
		update.pack(side=RIGHT)
		
		add = Button(self.fBtn, text='Agregar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=Agregar)
		add.pack(side=RIGHT)
		
		#========================= ASIDE ===========================
		
		self.aside = Frame(self)
		self.aside.pack(side=TOP, fill=BOTH)
		
		self.wrap1 = Frame(self.aside)
		self.wrap1.pack()
		
		self.viewer = Label(self.wrap1, text="LISTA DE INMUEBLES")
		self.viewer.pack()

		scroll = Scrollbar(self.wrap1, orient=VERTICAL)
		scroll.pack(side=RIGHT, fill=Y)
		lb = Listbox(self.wrap1, yscrollcommand=scroll.set, height=20, width=30, bg='#d8ecf3')
		scroll.config (command=lb.yview)
		lb.pack(fill=BOTH)
		lb.bind("<Double-Button-1>", callback)
		
		self.wrap2 = Frame(self.aside)
		self.wrap2.pack()
		
		self.updateBP = Button(self.wrap2, text='Cargar lista', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=cargar_lista)
		self.updateBP.pack(fill=X)
		
		delete = Button(self.wrap2, text='Borrar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=borrar)
		delete.pack(fill=X)
		
		edit = Button(self.wrap2, text='Modificar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=modificar)
		edit.pack(fill=X)
		
		buscador = Label(self.wrap2, text="Buscar por Código:")
		buscador.pack()
		E = Entry(self.wrap2, textvariable=busqueda, width=24)
		E.pack()
		E.bind("<KeyRelease>", caps)

def cargar_lista():
	try:
		connect.commit()
		display = "SELECT i_dir FROM inmuebles order by i_dir;"
		cursor.execute(display)
		registros = cursor.fetchall()
		lb.delete(0, END)
		for item in registros:
			#print item
			loc = item[0]
			lb.insert(END, loc)
	except:
		showerror ("Mensaje", "Ha ocurrido un error")

def limpiar():
	codigo.set(0)
	direccion.set("")
	piso.set(0)
	telefono.set("")
	ciudad.set("")
	zona.set("")
	barrio.set("")
	estrato.set("")
	llaves.set("")
	preguntarx.set("")
	fin.set(0)
	vlrenta.set(0)
	vladmon.set(0)
	incluida.set(0)
	vlventa.set(0)
	vlavaluo.set(0)
	comiventa.set(0.0)
	pagoprop.set(0)
	fpagoprop.set(0)
	fpagoadmin.set(0)
	tpropiedad.set("")
	area.set(0)
	lineas.set(0)
	habitaciones.set(0)
	closets.set(0)
	lamparas.set(0)
	duchas.set(0)
	lavamanos.set(0)
	tsala.set("")
	tcocina.set("")
	tpiso.set("")
	tgarage.set("")
	rutabus.set("")
	aservicio.set(0)
	ascensor.set(0)
	citofono.set(0)
	aguacaliente.set(0)
	biblioteca.set(0)
	zverdes.set(0)
	terraza.set(0)
	trifilar.set(0)
	parqueadero.set(0)
	#observaciones.delete('1.0', '2.0')
	observaciones.delete('1.0', END)
	habilitar()
	
	codE.configure(state="normal")
	add.configure(state="normal")
	update.configure(state="disabled")

def Agregar():
	try:
		d0 = codigo.get()
		d1 = direccion.get()
		d2 = piso.get()
		d3 = telefono.get()
		d4 = ciudad.get()
		d5 = zona.get()
		d6 = Cbx2.get()
		#d6 = barrio.get()
		d7 = estrato.get()
		d8 = llaves.get()
		d9 = preguntarx.get()
		d10 = fin.get()
		d11 = vlrenta.get()
		d12 = vladmon.get()
		d13 = incluida.get()
		d14 = vlventa.get()
		d15 = vlavaluo.get()
		d16 = comiventa.get()
		d17 = pagoprop.get()
		d18 = fpagoprop.get()
		d19 = fpagoadmin.get()
		d20 = tpropiedad.get()
		d21 = area.get()
		d22 = lineas.get()
		d23 = habitaciones.get()
		d24 = closets.get()
		d25 = lamparas.get()
		d26 = duchas.get()
		d27 = lavamanos.get()
		d28 = tsala.get()
		d29 = tcocina.get()
		d30 = tpiso.get()
		d31 = tgarage.get()
		d32 = rutabus.get()
		d33 = aservicio.get()
		d34 = ascensor.get()
		d35 = citofono.get()
		d36 = aguacaliente.get()
		d37 = biblioteca.get()
		d38 = zverdes.get()
		d39 = terraza.get()
		d40 = trifilar.get()
		d41 = parqueadero.get()
		d42 = observaciones.get("1.0",END)
		
		connect.commit()
		sql = "INSERT INTO inmuebles (i_cod, i_dir, i_piso, i_tel, i_ciudad, i_zona, i_barrio, i_estrato, i_llaves, i_preguntarx, i_fin, i_vlrenta, i_vladmon, i_incluida, i_vlventa, i_vlavaluo, i_comiventa, i_vlpagoprop, i_dpagoprop, i_dpagoadmon, i_tipo, i_area, i_lineas, i_cuartos, i_closets, i_lamps, i_duchas, i_lavamanos, i_tsala, i_tcocina, i_tpiso, i_tgarage, i_rutabus, i_aservicio, i_ascensor, i_citofono, i_aguacaliente, i_biblioteca, i_zverdes, i_terraza, i_trifilar, i_parqueadero, i_notas) VALUES ('%d', '%s', '%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%d', '%d', '%d', '%d', '%d', '%f', '%d', '%d', '%d', '%s', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%s', '%s', '%s', '%s', '%s', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%s');" % (d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27, d28, d29, d30, d31, d32, d33, d34, d35, d36, d37, d38, d39, d40, d41, d42)
		cursor.execute(sql)
		showinfo ("Mensaje", "Datos guardados")
		limpiar()
		cargar_lista()
		
	except MySQLdb.IntegrityError, e:
		showerror("Error", e)
		#showerror ("Error", "Este registro ya se escuentra guardado!")

def borrar():
	try:
		k = lb.curselection()
		value = lb.get(k[0])
		delete = """DELETE FROM inmuebles WHERE i_dir=("%s");""" % (value)
		cursor.execute(delete)
		connect.commit()
		lb.delete(k)
		showinfo("mensaje", "Dato Borrado!")
		lb.delete(0, END)
		cargar_lista()
		limpiar()
		
	except MySQLdb.IntegrityError, e:
		showerror("Error",e)
		#showerror ('Mensaje', "No se puede borrar o actualizar porque hace parte de una relación.")

def bloquear():
	codE.configure(state="disabled")
	adressE.configure(state="disabled")
	comisionE.configure(state="disabled")
	phoneE.configure(state="disabled")
	cityCbx.configure(state="disabled")
	Cbx1.configure(state="disabled")
	Cbx2.configure(state="disabled")
	estratoE.configure(state="disabled")
	keysE.configure(state="disabled")
	askforE.configure(state="disabled")
	rent.configure(state="disabled")			
	arriendoE.configure(state="disabled")
	admonE.configure(state="disabled")
	include.configure(state="disabled")
	sale.configure(state="disabled")
	ventaE.configure(state="disabled")
	avaluadoE.configure(state="disabled")
	comiE.configure(state="disabled")
	pagopropietarioE.configure(state="disabled")
	diapagopropietarioE.configure(state="disabled")
	diapagoadmonE.configure(state="disabled")
	
	propertyCbx.configure(state="disabled")
	areaE.configure(state="disabled")
	lineasE.configure(state="disabled")
	roomE.configure(state="disabled")
	closetE.configure(state="disabled")
	lampE.configure(state="disabled")
	bathE.configure(state="disabled")
	sinkE.configure(state="disabled")
	salasCbx.configure(state="disabled")
	cocinaCbx.configure(state="disabled")
	pisoCbx.configure(state="disabled")
	garageCbx.configure(state="disabled")
	rutaE.configure(state="disabled")
	chkb0.configure(state="disabled")
	chkb1.configure(state="disabled")
	chkb2.configure(state="disabled")
	chkb3.configure(state="disabled")
	chkb4.configure(state="disabled")
	chkb5.configure(state="disabled")
	chkb6.configure(state="disabled")
	chkb7.configure(state="disabled")
	chkb8.configure(state="disabled")
	observaciones.configure(state="disabled")

# LLENAR CAMPOS CON DOBLE CLIC
def callback(event):
    llenar_campos()

def llenar_campos():	
	i = lb.curselection()[0]
	valor = lb.get(i)
	
	#CONSULTAR ESTADO DEL INMUEBLE EN LA TABLA contratos
	#check = "SELECT c_estado FROM contratos WHERE "
	#cursor.execute(check)
	
	edit = """SELECT * FROM inmuebles WHERE i_dir=("%s");""" % (valor)
	cursor.execute(edit)
	result = cursor.fetchall()
	connect.commit()
	for item in result:
		i0 = item[1]
		i1 = item[2] #
		i2 = item[3] #
		i3 = item[4] #
		i4 = item[5] #
		i5 = item[6] #
		i6 = item[7] #
		i7 = item[8] #
		i8 = item[9] #
		i9 = item[10] #
		i10 = item[11] #
		i11 = item[12] #
		i12 = item[13] #
		i13 = item[14] #
		i14 = item[15] #
		i15 = item[16] #
		i16 = item[17] #
		i17 = item[18] #
		i18 = item[19] #
		i19 = item[20] #
		i20 = item[21] #
		i21 = item[22] #
		i22 = item[23] #
		i23 = item[24] #
		i24 = item[25] #
		i25 = item[26] #
		i26 = item[27] #
		i27 = item[28] #
		i28 = item[29] #
		i29 = item[30] #
		i30 = item[31] #
		i31 = item[32] #
		i32 = item[33] #
		i33 = item[34] #
		i34 = item[35] #
		i35 = item[36] #
		i36 = item[37] #
		i37 = item[38] #
		i38 = item[39] #
		i39 = item[40] #
		i40 = item[41] #
		i41= item[42] #
		i42 = item[43] #
		
		codigo.set(i0)
		direccion.set(i1)
		piso.set(i2)
		telefono.set(i3)
		ciudad.set(i4)
		zona.set(i5)
		barrio.set(i6)
		estrato.set(i7)
		llaves.set(i8)
		preguntarx.set(i9)
		fin.set(i10)
		vlrenta.set(i11)
		vladmon.set(i12)
		incluida.set(i13)
		vlventa.set(i14)
		vlavaluo.set(i15)
		comiventa.set(i16)
		pagoprop.set(i17)
		fpagoprop.set(i18)
		fpagoadmin.set(i19)
		tpropiedad.set(i20)
		area.set(i21)
		lineas.set(i22)
		habitaciones.set(i23)
		closets.set(i24)
		lamparas.set(i25)
		duchas.set(i26)
		lavamanos.set(i27)
		tsala.set(i28)
		tcocina.set(i29)
		tpiso.set(i30)
		tgarage.set(i31)
		rutabus.set(i32)
		aservicio.set(i33)
		ascensor.set(i34)
		citofono.set(i35)
		aguacaliente.set(i36)
		biblioteca.set(i37)
		zverdes.set(i38)
		terraza.set(i39)
		trifilar.set(i40)
		parqueadero.set(i41)
		observaciones.insert('1.0',i42)
		
		bloquear()
		
def habilitar():
	
	codE.configure(state="normal")
	adressE.configure(state="normal")
	comisionE.configure(state="normal")
	phoneE.configure(state="normal")
	cityCbx.configure(state="normal")
	Cbx1.configure(state="normal")
	Cbx2.configure(state="normal")
	estratoE.configure(state="normal")
	keysE.configure(state="normal")
	askforE.configure(state="normal")
	rent.configure(state="normal")			
	arriendoE.configure(state="normal")
	admonE.configure(state="normal")
	include.configure(state="normal")
	sale.configure(state="normal")
	ventaE.configure(state="normal")
	avaluadoE.configure(state="normal")
	comiE.configure(state="normal")
	pagopropietarioE.configure(state="normal")
	diapagopropietarioE.configure(state="normal")
	diapagoadmonE.configure(state="normal")
	
	propertyCbx.configure(state="normal")
	areaE.configure(state="normal")
	lineasE.configure(state="normal")
	roomE.configure(state="normal")
	closetE.configure(state="normal")
	lampE.configure(state="normal")
	bathE.configure(state="normal")
	sinkE.configure(state="normal")
	salasCbx.configure(state="normal")
	cocinaCbx.configure(state="normal")
	pisoCbx.configure(state="normal")
	garageCbx.configure(state="normal")
	rutaE.configure(state="normal")
	chkb0.configure(state="normal")
	chkb1.configure(state="normal")
	chkb2.configure(state="normal")
	chkb3.configure(state="normal")
	chkb4.configure(state="normal")
	chkb5.configure(state="normal")
	chkb6.configure(state="normal")
	chkb7.configure(state="normal")
	chkb8.configure(state="normal")
	observaciones.configure(state="normal")

def modificar():
	try:
		llenar_campos()
		habilitar()
		codE.configure(state="disabled")
		add.configure(state="disabled")
		update.configure(state="normal")
		clean.config(text='Cancelar')
		
	except IndexError, e:
		showerror("Error", e)

def actualizar():
	d0 = codigo.get()
	d1 = direccion.get()
	d2 = piso.get()
	d3 = telefono.get()
	d4 = ciudad.get()
	d5 = zona.get()
	d6 = Cbx2.get()
	#d6 = barrio.get()
	d7 = estrato.get()
	d8 = llaves.get()
	d9 = preguntarx.get()
	d10 = fin.get()
	d11 = vlrenta.get()
	d12 = vladmon.get()
	d13 = incluida.get()
	d14 = vlventa.get()
	d15 = vlavaluo.get()
	d16 = comiventa.get()
	d17 = pagoprop.get()
	d18 = fpagoprop.get()
	d19 = fpagoadmin.get()
	d20 = tpropiedad.get()
	d21 = area.get()
	d22 = lineas.get()
	d23 = habitaciones.get()
	d24 = closets.get()
	d25 = lamparas.get()
	d26 = duchas.get()
	d27 = lavamanos.get()
	d28 = tsala.get()
	d29 = tcocina.get()
	d30 = tpiso.get()
	d31 = tgarage.get()
	d32 = rutabus.get()
	d33 = aservicio.get()
	d34 = ascensor.get()
	d35 = citofono.get()
	d36 = aguacaliente.get()
	d37 = biblioteca.get()
	d38 = zverdes.get()
	d39 = terraza.get()
	d40 = trifilar.get()
	d41 = parqueadero.get()
	d42 = observaciones.get("1.0",END)
	
	connect.commit()
	
	sql = "UPDATE inmuebles SET i_dir='%s', i_piso='%d', i_tel='%s', i_ciudad='%s', i_zona='%s', i_barrio='%s', i_estrato='%s', i_llaves='%s', i_preguntarx='%s', i_fin='%d', i_vlrenta='%d', i_vladmon='%d', i_incluida='%d', i_vlventa='%d', i_vlavaluo='%d', i_comiventa='%f', i_vlpagoprop='%d', i_dpagoprop='%d', i_dpagoadmon='%d', i_tipo='%s', i_area='%d', i_lineas='%d', i_cuartos='%d', i_closets='%d', i_lamps='%d', i_duchas='%d', i_lavamanos='%d', i_tsala='%s', i_tcocina='%s', i_tpiso='%s', i_tgarage='%s', i_rutabus='%s', i_aservicio='%d', i_ascensor='%d', i_citofono='%d', i_aguacaliente='%d', i_biblioteca='%d', i_zverdes='%d', i_terraza='%d', i_trifilar='%d', i_parqueadero='%d', i_notas='%s' WHERE i_cod='%d'" % (d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27, d28, d29, d30, d31, d32, d33, d34, d35, d36, d37, d38, d39, d40, d41, d42, d0)
	cursor.execute(sql)
	showinfo ("Mensaje", "Datos actualizados!")
	
	cargar_lista()
	limpiar()
	#habilitar()
	
	codE.configure(state="normal")
	add.configure(state="normal")
	update.configure(state="disabled")
	#El siguiente error sale cuando se deja el espacio del vlrenta en blanco
	#ValueError: invalid literal for int() with base 10: '0.0'
	
def buscar():
	dato = busqueda.get()
	connect.commit()
	display = """SELECT i_dir FROM inmuebles WHERE i_cod=("%s");""" % (dato)
	cursor.execute(display)
	registros = cursor.fetchall()
	lb.delete(0, END)
	for item in registros:
		lb.insert(END, item)
		
def caps(event):
	direccion.set(direccion.get().upper())
	llaves.set(llaves.get().upper())
	preguntarx.set(preguntarx.get().upper())
		
def zone(event):
	if Cbx1.get() == "Zona 1":
		Cbx2['values']=zona1
	if Cbx1.get() == "Zona 2":
		Cbx2['values']=zona2
	if Cbx1.get() == "Zona 3":
		Cbx2['values']=zona3
	if Cbx1.get() == "Zona 4":
		Cbx2['values']=zona4
	if Cbx1.get() == "Zona 5":
		Cbx2['values']=zona5
