#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from ttk import Combobox, Treeview
from tkMessageBox import*
import os
import datetime
from time import localtime,strftime,time
import time
import locale
locale.setlocale(locale.LC_ALL, "")
import MySQLdb
from controller import *
#Librerias Reportlab a usar:
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,
Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
styleSheet = getSampleStyleSheet()
style = styleSheet['BodyText']

class Gastos(Frame):
        def __init__(self, parent, controller):
			Frame.__init__(self, parent)
			
			#INSTANCIAS
			global cc, nombre, pago, ref, cod, desc, valor, resultado, total, tiempo, mes, anio, fechapago
			#INSTANCIAS DE LOS WIDGETS
			global e1, e2, e3, e4, e5, tree, l8, lb
			
			cc = IntVar()
			nombre = StringVar()
			pago = StringVar()
			ref = StringVar()
			cod = StringVar()
			desc = StringVar()
			valor = DoubleVar()
			
			tiempo = datetime.date.today()
			anio = time.strftime("%Y")
			mes = time.strftime("%B")
			fechapago = StringVar()
			
			total = 0.0
			resultado = DoubleVar()
			
			tbancos = ['Bancolombia', "Banco Bogotá", "Banco Agrario", "Banco Occidente"]
			
			lupa = PhotoImage(file='img/lupa.png')
			
			tbanktype = ['Corriente','Ahorro']
			fpago = ['Efectivo','Transferencia']
			
			#BUSQUEDA = ["Nombre","CC/Nit"]
			busqueda = StringVar()
			busqueda.trace("w", lambda name, index, mode: buscar())
			dato = StringVar()
			
			#WIDGETS
			
			#========================= HEADER ==============================
			
			self.titleL = Label(self, text="GASTOS", font="bold")
			self.titleL.pack(pady=20, side=TOP)
			
			#========================== WRAPPER ============================
			
			self.wrapper = Frame (self)
			self.wrapper.pack(side=LEFT, fill=Y)
			#Esto centro el wrapper
			#self.wrapper.pack(side=LEFT, fill=BOTH, expand=True)
			
			#======================== BENEFICIARIO =======================
			
			self.lf1 = LabelFrame(self.wrapper, text="Beneficiario")
			self.lf1.pack(fill=X, ipady=5)
			
			self.f0 = Frame(self.lf1)
			self.f0.pack(pady=5, fill=X)#-----------------------------------
			
			l1 = Label(self.f0, text='CC/Nit:')
			l1.pack(side=LEFT)
			
			e1 = Entry(self.f0, textvariable=cc)
			e1.pack(side=LEFT)
			e1.bind('<Return>', buscarB)
			
			b0 = Button(self.f0, text='Buscar:', image=lupa, command=topBeneficiarios)
			b0.pack(side=LEFT)
			
			l2 = Label(self.f0, text='Nombre:')
			l2.pack(side=LEFT)
			e2 = Entry(self.f0, textvariable=nombre)
			e2.pack(side=LEFT, fill=X, expand=1)
			
			self.f1 = Frame(self.lf1)
			self.f1.pack(pady=5, fill=X)#-----------------------------------
			
			l3 = Label(self.f1, text='Forma de Pago:')
			l3.pack(side=LEFT)
			Cbx = Combobox(self.f1, textvariable=pago, values=fpago, width=15)
			Cbx.set('Efectivo')
			Cbx.pack(side=LEFT)
			
			l4 = Label(self.f1, text='Ref. Bancaria:')
			l4.pack(side=LEFT)
			e3 = Entry(self.f1, textvariable=ref)
			e3.pack(side=LEFT, fill=X, expand=1)
			
			b1 = Button(self.f1, text='Buscar:', image=lupa)
			b1.image=lupa
			b1.pack(side=LEFT)
			
			#======================== CONCEPTO ========================
			
			self.lf2 = LabelFrame(self.wrapper, text="Concepto")
			self.lf2.pack(fill=X, ipady=5)
			
			self.f2 = Frame(self.lf2)
			self.f2.pack(pady=5, fill=X)#-------------------------------
			
			l5 = Label(self.f2, text='Código:')
			l5.pack(side=LEFT)
			e4 = Entry(self.f2, textvariable=cod)
			e4.pack(side=LEFT)
			e4.bind('<Return>', buscarC)
			
			b2 = Button(self.f2, text='Buscar:', image=lupa, command=topCtasContables)
			b2.pack(side=LEFT)
			
			self.f3 = Frame(self.lf2)
			self.f3.pack(pady=5, fill=X)#-------------------------------
			
			l6 = Label(self.f3, text='Descripción:')
			l6.pack(side=LEFT)
			e5 = Entry(self.f3, textvariable=desc, state=DISABLED)
			e5.pack(side=LEFT, fill=X, expand=1)
			
			l7 = Label(self.f3, text='Valor:')
			l7.pack(side=LEFT)
			e6 = Entry(self.f3, width=15, textvariable=valor)
			e6.pack(side=LEFT)
			
			b3 = Button(self.f3, text='Agregar:', command=agregar)
			b3.pack(side=LEFT)
			
			#-------------------------- TREEVIEW ---------------------------
			
			self.f4 = Frame(self.wrapper)
			self.f4.pack(pady=5,fill=X)
			
			tree = Treeview(self.f4, height=4, show="headings", columns=('col1','col2','col3'))
			tree.pack(side=LEFT, fill=X, expand=1)
			tree.column('col1', width=20, anchor='center')
			tree.column('col2', width=200, anchor='center')
			tree.column('col3', width=10, anchor='center')
			
			tree.heading('col1', text='Código')
			tree.heading('col2', text='Concepto')
			tree.heading('col3', text='Valor')
			
			scroll = Scrollbar(self.f4,orient=VERTICAL,command=tree.yview)
			tree.configure(yscrollcommand=scroll.set)
			tree.bind("<Delete>", borrar)
			
			#-------------------------- RESULTADOS ---------------------------
			
			self.f5 = Frame(self.wrapper)
			self.f5.pack(pady=5,fill=X)#-------------------
			
			l8 = Label(self.f5, textvariable=resultado, fg="red", bg="white", anchor='e', font="bold, 22", relief= SUNKEN)
			l8.pack(fill=X, side=RIGHT, expand=1)
			
			#-------------------------- FOOTER ---------------------------
			
			self.fBtn = Frame(self.wrapper)
			self.fBtn.pack()#-------------------------------
			
			clean = Button(self.fBtn, text='Cancelar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=limpiar)
			clean.pack(side=RIGHT)
			
			add = Button(self.fBtn, text='Grabar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=grabar)
			add.pack(side=RIGHT)
			
			#========================= ASIDE ===========================
			
			self.aside = Frame(self)
			self.aside.pack(side=TOP, fill=BOTH)
			
			self.wrap1 = Frame(self.aside)
			self.wrap1.pack()
			
			self.viewer = Label(self.wrap1, text="LISTA DE GASTOS")
			self.viewer.pack()
			
			scroll = Scrollbar(self.wrap1, orient=VERTICAL)
			scroll.pack(side=RIGHT, fill=Y)
			
			lb = Listbox(self.wrap1, yscrollcommand=scroll.set, height=20, width=30)
			scroll.config (command=lb.yview)
			lb.pack(fill=BOTH)
			
			self.wrap2 = Frame(self.aside)
			self.wrap2.pack()
			
			load = Button(self.wrap2, text='Cargar lista', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=cargar_lista)
			load.pack(fill=X)
			
			delete = Button(self.wrap2, text='Borrar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=None)
			delete.pack(fill=X)
			
			edit = Button(self.wrap2, text='Modificar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=None)
			edit.pack(fill=X)
			
			buscador = Label(self.wrap2, text="Buscar por Número:")
			buscador.pack()
			E = Entry(self.wrap2, textvariable=busqueda, width=24)
			E.pack()
			E.bind("<KeyRelease>", caps)

def buscarB(event):
	connect.commit()
	try:
		v = cc.get()
		sql = "SELECT b_nombre from beneficiarios WHERE b_cc='%d';" % (v)
		cursor.execute(sql)
		query = cursor.fetchone()
		for n in query:
			nombre.set(n)
	except TypeError, e:
		showerror("Error", e)
		
	except MySQLdb.IntegrityError, e:
		showerror("Error", e)

def topBeneficiarios():
	global topB, topB_scroll, topB_lb
	
	topB = Toplevel()
	topB.title("Beneficiarios")
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
	topB_lb.bind("<Double-Button-1>", cargarBeneficiario)
	
	try:
		connect.commit()
		display = "SELECT b_nombre FROM beneficiarios;"
		cursor.execute(display)
		registros = cursor.fetchall()
		topB_lb.delete(0, END)
		for item in registros:
			nombres = item[0]
			topB_lb.insert(END, nombres)
	except:
		showerror("Error", "Error al cargar los beneficiarios")

def cargarBeneficiario(event):
	i = topB_lb.curselection()[0]
	val = topB_lb.get(i)
	connect.commit()
	edit = "SELECT b_cc, b_nombre FROM beneficiarios WHERE b_nombre=('%s');" % (val)
	cursor.execute(edit)
	sol = cursor.fetchall()
	for item in sol:
		d1 = item[0] #b_cc
		d2 = item[1] #b_nombre
		cc.set(d1)
		nombre.set(d2)
	topB.destroy()

def buscarC(event):
	connect.commit()
	try:
		v = cod.get()
		sql = "SELECT cc_desc from cuentas_contables WHERE cc_cod='%s';" % (v)
		cursor.execute(sql)
		query = cursor.fetchone()
		for n in query:
			desc.set(n)
	except TypeError, e:
		showerror("Error", e)
		
	except MySQLdb.IntegrityError, e:
		showerror("Error", e)
	except:
		showerror ("Mensaje", "No se encuentra!")

def topCtasContables():
	global topC, topC_scroll, topC_lb
	
	topC = Toplevel()
	topC.title("Cuentas Contables")
	topC.geometry("300x300")
	
	topC.wm_attributes("-topmost", 1)#Inabilitar este en WIN
	topC.focus_set()#Mantiene el toplevel sobre root/w
	topC.transient() #Se minimiza solo cuando root lo hace
	topC.grab_set() #Impite que se interactue con la ventana root/w
			
	topC_scroll = Scrollbar(topC, orient=VERTICAL)
	topC_scroll.pack(side=RIGHT, fill=Y)
	topC_lb = Listbox(topC, yscrollcommand=topC_scroll.set, height=20, width=20)
	topC_scroll.config (command=topC_lb.yview)
	topC_lb.pack(fill=BOTH)
	topC_lb.bind("<Double-Button-1>", cargarCtasContables)
	
	try:
		connect.commit()
		display = "SELECT cc_desc FROM cuentas_contables;"
		cursor.execute(display)
		registros = cursor.fetchall()
		topC_lb.delete(0, END)
		for item in registros:
			nombres = item[0]
			topC_lb.insert(END, nombres)
	except:
		showerror("Error", "Error al cargar los ctas contables")

def cargarCtasContables(event):
	i = topC_lb.curselection()[0]
	val = topC_lb.get(i)
	connect.commit()
	edit = "SELECT cc_cod, cc_desc FROM cuentas_contables WHERE cc_desc=('%s');" % (val)
	cursor.execute(edit)
	sol = cursor.fetchall()
	for item in sol:
		d1 = item[0] #cc_cod
		d2 = item[1] #cc_desc
		cod.set(d1)
		desc.set(d2)
	topC.destroy()

def agregar():
	v1 = cc.get()
	v2 = nombre.get()
	v3 = cod.get()
	v4 = desc.get()
	v5 = valor.get()
	
	resultado.set(resultado.get() + v5)
	tree.insert('', 0, values=(v3,v4,v5))
	
	cod.set(0)
	desc.set("")
	valor.set(0.0)
	e4.focus()

def borrar(event):
	i = tree.selection()[0] #get selected item
	x = float(tree.item(i,'values')[2])
	tree.delete(i)
	resultado.set(resultado.get()-x)
	e4.focus()

def caps(event):
	nombre.set(name.get().upper())
	desc.set(desc.get().upper())
	
# NUEVO / CANCELAR
def limpiar():
	for row in tree.get_children():
		tree.delete(row)
	#También funciona:
	#tree.delete(*tree.get_children())
	cc.set(0)
	nombre.set("")
	cod.set("")
	desc.set("")
	valor.set(0.0)
	resultado.set(0.0)
	e1.focus()
	
def grabar():

	total_result = resultado.get()
	
	#DATETIME PARA MYSQL
	fechahora = strftime("%Y-%m-%d %H:%M:%S",localtime())
	fh = str(fechahora)
	
	d0 = cc.get()
	d1 = nombre.get()
	d2 = pago.get()
	d3 = ref.get()
	
	connect.commit()
	#GUARDAR ENCABEZADO FACTURA
	sql1 = "INSERT INTO gastos (g_fecha, b_cc, g_fpago) VALUES ('%s', '%s', '%s');" % (fh, d0, d2)
	cursor.execute(sql1)
	
	#CARTURAR NUM FACTURA
	sql2 = """SELECT g_num FROM gastos WHERE g_fecha = ("%s");""" % (fh)
	cursor.execute(sql2)
	result = cursor.fetchall()
	for item in result:
		num = item[0] #NUM FACTURA
	
	children = tree.get_children()
	for child in children:
		col1 = tree.item(child, 'values')[0]#Código
		col2 = tree.item(child, 'values')[1]#
		col3 = tree.item(child, 'values')[2]#Valor
		#GUARDAR DETALLES FACTURA
		sql3 = "INSERT INTO gastos_detalles (g_num, cc_cod, gd_valor) VALUES ('%s', '%s', '%s');" % (num, col1, col3)
		cursor.execute(sql3)
	showinfo ("Mensaje", "Registro guardados! Ver recibo")
	connect.commit()
	
	#-----------------------------------------------------------------------
	
	#REPORTLAB PDF
	doc = SimpleDocTemplate("comprobantes_egreso/comprobante.pdf", pagesize = letter)
	story=[]
	
	#-------------------------------------------- CABECERA DEL DOCUMENTO
	
	#VARIABLES
	logo = Image("img/logo.gif", width=150, height=45) #Imagen del logo
	logo.hAlign ='LEFT' #Alineación de la img en la hoja
	
	info = Paragraph('''<para align=center leading=8><font size=6>CALLE 11A N°42-68 LOC,195<br/>
		TELEFONO: 3110513 FAX:2664154<br/>
		AA.75105 ED. EL DORADO<br/>
		AFILIADO A FENALCO<br/>
		M.A.V.U N°000078</font></para>''', styleSheet["BodyText"])
		
	tipoDoc = Paragraph ('''<para align=right><b>COMPROBANTE DE EGRESO<br/>N° %s</b></para>'''%num, styleSheet["BodyText"])
	
	#-----------------------------------------------------------------------
	
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
	sra = Paragraph ('''<font size=6><br/></font><font>Señor(a): </font>%s'''%d1, styleSheet["BodyText"])
	docID = Paragraph ('''<font>C.C.: </font>	%s''' %d0, styleSheet["BodyText"])
	pagoCon = Paragraph ('''<font>Pago Con: </font>%s'''%d2, styleSheet["BodyText"])
	referencia = Paragraph ('''<font>Referencia Pago: </font>%s'''%d3, styleSheet["BodyText"])
	fechaFormato = Paragraph ('''<para align=center fontSize=6>Día Mes Año</para>''', styleSheet["BodyText"])
	hoy = time.strftime("%d/%m/%Y")
	fecha = Paragraph ('''<para align=center spaceBefore=0>%s</para>''' %hoy, styleSheet["BodyText"])
	
	#-----------------------------------------------------------------------
	
	#TABLA
	datos = [[sra,'','','','',[fechaFormato,fecha]],
			 [docID,'','','','',''],
			 [pagoCon,'',referencia,'','','']]
			 
	tabla2 = Table(datos, style=[
						 ('VALIGN', (0,0),(2,0),'TOP'),
						 ('SPAN',(0,0),(3,0)),#Combinar 3 filas (col0,row0) hasta (col2,row0) Nombre #0
						 ('SPAN',(0,1),(2,1)),#Combinar 3 filas CC #1
						 ('SPAN',(0,2),(1,2)),#Combinar 2 filas Pago Con
						 ('SPAN',(2,2),(4,2)),#Combinar 2 filas Referencia Pago
						 ('GRID',(5,0),(5,0),0.5,colors.black)#Marco Fecha
						 ],colWidths=80, rowHeights=None)
						 
	#Constructor y espaciado
	story.append(Spacer(0,15)) #Espacio del salto de línea con el siguiente Ejemplo
	story.append(tabla2) #Construye la tabla 't' definida anteriormente
	
	#-------------------------------------------- ENCABEZADO DETALLES DEL DOCUMENTO
	
	#VARIABLES
	codigo = Paragraph('''<para align=center><b>CODIGO</b></para>''', styleSheet["BodyText"])
	concepto = Paragraph('''<para align=center><b>CONCEPTO</b></para>''', styleSheet["BodyText"])
	valores = Paragraph('''<para align=center><b>VALOR</b></para>''', styleSheet["BodyText"])
	
	#-----------------------------------------------------------------------
	
	#TABLA ENCABEZADO DETALLE
	data=[[codigo, concepto, valores]] #0
		  
	#FORMATO TABLA ENCABEZADO DETALLE
	tabla3=Table(data,
		style=[
			('GRID',(0,0),(2,0),0.5,colors.grey),#Color regilla de DESCRIPCION & VALOR
			('BOX',(2,1),(2,9),0.5,colors.grey), #Color & grosor de la tabla o marco externo de los VALORES
			('BACKGROUND',(0,0),(2,0), colors.pink) #Color de fondo de DESCRIPCION & VALOR #0
			], colWidths=[110,250,115], rowHeights=None)
			
	#Constructor y espaciado
	story.append(Spacer(0,15)) #Espacio del salto de línea con el siguiente Ejemplo
	story.append(tabla3) #Construye la tabla 't' definida anteriormente
	
	#-------------------------------------------- DETALLES DEL DOCUMENTO
	
	children = tree.get_children()
	for child in children:
		col1 = tree.item(child, 'values')[0]#Código
		col2 = tree.item(child, 'values')[1]#
		col3 = tree.item(child, 'values')[2]#Valor
		
		#Formato de la tabla
		contenido = [[col1, col2, col3]]
		
		tabla4 = Table(contenido, colWidths=[110,250,115], rowHeights=None)
		
		tabla4.setStyle([
						('BACKGROUND',(0,0),(2,0), colors.lavender)
						#('ALIGN', (2,0), (2,0), 'RIGHT'),#Centrar valores #0)
						])
						
		#Constructor y espaciado
		story.append(Spacer(0,15)) #Espacio del salto de línea con el siguiente Ejemplo
		story.append(tabla4) #Construye la tabla 't' definida anteriormente
	
	#-------------------------------------------- TOTALES DEL DOCUMENTO
	
	totales= [['', 'TOTAL PAGADO', total_result]]
	tabla5 = Table(totales,
			style=[
				  ('GRID',(1,0),(2,0),0.5,colors.grey),#Color regilla de SUBTOTAL, IVA, TOTAL
				  ('BACKGROUND',(2,0),(2,0),colors.black),#Color de fondo de TOTAL
				  ('TEXTCOLOR',(2,0),(2,0),colors.white), #Color de letra de TOTAL
				  ('BACKGROUND',(2,0),(2,0),colors.grey)#Color de fondo de VALOR TOTAL
				  ], colWidths=[210,150,115], rowHeights=None)
	story.append(Spacer(0,15)) #Espacio del salto de línea con el siguiente Ejemplo
	story.append(tabla5) #Construye la tabla 't' definida anteriormente
	
	"""
	children = tree.get_children()
	for child in children:
		col1 = tree.item(child, 'values')[0]#Código
		col2 = tree.item(child, 'values')[1]#
		col3 = tree.item(child, 'values')[2]#Valor
	
	#TABLA DETALLES (OTRA FORMA)
	data=[[codigo, concepto, valores], #0
		  [col1, col2, col3],	#1
		  ['', '', ''],	#2
		  ['', '', ''],	#3
		  ['', '', ''],	#4
		  ['', '', ''],	#5
		  ['', '', ''],	#6
		  ['', '', ''], #7
		  ['', '', ''], #8
		  ['', 'TOTAL PAGADO', total_result]] #9
		  
	#Formato de la tabla
	tabla5=Table(data,
		style=[
			('GRID',(0,0),(2,0),0.5,colors.grey),#Color regilla de DESCRIPCION & VALOR
			('BOX',(2,1),(2,9),0.5,colors.grey), #Color & grosor de la tabla o marco externo de los VALORES
			('BACKGROUND',(0,0),(2,0), colors.pink), #Color de fondo de DESCRIPCION & VALOR #0
			#('SPAN',(0,0),(1,0)), #Combinar filas DESCRIPCION #0
			('BOX',(0,1),(2,6),0.5,colors.grey), #Color & grosor de la tabla o marco externo de los DETALLES
			('ALIGN', (2,1), (2,1), 'CENTER'),#Centrar #1
			#('SPAN',(0,1),(1,1)), #Combinar filas de Detalle #1
			('SPAN',(0,2),(0,8)), #Combinar filas de Detalle #2
			('SPAN',(1,2),(1,8)), #Combinar filas de Detalle #3
			('SPAN',(2,2),(2,8)), #Combinar filas de Detalle #4
			#('SPAN',(0,5),(1,5)), #Combinar filas de Detalle #5
			#('SPAN',(0,6),(1,6)), #Combinar filas de Detalle #6
			('GRID',(1,7),(2,8),0.5,colors.grey),#Color regilla de SUBTOTAL, IVA, TOTAL
			('BACKGROUND',(1,9),(1,9),colors.black),#Color de fondo de TOTAL
			('TEXTCOLOR',(1,9),(1,9),colors.white), #Color de letra de TOTAL
			('BACKGROUND',(2,9),(2,9),colors.grey)#Color de fondo de VALOR TOTAL
			])
			
	#Constructor y espaciado
	story.append(Spacer(0,15)) #Espacio del salto de línea con el siguiente Ejemplo
	story.append(tabla5) #Construye la tabla 't' definida anteriormente
	"""
	
	#-------------------------------------------- FIN PDF
	
	doc.build(story) #Constructor del documento
	if sys.platform == 'linux2':
		os.system("xdg-open ~/SBIENES/comprobantes_egreso/comprobante.pdf")
	elif sys.platform == 'linux2':
		os.system("/usr/bin/gnome-open comprobantes_egreso/comprobante.pdf")
	else:
		os.startfile("D:/SBIENES/comprobantes_egreso/comprobante.pdf")

	limpiar()
	cargar_lista()
	
def cargar_lista():
	try:
		connect.commit()
		display = "select g_num from gastos order by g_num;"
		cursor.execute(display)
		registros = cursor.fetchall()
		lb.delete(0, END)
		for item in registros:
			#print item
			num = item[0]
			lb.insert(END, num)
	except:
		showerror("Mensaje", "Ha ocurrido un error")
