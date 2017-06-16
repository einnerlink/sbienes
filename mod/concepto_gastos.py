#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from ttk import Combobox, Treeview
from tkMessageBox import*
import MySQLdb
from controller import *

class ConceptoGastos(Frame):
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)

		global codigo, ctacontable, nombre, desc, tree
		
		lupa = PhotoImage(file='img/lupa.png')
		
		codigo = StringVar()
		ctacontable = StringVar()
		nombre = StringVar()
		desc = StringVar()
		
		#WIDGETS
		
		#=========================== HEADER ============================
		
		self.titleL = Label(self, text="CONCEPTO DE GASTOS", font="bold")
		self.titleL.pack(pady=20, side=TOP)
		
		#=========================== WRAPPER ===========================
		
		self.wrapper = Frame (self)
		self.wrapper.pack(side=TOP, fill=Y)
		
		self.f0 = Frame(self.wrapper)
		self.f0.pack(pady=5, fill=X)#-----------------------------------
		
		l1 = Label (self.f0, text="Código:")
		l1.pack(side=LEFT)
		e1 = Entry (self.f0, textvariable=codigo, width=60)
		e1.pack(side=LEFT)
		e1.bind("<KeyRelease>", caps)
		
		self.f2 = Frame(self.wrapper)
		self.f2.pack(pady=5, fill=X)#-----------------------------------
		
		l2 = Label (self.f2, text="Cuenta Contable: ")
		l2.pack(side=LEFT)
		
		e2 = Entry (self.f2, textvariable=ctacontable, width=60)
		e2.pack(side=LEFT, fill=X, expand=1)
		
		b0 = Button (self.f2, text="Buscar", image=lupa, command=buscar)
		b0.image=lupa
		b0.pack(side=LEFT)
		
		self.f3 = Frame(self.wrapper)
		self.f3.pack(pady=5, fill=X)#-----------------------------------
		
		self.nombre = Label (self.f3, text="Nombre: ")
		self.nombre.pack(side=LEFT)
		self.nombreE = Entry (self.f3, textvariable=nombre, state=DISABLED)
		self.nombreE.pack(side=LEFT, fill=X, expand=1)
		
		self.f4 = Frame(self.wrapper)
		self.f4.pack(pady=5, fill=X)#-----------------------------------
		
		self.descL = Label (self.f4, text="Descripción: ")
		self.descL.pack(side=LEFT)
		self.descE = Entry (self.f4, textvariable=desc)
		self.descE.pack(side=LEFT, fill=X, expand=1)
		self.descE.bind("<KeyRelease>", caps)
		
		self.f5 = Frame(self.wrapper)
		self.f5.pack(pady=5, fill=X)#-----------------------------------
		
		b1 = Button (self.f5, text="Cargar", bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=cargar)
		b1.pack(side=RIGHT)
		
		b2 = Button (self.f5, text="Agregar", bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=agregar)
		b2.pack(side=RIGHT)
		
		self.f6 = Frame(self.wrapper)
		self.f6.pack(pady=5, fill=X)#-----------------------------------
		
		tree = Treeview(self.f6, show="headings", columns=('col1','col2', 'col3', 'col4'))
		tree.pack(side=LEFT, fill=X, expand=1)
		tree.column('col1', width=2, anchor='center')
		tree.column('col2', width=150, anchor='center')
		tree.column('col3', width=10, anchor='center')
		tree.column('col4', width=150, anchor='center')
		
		tree.heading('col1', text='Código')
		tree.heading('col2', text='Descripción')
		tree.heading('col3', text='Cta Contable')
		tree.heading('col4', text='Nombre')
		
		self.scroll = Scrollbar(self.f6,orient=VERTICAL,command=tree.yview)
		tree.configure(yscrollcommand=self.scroll.set)
		
		self.f7 = Frame(self.wrapper)
		self.f7.pack(pady=5, fill=X)#-----------------------------------
		
		self.delete = Button (self.f7, text="Eliminar", bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=borrar)
		self.delete.pack(side=RIGHT)
		
def caps(event):
	codigo.set(codigo.get().upper())
	desc.set(desc.get().upper())
	
def buscar():
	try:
		sql = "SELECT cc_desc FROM cuentas_contables WHERE cc_cod='%s'" % (ctacontable.get())
		cursor.execute(sql)
		connect.commit()
		dato = cursor.fetchone()
		for n in dato:
			nombre.set(n)
	except:
		showerror("Error", "No existe ese código.")
	
def agregar():
	try:
		connect.commit
		add = "INSERT INTO concepto_gastos(cg_cod, cc_cod, cg_nombre, cg_desc)VALUES('%s', '%s', '%s', '%s'); " % (codigo.get(), ctacontable.get(), nombre.get(), desc.get())
		cursor.execute(add)
		showinfo ("Mensaje", "Cuenta contable guardada!")
		codigo.set("")
		ctacontable.set("")
		nombre.set("")
		desc.set("")
		cargar()
	except MySQLdb.IntegrityError:
		showerror ("Mensaje", "Error al guardar la cuenta!")

def cargar():
	try:
		connect.commit()
		tv = "SELECT cg_cod, cg_desc, cc_cod, cg_nombre FROM concepto_gastos"
		#tv = "SELECT cc_cod, cc_desc FROM cuentas_contables order by cc_desc;"
		cursor.execute(tv)
		results = cursor.fetchall()
		#tree.delete()
		tree.delete(*tree.get_children())
		for row in results:
			tree.insert('', END, values=(row[0],row[1], row[2], row[3]))
	except:
		showerror ("Mensaje", "Error en la carga del Treeview!")
		
def borrar():
	try:
		i = tree.selection()[0] #'[0]'puede o no ser necesario
		value = tree.item(i, 'values')[0] #0=código, 1=desc
		delete = """DELETE FROM concepto_gastos WHERE cg_cod=("%s");""" % (value)
		cursor.execute(delete)
		connect.commit()
		showinfo("mensaje", "Concepto borrado!")
		cargar()
	except MySQLdb.IntegrityError:
		showerror ('Mensaje', "Error al borrar el registro.")
	except TypeError, e:
		showerror("Error", e)
		
	#except MySQLdb.IntegrityError, e:
		#showerror("Error", e)
