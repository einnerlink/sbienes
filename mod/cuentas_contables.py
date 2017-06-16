#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from ttk import Combobox, Treeview
from tkMessageBox import*
import MySQLdb
from controller import *

class CuentasContables(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		global codigo, descripcion, tree, busqueda, info
		global e3
		
		lupa = PhotoImage(file='img/lupa.png')
		
		codigo = StringVar()
		descripcion = StringVar()
		busqueda = StringVar()
		info = IntVar()
		
		#WIDGETS
		
		#=========================== HEADER ============================
		
		self.titleL = Label(self, text="CUENTAS CONTABLES", font="bold")
		self.titleL.pack(pady=20, side=TOP)
		
		#=========================== WRAPPER ===========================
		
		self.wrapper = Frame (self)
		self.wrapper.pack(side=TOP, fill=Y)
		#self.wrapper.pack(side=LEFT, fill=Y) #UBICA EL FORM A LA IZQ
		
		self.f0 = Frame(self.wrapper)
		self.f0.pack(pady=5, fill=X)#-----------------------------------
		
		l1 = Label (self.f0, text="Código:")
		l1.pack(side=LEFT)
		e1 = Entry (self.f0, textvariable=codigo, width=20)
		e1.pack(side=LEFT)
		e1.bind("<KeyRelease>", caps)
		e1.focus_set()
		
		self.f2 = Frame(self.wrapper)
		self.f2.pack(pady=5, fill=X)#-----------------------------------
		
		l2 = Label (self.f2, text="Descripción: ")
		l2.pack(side=LEFT)
		e2 = Entry (self.f2, textvariable=descripcion, width=60)
		e2.pack(side=LEFT, fill=X, expand=1)
		e2.bind("<KeyRelease>", caps)
		
		self.f3 = Frame(self.wrapper)
		self.f3.pack(pady=5, fill=X)#-----------------------------------
		
		b1 = Button (self.f3, text="Cargar", bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=cargar)
		b1.pack(side=RIGHT)
		
		b2 = Button (self.f3, text="Agregar", bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=agregar)
		b2.pack(side=RIGHT)
		
		#========================== TREEVIEW ===========================
		
		self.f4 = Frame(self.wrapper)
		self.f4.pack(pady=5, fill=X)#-----------------------------------
		
		tree = Treeview(self.f4, show="headings", columns=('col1','col2'))
		tree.pack(side=LEFT, fill=X, expand=1)
		tree.column('col1', width=0, anchor='center')
		tree.column('col2', width=150, anchor='w')
		
		tree.heading('col1', text='Código')
		tree.heading('col2', text='Descripción')
		
		self.scroll = Scrollbar(self.f4,orient=VERTICAL,command=tree.yview)
		tree.configure(yscrollcommand=self.scroll.set)
		
		self.f5 = Frame(self.wrapper)
		self.f5.pack(pady=5, fill=X)#-----------------------------------
		
		self.delete = Button (self.f5, text="Eliminar", bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=borrar)
		self.delete.pack(side=RIGHT)
		
		e3 = Entry(self.f5, textvariable=busqueda)
		e3.pack(side=LEFT)
		e3.bind("<KeyRelease>", caps)
		
		b3 = Button(self.f5, text='BUSCAR', image=lupa, command=buscar)
		b3.image = lupa
		b3.pack(side=LEFT)
		
		R1 = Radiobutton(self.f5, text="Código", variable=info, value=1)
		R1.pack(side=LEFT)
		R2 = Radiobutton (self.f5, text="Desc", variable=info, value=2)
		R2.pack(side=LEFT)
		info.set(1)

def caps(event):
	codigo.set(codigo.get().upper())
	descripcion.set(descripcion.get().upper())
	busqueda.set(busqueda.get().upper())

def buscar():
	r = info.get()
	if r == 1:
		v = busqueda.get()
		children = tree.get_children() #OBTIENE LOS iid DE LOS ITEMS
		for child in children:
			i = tree.item(child, 'values')[0]
			if v == i:
				tree.selection_set(child)
				showinfo("Mensaje", "Dato encontrado!")
			else:
				#showerror("Error", "Dato no encontrado!")
				pass
	else:
		v = busqueda.get()
		children = tree.get_children() #OBTIENE LOS iid DE LOS ITEMS
		for child in children:
			i = tree.item(child, 'values')[1]
			if v == i:
				tree.selection_set(child)
				showinfo("Mensaje", "Dato encontrado!")
			else:
				#showerror("Error", "Dato no encontrado!")
				pass

"""
def buscar(item = ''):
	children = tree.get_children(item) #OBTIENE LOS iid DE LOS ITEMS
	for child in children:
		text = tree.item(child, 'text')
		if text.startswith(e3.get()):
			tree.selection_set(child)
			return True
		else:
			res = buscar(child)
			if res:
				return True"""
					
def agregar():
	try:
		connect.commit
		sql = "INSERT INTO cuentas_contables(cc_cod, cc_desc)VALUES('%s', '%s'); " % (codigo.get(), descripcion.get())
		cursor.execute(sql)
		#connect.commit()
		showinfo ("Mensaje", "Cuenta contable guardada!")
		codigo.set("")
		descripcion.set("")
		cargar()
	except MySQLdb.IntegrityError:
		showerror ("Mensaje", "Error al guardar la cuenta!")

def cargar():
	try:
		connect.commit()
		tv = "SELECT cc_cod, cc_desc FROM cuentas_contables"
		#tv = "SELECT cc_cod, cc_desc FROM cuentas_contables order by cc_desc;"
		cursor.execute(tv)
		results = cursor.fetchall()
		#tree.delete()
		tree.delete(*tree.get_children())
		for row in results:
			tree.insert('', END, values=(row[0],row[1]))
	except:
		showerror ("Mensaje", "Error en la carga del Treeview!")
		
def borrar():
	try:
		i = tree.selection()[0] #'[0]'puede o no ser necesario
		value = tree.item(i, 'values')[0] #0=código, 1=desc
		delete = """DELETE FROM cuentas_contables WHERE cc_cod=("%s");""" % (value)
		cursor.execute(delete)
		connect.commit()
		showinfo("mensaje", "Cuenta borrada!")
		cargar()
	except MySQLdb.IntegrityError:
		showerror ('Mensaje', "Error al borrar el registro.")
	
