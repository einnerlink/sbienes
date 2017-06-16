#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from ttk import Combobox, Treeview
from tkMessageBox import*
import MySQLdb
from controller import *

class Admindocs(Frame):
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)
		
		global info, tree
		
		#VARIABLES
		info = IntVar()
		
		#WIDGETS
		
		#========================= HEADER ===========================
		
		self.header = Label(self, text="ADMINISTRADOR DE DOCUMENTOS", font="bold")
		self.header.pack(pady=20, side=TOP)
		
		#========================= WRAPPER 1 ===========================
		
		self.wrapper = Frame (self)
		self.wrapper.pack(side=LEFT, fill=Y)

		#======================== DOCUMENTOS DE ========================
		
		self.f0 = Frame(self.wrapper)
		self.f0.pack(pady=5,fill=X)#------------------------------------

		self.lf1 = LabelFrame(self.f0, text="Documentos de")#---------->

		self.f1 = Frame(self.lf1)
		self.f1.pack(pady=5, side=LEFT)
		
		self.pR1 = Radiobutton(self.f1, text="Propietario", variable=info, value=1, command=select)
		self.pR1.grid(row=0, column=0, sticky=W)
		self.aR2 = Radiobutton (self.f1, text="Arrendatario", variable=info, value=2, command=select)
		self.aR2.grid(row=1, column=0, sticky=W)
		self.tR3 = Radiobutton (self.f1, text="Tercero", variable=info, value=3, command=select)
		self.tR3.grid(row=2, column=0, sticky=W)
		
		self.lf1.pack(side=LEFT)#<--------------------------------------
		
		#====================== FECHAS DE BÚSQUEDA =====================
		
		self.lf2 = LabelFrame(self.f0, text="Fechas de búsqueda")#------>

		self.f2 = Frame(self.lf2)
		self.f2.pack(pady=5)#---------------------------
		
		self.deL = Label(self.f2, text='De:')
		self.deL.pack(side=LEFT)
		
		self.deCbx = Combobox(self.f2, width=32)
		self.deCbx.set('')
		self.deCbx.pack(side=LEFT)
		
		self.f3 = Frame(self.lf2)
		self.f3.pack(pady=5)#---------------------------
		
		self.hastaL = Label(self.f3, text='Hasta:')
		self.hastaL.pack(side=LEFT)
		
		self.hastaCbx = Combobox(self.f3, width=30)
		self.hastaCbx.set('')
		self.hastaCbx.pack(side=LEFT)

		self.lf2.pack(side=LEFT, fill=X)#<---------------------------

		#========================= WRAPPER 2 ===========================
		
		self.wrapper2 = Frame (self.wrapper)
		self.wrapper2.pack(pady=5,fill=X)
		
		#========================= BENEFICIARIO ========================
		
		self.box1 = Frame(self.wrapper2)
		self.box1.pack(side=LEFT)
		
		#---------------------------------------------------------------
		
		self.f4 = Frame(self.box1)
		self.f4.pack()
		
		self.l1 = Label(self.f4, text="Beneficiario")
		self.l1.pack()

		tree = Treeview(self.f4, height=7, show="headings", columns=('col1','col2'))
		tree.pack(side=LEFT, fill=X, expand=1)
		tree.column('col1', width=100, anchor='center')
		tree.column('col2', width=180, anchor='center')
		
		tree.heading('col1', text='CC')
		tree.heading('col2', text='Nombres')
		
		self.scroll = Scrollbar(self.f4,orient=VERTICAL,command=tree.yview)
		tree.configure(yscrollcommand=self.scroll.set)

		self.f5 = Frame(self.box1)#----------------------------------
		self.f5.pack()
		
		self.lf3 = LabelFrame(self.f5, text="Factura Propietario")#---->
		
		self.e1 = Entry(self.lf3, width=12).pack(side=LEFT)
		self.anularCk = Checkbutton(self.lf3, text="Anular").pack(side=LEFT)
		self.viewB = Button(self.lf3, text='Visualizar').pack(side=LEFT)
		
		self.lf3.pack(side=LEFT)#<--------------------------------------
		
		#========================== FACTURAS ==========================
		
		self.box2 = Frame(self.wrapper2)
		self.box2.pack(side=LEFT)
		
		#---------------------------------------------------------------
		
		self.f6 = Frame(self.box2)
		self.f6.pack()
		
		self.l2 = Label(self.f6, text="Facturas")
		self.l2.pack()

		self.tree = Treeview(self.f6, height=7, show="headings", columns=('col1','col2'))
		self.tree.pack(side=LEFT, fill=X, expand=1)
		self.tree.column('col1', width=100, anchor='center')
		self.tree.column('col2', width=100, anchor='center')
		
		self.tree.heading('col1', text='Número')
		self.tree.heading('col2', text='Valor')
		
		self.scroll = Scrollbar(self.f6,orient=VERTICAL,command=self.tree.yview)
		self.tree.configure(yscrollcommand=self.scroll.set)
		
		self.f7 = Frame(self.box2)#----------------------------------
		self.f7.pack()
		
		self.lf4 = LabelFrame(self.f7, text="Factura Arrendatario")#---->
		
		self.e1 = Entry(self.lf4, width=12).pack(side=LEFT)
		self.anularCk = Checkbutton(self.lf4, text="Anular").pack(side=LEFT)
		self.viewB = Button(self.lf4, text='Ver', width=5).pack(side=LEFT)
		
		self.lf4.pack(side=LEFT)#<--------------------------------------
		
		#========================== RECIBOS ==========================
		
		self.box3 = Frame(self.wrapper2)
		self.box3.pack(side=LEFT)
		
		#---------------------------------------------------------------
		
		self.f8 = Frame(self.box3)
		self.f8.pack()
		
		self.l3 = Label(self.f8, text="Recibos de caja")
		self.l3.pack()

		self.tree = Treeview(self.f8, height=7, show="headings", columns=('col1','col2'))
		self.tree.pack(side=LEFT, fill=X, expand=1)
		self.tree.column('col1', width=100, anchor='center')
		self.tree.column('col2', width=100, anchor='center')
		
		self.tree.heading('col1', text='Número')
		self.tree.heading('col2', text='Valor')
		
		self.scroll = Scrollbar(self.f8,orient=VERTICAL,command=self.tree.yview)
		self.tree.configure(yscrollcommand=self.scroll.set)
		
		self.f9 = Frame(self.box3)#----------------------------------
		self.f9.pack()
		
		self.lf5 = LabelFrame(self.f9, text="Recibos de caja")#---->
		
		self.e1 = Entry(self.lf5, width=12).pack(side=LEFT)
		self.anularCk = Checkbutton(self.lf5, text="Anular").pack(side=LEFT)
		self.viewB = Button(self.lf5, text='Ver', width=5).pack(side=LEFT)
		
		self.lf5.pack(side=LEFT)#<--------------------------------------
		
		#===================== COMPROBANTE DE PAGO =====================
		
		self.box4 = Frame(self.wrapper2)
		self.box4.pack(side=LEFT)
		
		#---------------------------------------------------------------
		
		self.f10 = Frame(self.box4)
		self.f10.pack()
		
		self.l4 = Label(self.f10, text="Comprobantes de pago")
		self.l4.pack()

		self.tree = Treeview(self.f10, height=7, show="headings", columns=('col1','col2'))
		self.tree.pack(side=LEFT, fill=X, expand=1)
		self.tree.column('col1', width=100, anchor='center')
		self.tree.column('col2', width=100, anchor='center')
		
		self.tree.heading('col1', text='Número')
		self.tree.heading('col2', text='Valor')
		
		self.scroll = Scrollbar(self.f10,orient=VERTICAL,command=self.tree.yview)
		self.tree.configure(yscrollcommand=self.scroll.set)
		
		self.f11 = Frame(self.box4)#----------------------------------
		self.f11.pack()
		
		self.lf6 = LabelFrame(self.f11, text="Pagos")#---->
		
		self.e1 = Entry(self.lf6, width=12).pack(side=LEFT)
		self.anularCk = Checkbutton(self.lf6, text="Anular").pack(side=LEFT)
		self.viewB = Button(self.lf6, text='Ver', width=5).pack(side=LEFT)
		
		self.lf6.pack(side=LEFT)#<--------------------------------------

def select():
	connect.commit()
	v = info.get()
	if v == 1:
		display = "SELECT p_cc, dueño FROM relacionip order by dueño;"
		cursor.execute(display)
		registros = cursor.fetchall()
		#tree.delete()
		tree.delete(*tree.get_children())
		for item in registros:
			tree.insert('', END, values=(item[0],item[1]))
	elif v== 2:
		show2 = "SELECT a_cc, a_nombres FROM arrendatarios order by a_nombres;"
		cursor.execute(show2)
		registros = cursor.fetchall()
		tree.delete(*tree.get_children())
		for item in registros:
			tree.insert('', END, values=(item[0],item[1]))
	elif v== 3:
		show2 = "SELECT t_cc, t_nombre FROM terceros order by t_nombre;"
		cursor.execute(show2)
		registros = cursor.fetchall()
		tree.delete(*tree.get_children())
		for item in registros:
			tree.insert('', END, values=(item[0],item[1]))
	else:
		pass
		#showerror('Mensaje', "Error al cargar los datos.")
