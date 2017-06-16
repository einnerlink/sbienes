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

try:
	connect.commit()
	search1 = "SELECT ivajuridico, resolucion FROM configuracion;"
	cursor.execute(search1)
	dato1 = cursor.fetchall()
	for conf in dato1:
		ivajuridico = conf[0]
		resolucion = conf[1]
except:
	pass
	

class FacturaInquilino(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		global e0, e1, e2, e3, e4, e5, e6, e7, e8, CbxVlr, observaciones, scroll, tree, pdfB, add
		global cc, arrend, inmueble, codigo, tel, valor
		global Cbx, meses, mes1, mes2, tiempo, fechapago, anio, mes
		global prop, nit, tp, subtotal, iva, total
				
		#VARIABLES
		tiempo = datetime.date.today()
		anio = time.strftime("%Y")
		mes = time.strftime("%B")
		fechapago = StringVar()
		
		cc = StringVar()
		arrend = StringVar()
		
		inmueble = StringVar()
		codigo = StringVar()
		tel = StringVar()
		valor = DoubleVar()
		
		prop = StringVar()
		nit = StringVar()
		tp = StringVar()
		
		subtotal = DoubleVar()
		iva = DoubleVar()
		total = DoubleVar()
		
		mes1 = StringVar()
		mes2 = StringVar()
		meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

		#WIDGETS
		
		#=========================== HEADER ============================
		
		self.titleL = Label(self, text="FACTURA INQUILINO", font="bold")
		self.titleL.pack(pady=20, side=TOP)
		
		#========================= WRAPPER 1 ===========================
		
		wrapper = Frame (self)
		wrapper.pack(fill='both')

		#======================= DATOS GENERALES =======================
		
		self.lf = LabelFrame(wrapper, text="Datos generales")
		self.lf.pack(side=LEFT)#-------------------------------

		self.f0 = Frame(self.lf)
		self.f0.pack(pady=5,fill=X)#---------------------------

		self.ccnitL = Label(self.f0, text='CC/Nit:')
		self.ccnitL.pack(side=LEFT)
		e0 = Entry(self.f0, textvariable=cc, width=30)
		e0.pack(side=LEFT)
		
		self.b1 = Button (self.f0, text='Buscar', command=buscar)
		self.b1.pack(side=LEFT)

		self.f1 = Frame(self.lf)
		self.f1.pack(pady=5,fill=X)#---------------------------
		
		self.nombreL = Label(self.f1, text='Nombre:')
		self.nombreL.pack(side=LEFT)
		e1 = Entry(self.f1, textvariable=arrend, width=50, state=DISABLED)
		e1.pack(side=LEFT,fill=X)

		self.f2 = Frame(self.lf)
		self.f2.pack(pady=5,fill=X)#---------------------------
		
		self.inmuebleL = Label(self.f2, text='Inmueble:')
		self.inmuebleL.pack(side=LEFT)
		e2 = Entry(self.f2, textvariable=inmueble, state=DISABLED, width=48)
		e2.pack(side=LEFT,fill=X)
		
		self.f3 = Frame(self.lf)
		self.f3.pack(pady=5,fill=X)#---------------------------
		
		self.inmuebleL = Label(self.f3, text='Código: ')
		self.inmuebleL.pack(side=LEFT)
		e3 = Entry(self.f3, textvariable=codigo, state=DISABLED, width=5)
		e3.pack(side=LEFT,fill=X)
		
		self.tel = Label(self.f3, text='Teléfono: ')
		self.tel.pack(side=LEFT)
		e4 = Entry(self.f3, textvariable=tel, state=DISABLED, width=15)
		e4.pack(side=LEFT,fill=X)
		
		self.precio = Label(self.f3, text='Arriendo $: ')
		self.precio.pack(side=LEFT)
		e5 = Entry(self.f3, textvariable=valor, state=DISABLED, width=15)
		e5.pack(side=LEFT,fill=X)
		
		#======================= DATOS PROPIETARIO =======================
		
		wrap = Frame(wrapper)
		wrap.pack(side=RIGHT)
		
		lf = LabelFrame(wrap, text="Propietario")
		lf.pack()#-------------------------
		#lf.pack_forget()#-------------------------
		
		f0 = Frame(lf)
		f0.pack(pady=5,fill=X)#---------------------------
		
		nombreL = Label(f0, text='Nombre: ')
		nombreL.pack(side=LEFT)
		e6 = Entry(f0, textvariable=prop, width=48, state=DISABLED)
		e6.pack(side=LEFT,fill=X)
		
		f1 = Frame(lf)
		f1.pack(pady=5,fill=X)#---------------------------

		ccnitL = Label(f1, text='CC/Nit: ')
		ccnitL.pack(side=LEFT)
		e7 = Entry(f1, textvariable=nit, state=DISABLED, width=48)
		e7.pack(side=LEFT)
		
		f2 = Frame(wrap)
		f2.pack(pady=5,fill=X)#---------------------------
		
		self.lb = Label(f2, text=None)
		self.lb.pack(side=LEFT)
		
		f3 = Frame(wrap)
		f3.pack(pady=5,fill=X)#---------------------------
		
		"""
		self.inmuebleL = Label(f2, text='Tipo Persona: ')
		self.inmuebleL.pack(side=LEFT)
		e8 = Entry(f2, textvariable=tp, state=DISABLED, width=40)
		e8.pack(side=LEFT,fill=X)
		"""
		
		l = Label(f3, text='SubTotal ')
		l.pack(side=LEFT)
		e8 = Entry(f3, textvariable=subtotal, state=DISABLED, width=12)
		e8.pack(side=LEFT,fill=X)
		
		l = Label(f3, text='IVA ')
		l.pack(side=LEFT)
		e9 = Entry(f3, textvariable=iva, state=DISABLED, width=12)
		e9.pack(side=LEFT,fill=X)
		
		l = Label(f3, text='Total ')
		l.pack(side=LEFT)
		e10 = Entry(f3, textvariable=total, state=DISABLED, width=12)
		e10.pack(side=LEFT,fill=X)
		
		f4 = Frame(wrap)
		f4.pack(pady=5,fill=X)#---------------------------
		
		#========================= FACTURACIÓN =========================
		
		self.lf1 = LabelFrame(self, text="Periodo a facturar")
		self.lf1.pack(anchor=W,pady=5,fill=X)#-------------------------

		self.f2 = Frame(self.lf1)
		self.f2.pack(pady=5,fill=X)#---------------------------

		self.mesiniL = Label(self.f2, text='Mes inicial:')
		self.mesiniL.pack(padx=5,side=LEFT)

		CbxVlr = Combobox(self.f2, textvariable=mes1, values=meses, width=10, state=DISABLED)
		CbxVlr.set(mes)
		CbxVlr.pack(side=LEFT)

		self.emptyL = Label(self.f2)###VACIO###
		self.emptyL.pack(padx=5, side=LEFT)
	
		self.yeariniL = Label(self.f2, text='Año:')
		self.yeariniL.pack(side=LEFT)
		self.yeariniE = Entry(self.f2, textvariable=fechapago, width=8, state=DISABLED)
		fechapago.set(anio)
		self.yeariniE.pack(side=LEFT)

		self.mesfinL = Label(self.f2, text='Mes final:')
		self.mesfinL.pack(padx=5,side=LEFT)

		self.mesfinCbx = Combobox(self.f2, textvariable=mes2, values=meses, width=10)
		self.mesfinCbx.set(mes)
		self.mesfinCbx.pack(side=LEFT)

		self.emptyL = Label(self.f2)###VACIO###
		self.emptyL.pack(padx=5, side=LEFT)

		self.yearfinL = Label(self.f2, text='Año:')
		self.yearfinL.pack(side=LEFT)
		self.yearfinE = Entry(self.f2, textvariable=fechapago, width=8)
		fechapago.set(anio)
		self.yearfinE.pack(side=LEFT)

		self.emptyL = Label(self.f2)###VACIO###
		self.emptyL.pack(padx=5, side=LEFT)
		
		pdfB = Button(self.f2, text="Facturar", command=agregar, state=DISABLED)
		pdfB.pack(side=LEFT)

		#========================== TREEVIEW ===========================
		
		self.f3 = Frame(self)
		self.f3.pack(pady=5,fill=X)#------------------------------------
		
		tree = Treeview(self.f3, height=4, show="headings", columns=('col1','col2'))
		tree.pack(side=LEFT, fill=X, expand=1)
		
		tree.column('col1', width=250, anchor='center')
		tree.column('col2', width=5, anchor='center')
		
		tree.heading('col1', text='Descripción')
		tree.heading('col2', text='Valor')
		
		scroll = Scrollbar(self.f3,orient=VERTICAL,command=tree.yview)
		tree.configure(yscrollcommand=scroll.set)
		tree.bind("<Delete>", borrar)
		
		#======================== OBSERVACIONES ========================

		self.f4 = Frame(self)
		self.f4.pack(pady=5,fill=X)#--------------------

		self.notesL = Label(self.f4, text='Observaciones:')
		self.notesL.pack(side=LEFT)

		self.f5 = Frame(self)
		self.f5.pack(pady=5,fill=X)#-------------------

		observaciones = Text(self.f5, height=5)
		observaciones.pack(fill=X, side=LEFT, expand=1)
		
		#=========================== BOTONES ===========================
		
		footer = Frame(self)
		footer.pack()#-------------------------------
		
		clean = Button(footer, text='Cancelar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=cancelar)
		clean.pack(side=RIGHT)
		
		add = Button(footer, text='Grabar', bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=grabar, state=DISABLED)
		add.pack(side=RIGHT)

def buscar():

	doCC = cc.get()
	if doCC == None:
		showerror("Error", "El campo está vacío")
	else:
		pdfB.configure(state="normal")#HABILITA BOTÓN GENERAR PDF
		#pdfB.configure(state="disabled")#BLOQUEA BOTÓN GENERAR PDF
	connect.commit()
	search2 = "SELECT inquilino, inmueble, i_tel, dueño, relacionip.p_cc, relacionip.i_cod, i_vlrenta, a_tpersona FROM contratos INNER JOIN relacionip ON contratos.r_id = relacionip.r_id INNER JOIN inmuebles ON relacionip.i_cod = inmuebles.i_cod INNER JOIN arrendatarios ON contratos.a_cc = arrendatarios.a_cc WHERE contratos.a_cc='%s';" % (doCC)
	cursor.execute(search2)
	dato2 = cursor.fetchall()
	for a, b, c, d, e, f, g, h in dato2:
		arrend.set(a)
		inmueble.set(b)
		tel.set(c)
		prop.set(d)
		nit.set(e)
		codigo.set(f)
		valor.set(g)
		subtotal.set(g)
		if h == 2:
			iva.set(g*ivajuridico/100)
		else:
			tp.set(0)
		total.set(subtotal.get()+iva.get())
		#showerror ("Error", "La Cédula o Nit no figura en la base de datos!")

def agregar():
	valorRenta = valor.get()
	desc = "Valor Arrendamiento Mes: %s/%s" % (mes1.get(),fechapago.get())
	tree.insert('', 0, values=(desc,valorRenta))
	add.configure(state="normal")
	
def borrar(event):
	i = tree.selection()[0]
	tree.delete(i)
	
def grabar():
	
	d0 = cc.get()
	d1 = arrend.get()
	d2 = inmueble.get()
	d3 = codigo.get()
	d4 = tel.get()
	d5 = iva.get()
	vlrenta = valor.get()
	d6 = prop.get()
	d7 = nit.get()
	d8 = mes1.get()
	d9 = fechapago.get()
	d10 = total.get()
	comentario = observaciones.get("1.0",END)
	
	#DATETIME PARA MYSQL
	fechahora = strftime("%Y-%m-%d %H:%M:%S",localtime())
	fh = str(fechahora)
	
	for conf in dato1:
		resolucion = conf[1]
	
	connect.commit()
	sql0 = "SELECT c_cod FROM contratos WHERE a_cc=%s;" % (d0)
	cursor.execute(sql0)
	result = cursor.fetchall()
	for r in result:
		contrat = r[0]
	
	sql1 = "INSERT INTO factura_arre (c_cod, fa_fecha, fa_iva, fa_total) VALUES ('%d', '%s', '%f', '%f');" % (contrat, fh, d5, d10)
	cursor.execute(sql1)
	
	
	#CARTURAR NUM FACTURA
	sql2 = """SELECT fa_num FROM factura_arre WHERE fa_fecha=("%s");""" % (fh)
	cursor.execute(sql2)
	res = cursor.fetchall()
	for item in res:
		num = item[0] #NUM FACTURA
		
	children = tree.get_children()
	for child in children:
		col1 = tree.item(child, 'values')[0]#Descripcion
		col2 = tree.item(child, 'values')[1]#Valor
		#GUARDAR DETALLES FACTURA
		sql3 = "INSERT INTO fa_detalles (fa_num, fad_desc, fad_valor) VALUES ('%s', '%s', '%s');" % (num, col1, col2)
		cursor.execute(sql3)
	connect.commit()
	showinfo ("Mensaje", "Registro guardados! Ver recibo")
	
	doc = SimpleDocTemplate("facturas/factura_inquilino.pdf", pagesize = letter,
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
	docID = Paragraph ('''<font size=6><b>CC/Nit: </b></font>	%s''' %d0, styleSheet["BodyText"])
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
			 
	tabla2 = Table(datos, style=[('BOX',(0,0),(2,2),0.5,colors.black),
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
	concepto = Paragraph('''Valor Arrendamiento Mes: %s/%s''' % (d8,d9), styleSheet["BodyText"])
	
	resol = "Resolucion Dian N°110000658514 de Diciembre de 2015 Consectivo Facturacion 33001 al 36000. P"
	
	#TABLA
	data=[[desc, '', vlr], 		#0
		  [concepto, '', vlrenta], #1
		  ['', '', ''],			#2
		  ['', '', ''],			#3
		  ['', '', ''],			#4
		  ['', '', ''],			#5
		  ['', '', ''],			#6
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
		os.system("xdg-open ~/SBIENES/facturas/factura_inquilino.pdf")#DEBIAN
	elif sys.platform == 'linux2':
		os.system("/usr/bin/gnome-open facturas/factura_inquilino.pdf")#UBUNTU
	else:
		os.startfile("D:/SBIENES/facturas/factura_inquilino.pdf")#WINDOWS
	
# NUEVO / CANCELAR
def cancelar():
	tree.delete(*tree.get_children())
	cc.set("")
	arrend.set("")
	inmueble.set("")
	codigo.set("")
	tel.set("")
	valor.set(0)
	prop.set("")
	nit.set("")
	tp.set("")
	subtotal.set(0.0)
	iva.set(0.0)
	total.set(0.0)
	#mes1.set("")
	#mes2.set("")
	observaciones.delete('1.0', END)
	pdfB.configure(state="disabled")#BLOQUEA BOTÓN GENERAR PDF
	tree.delete(*tree.get_children())
