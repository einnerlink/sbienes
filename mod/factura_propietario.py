#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from ttk import*
import os
from tkMessageBox import*
import MySQLdb
from controller import *
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime
import time

class FacturaProp(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		global nit, nombre, inmueble, Cbx, etime1, etime2
		global fecha, hoy, year
		
		#VARIABLES
		fecha = datetime.date.today()
		hoy = "%s" %fecha.year
		fecha = StringVar()
		
		nit = StringVar()
		nombre = StringVar()
		inmueble = StringVar()
		meses = ["Enero", "Febreo", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

		#WIDGETS
		
		#=========================== HEADER ============================
		
		self.titleL = Label(self, text="FACTURA PROPIETARIO", font="bold")
		self.titleL.pack(pady=20, side=TOP)

		#======================= DATOS GENERALES =======================
		
		self.lf = LabelFrame(self, text="Datos generales")
		self.lf.pack(anchor=W,pady=5)#-------------------------

		self.f0 = Frame(self.lf)
		self.f0.pack(pady=5,fill=X)#---------------------------

		self.ccnitL = Label(self.f0, text='CC/Nit:')
		self.ccnitL.pack(side=LEFT)
		self.ccnitE = Entry(self.f0, textvariable=nit, width=30)
		self.ccnitE.pack(side=LEFT)
		
		self.b1 = Button (self.f0, text='Buscar', command=buscar)
		self.b1.pack(side=LEFT)

		self.f1 = Frame(self.lf)
		self.f1.pack(pady=5,fill=X)#---------------------------
		
		self.nombreL = Label(self.f1, text='Nombre:')
		self.nombreL.pack(side=LEFT)
		self.nombreE = Entry(self.f1, textvariable=nombre, width=50, state=DISABLED)
		self.nombreE.pack(side=LEFT,fill=X)

		self.f2 = Frame(self.lf)
		self.f2.pack(pady=5,fill=X)#---------------------------
		
		self.inmuebleL = Label(self.f2, text='Inmueble:')
		self.inmuebleL.pack(side=LEFT)
		Cbx = Entry(self.f2, textvariable=inmueble, state=DISABLED, width=48)
		Cbx.pack(side=LEFT,fill=X)
		"""
		Cbx = Combobox(self.f2, textvariable=inmuebles, values=inmueble)
		Cbx.configure(width=48)
		Cbx.pack(side=LEFT)"""

		#========================= FACTURACIÓN =========================
		
		self.lf1 = LabelFrame(self, text="Periodo a facturar")
		self.lf1.pack(anchor=W,pady=5,fill=X)#-------------------------

		self.f2 = Frame(self.lf1)
		self.f2.pack(pady=5,fill=X)#---------------------------

		self.mesiniL = Label(self.f2, text='Mes inicial:')
		self.mesiniL.pack(padx=5,side=LEFT)

		self.mesiniCbx = Combobox(self.f2, values=meses, width=10)
		self.mesiniCbx.set('')
		self.mesiniCbx.pack(side=LEFT)

		self.emptyL = Label(self.f2)###VACIO###
		self.emptyL.pack(padx=5, side=LEFT)
	
		self.yeariniL = Label(self.f2, text='Año:')
		self.yeariniL.pack(side=LEFT)
		etime1 = Entry(self.f2, textvariable=fecha, width=8)
		fecha.set(hoy)
		etime1.pack(side=LEFT)
		
		#self.yeariniE = Entry(self.f2, width=8)
		#self.yeariniE.pack(side=LEFT)

		self.mesfinL = Label(self.f2, text='Mes final:')
		self.mesfinL.pack(padx=5,side=LEFT)

		self.mesfinCbx = Combobox(self.f2, values=meses, width=10)
		self.mesfinCbx.set('')
		self.mesfinCbx.pack(side=LEFT)

		self.emptyL = Label(self.f2)###VACIO###
		self.emptyL.pack(padx=5, side=LEFT)

		self.yearfinL = Label(self.f2, text='Año:')
		self.yearfinL.pack(side=LEFT)
		etime2 = Entry(self.f2, textvariable=fecha, width=8)
		fecha.set(hoy)
		etime2.pack(side=LEFT)
		
		#self.yearfinE = Entry(self.f2, width=8)
		#self.yearfinE.pack(side=LEFT)

		self.emptyL = Label(self.f2)###VACIO###
		self.emptyL.pack(padx=5, side=LEFT)
		
		self.pdfB = Button(self.f2, text="Facturar", command=pdf)
		self.pdfB.pack(side=LEFT)

		#========================== TREEVIEW ===========================
		
		self.f3 = Frame(self)
		self.f3.pack(pady=5,fill=X)#------------------------------------
		
		self.tree = Treeview(self.f3, height=4, show="headings", columns=('col1','col2','col3'))
		self.tree.pack(side=LEFT, fill=X, expand=1)
		self.tree.column('col1', width=20, anchor='center')
		self.tree.column('col2', width=200, anchor='center')
		self.tree.column('col3', width=10, anchor='center')
		
		self.tree.heading('col1', text='Imnueble')
		self.tree.heading('col2', text='Descripción')
		self.tree.heading('col3', text='Valor')
		
		self.scroll = Scrollbar(self.f3,orient=VERTICAL,command=self.tree.yview)
		self.tree.configure(yscrollcommand=self.scroll.set)

		self.f4 = Frame(self)
		self.f4.pack(pady=5,fill=X)#--------------------

		self.notesL = Label(self.f4, text='Observaciones:')
		self.notesL.pack(side=LEFT)

		self.f5 = Frame(self)
		self.f5.pack(pady=5,fill=X)#-------------------

		self.notesT = Text(self.f5, height=5)
		self.notesT.pack(fill=X, side=LEFT, expand=1)

		self.fBtn = Frame(self)
		self.fBtn.pack()#-------------------------------
		
def buscar():
	connect.commit()
	try:
		c = nit.get()
		search = "SELECT dueño, inmueble FROM relacionip WHERE p_cc='%s';" % (c)
		cursor.execute(search)
		dato = cursor.fetchall()
		for n, d in dato:
			nombre.set(n)
			inmueble.set(d)
	except:
		showinfo ("Mensaje", "La Cédula o Nit no figura en la base de datos!")

def pdf():
	
	v1 = nit.get()
	v2 = nombre.get()
	v3 = inmueble.get()
	
	factura = canvas.Canvas("facturas/factura_propietario.pdf", pagesize=letter)
	factura.setLineWidth(.3)

	logo = "img/logo.gif"
	info = """CALLE 11A N°42-68 LOC,195\n
			TELEFONO: 3110513 FAX:2664154\n
			AA.75105 ED. EL DORADO\n
			AFILIADO A FENALCO\n
			M.A.V.U N°000078"""
	#-------------------------------------------- CABECERA DEL DOCUMENTO
	
	factura.drawImage(logo, 30,700, width=200, height=50)
	#factura.drawCentredString(250,740,info)
	#factura.drawString(250,740,'CALLE 11A N°42-68 LOC,195')
	
	factura.drawString(450,730,"FACTURA DE VENTA")
	factura.drawString(490,710,"N°")
	
	#---------------------------------------------- CUERPO DEL DOCUMENTO
	
	factura.drawString(490,670,"Día Mes Año")
	factura.drawString(490,650,hoy)
	
	#(x, y, width, height, stroke, fill)
	factura.rect(30,600,240,90, stroke=1, fill=0)
	
	#DrawString(x, y, text)
	factura.drawString(35,670,'Nombre del Propietario:')
	#textobject.setFont("Helvetica", 8)
	factura.setFont("Helvetica", 8)
	factura.drawString(35,650,v2)
	factura.drawString(35,630,'Identificación:')
	factura.setFont("Helvetica", 8)
	factura.drawString(130,630,v1)
	
	
	factura.rect(30,560,550,30, stroke=1, fill=0)
	factura.drawString(190,570,'DESCRIPCION')
	factura.drawString(480,570,'VALOR')
	factura.line(430,590,430,410)
	factura.rect(30,410,550,150, stroke=1, fill=0)
	
	#------------------------------------------------ FIN DEL DOCUMENTO
	factura.showPage()
	factura.save()
	if sys.platform == 'linux2':
		os.system("xdg-open ~/SBIENES/facturas/factura_propietario.pdf")#DEBIAN
	elif sys.platform == 'linux2':
		os.system("/usr/bin/gnome-open ~/SBIENES/facturas/factura_propietario.pdf")#UBUNTU
	else:
		os.startfile("D:/SBIENES/facturas/factura_propietario.pdf")#WINDOWS
