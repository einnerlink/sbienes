#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from ttk import Combobox, Notebook, Treeview
from tkMessageBox import*
import MySQLdb

class ReciboCaja(Frame):
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)

		lupa = PhotoImage(file='img/lupa.png')
		
		#VARIABLES
		tcontrato = ['Vivienda', 'Comercial']
		aplica = StringVar()
		
		#WIDGETS
		
		#========================= HEADER ===========================
		
		self.header = Label(self, text="RECIBO DE CAJA", font="bold")
		self.header.pack(pady=20, side=TOP)
		
		#========================== WRAPPER ==========================
		
		self.wrapper = Frame (self)
		self.wrapper.pack(side=TOP, fill=Y)
		#self.wrapper.pack(side=LEFT, fill=Y)#Este ubica el forma a la IZA
		
		#================ NOTEBOOK =============>
		
		self.nb = Notebook(self.wrapper)
		
		#-----------------------> TAB 1
		
		self.tab1 = Frame (self.nb)
		self.tab1.pack()
		
		self.f0 = Frame(self.tab1)#-------------------------------------
		self.f0.pack(pady=5,fill=X)

		self.R1 = Radiobutton(self.f0, text="Arrendatario", variable=aplica, value='Arrendatario')
		self.R1.pack(padx=20,side=LEFT)
		self.R2 = Radiobutton (self.f0, text="Propietario", variable=aplica, value='Propietario')
		self.R2.pack(padx=20,side=LEFT)
		self.R3 = Radiobutton (self.f0, text="Tercero", variable=aplica, value='Tercero')
		self.R3.pack(padx=20,side=LEFT)
		
		self.f1 = Frame(self.tab1)#-------------------------------------
		self.f1.pack(pady=5,fill=X)
		
		self.cc = Label(self.f1, text='CC/Nit: ')
		self.cc.pack(side=LEFT)
		self.ccE = Entry(self.f1)
		self.ccE.pack(side=LEFT)
		
		self.b1 = Button(self.f1, text='Buscar', image=lupa)
		self.b1.image=lupa
		self.b1.pack(side=LEFT)

		self.f2 = Frame(self.tab1)
		self.f2.pack(pady=5,fill=X)#------------------------------------
		
		self.nombre = Label(self.f2, text='Nombre:')
		self.nombre.pack(side=LEFT)
		self.nombrE = Entry(self.f2, width=5, state=DISABLED)
		self.nombrE.pack(side=LEFT, fill=X, expand=1)
		
		self.f3 = Frame(self.tab1)
		self.f3.pack(pady=5,fill=X)#------------------------------------
		
		self.inmueble = Label(self.f3, text='Inmueble:')
		self.inmueble.pack(side=LEFT)
		
		self.inmuebleCbx = Combobox(self.f3, values=NONE, width=10)
		self.inmuebleCbx.set('')
		self.inmuebleCbx.pack(side=LEFT, fill=X, expand=1)
		
		self.b2 = Button(self.f3, text='Agregar', image=lupa)
		self.b2.image=lupa
		self.b2.pack(side=LEFT)
		
		self.f4 = Frame(self.tab1)
		self.f4.pack(pady=5,fill=X)#------------------------------------
		
		self.fpago = Label(self.f4, text='Forma de Pago:')
		self.fpago.pack(side=LEFT)
		
		self.fpagoCbx = Combobox(self.f4, values=NONE, width=10)
		self.fpagoCbx.set('')
		self.fpagoCbx.pack(side=LEFT)
		
		self.b3 = Button(self.f4, text='Crear novedad', state=DISABLED)
		self.b3.pack(side=LEFT)

		#========================== TREEVIEW ===========================
		
		self.f5 = Frame(self.tab1)
		self.f5.pack(pady=5,fill=X)#------------------------------------
		
		self.tree = Treeview(self.f5, height=4, show="headings", columns=('col1','col2','col3'))
		self.tree.pack(side=LEFT, fill=X, expand=1)
		self.tree.column('col1', width=20, anchor='center')
		self.tree.column('col2', width=200, anchor='center')
		self.tree.column('col3', width=10, anchor='center')
		
		self.tree.heading('col1', text='CC')
		self.tree.heading('col2', text='Descripción')
		self.tree.heading('col3', text='Valor')
		
		self.scroll = Scrollbar(self.f3,orient=VERTICAL,command=self.tree.yview)
		self.tree.configure(yscrollcommand=self.scroll.set)

		self.f6 = Frame(self.tab1)
		self.f6.pack(pady=5,fill=X)#--------------------

		self.notesL = Label(self.f6, text='Observaciones:')
		self.notesL.pack(side=LEFT)

		self.f7 = Frame(self.tab1)
		self.f7.pack(pady=5,fill=X)#-------------------

		self.notesT = Text(self.f7, height=5)
		self.notesT.pack(fill=X, side=LEFT, expand=1)
		
		#-----------------------> TAB 2
		
		self.tab2 = Frame (self.nb)
		self.tab2.pack()
		
		#-----------------------> TAB 3
		
		self.tab3 = Frame (self.nb)
		self.tab3.pack()
	
		#---------------------------------------------------------------
		
		self.nb.add (self.tab1, text="Datos Generales")
		self.nb.add(self.tab2, text="Referencia de Pago", state=DISABLED)
		self.nb.add(self.tab3, text="Referencias Bancarias", state=DISABLED)
		
		self.nb.pack()
		
		#---------------------------------------------------------------
		
		self.fBtn = Frame(self.wrapper)
		self.fBtn.pack()#-------------------------------
	
		self.queryB = Button(self.fBtn, text='Consultar')
		self.queryB.pack(side=RIGHT)
		self.deleteB = Button(self.fBtn, text='Borrar')
		self.deleteB.pack(side=RIGHT)
		self.updateB = Button(self.fBtn, text='Actualizar')
		self.updateB.pack(side=RIGHT)
		self.addB = Button(self.fBtn, text='Agregar')
		self.addB.pack(side=RIGHT)
		
		#========================= ASIDE ===========================
		"""
		self.aside = Frame(self)
		self.aside.pack(side=TOP, fill=BOTH)
		
		self.viewer = Label(self.aside, text="LISTA DE CONTRATOS")
		self.viewer.pack()

		scroll = Scrollbar(self.aside, orient=VERTICAL)
		list = Listbox(self.aside, yscrollcommand=scroll.set, height=20, width=20)
		scroll.config (command=list.yview)
		
		scroll.pack(side=RIGHT, fill=Y)
		list.pack(fill=Y, expand=1)
		
		self.updateBP = Button(self.aside, text='Actualizar')
		self.updateBP.pack()"""
