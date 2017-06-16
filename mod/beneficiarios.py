#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from ttk import Combobox, Treeview
from tkMessageBox import*
import MySQLdb
from controller import *

class Beneficiarios(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		global docID, nombre, refbanco, tree, busqueda, info, delete
		global e3
		
		lupa = PhotoImage(file='img/lupa.png')
		
		docID = StringVar()
		nombre = StringVar()
		refbanco = StringVar()
		busqueda = StringVar()
		info = IntVar()
		
		#WIDGETS
		
		#=========================== HEADER ============================
		
		l0 = Label(self, text="BENEFICIARIOS", font="bold")
		l0.pack(pady=20, side=TOP)
		
		#=========================== WRAPPER ===========================
		
		wrapper = Frame (self)
		wrapper.pack(side=TOP, fill=Y)
		#wrapper.pack(side=LEFT, fill=Y) #UBICA EL FORM A LA IZQ
		
		f1 = Frame(wrapper)
		f1.pack(pady=5, fill=X)#-----------------------------------
		
		l1 = Label (f1, text="CC/Nit: ")
		l1.pack(side=LEFT)
		e1 = Entry (f1, textvariable=docID, width=20)
		e1.pack(side=LEFT)
		e1.bind("<KeyRelease>", caps)
		e1.focus_set()
		
		f2 = Frame(wrapper)
		f2.pack(pady=5, fill=X)#-----------------------------------
		
		l2 = Label (f2, text="Nombre: ")
		l2.pack(side=LEFT)
		e2 = Entry (f2, textvariable=nombre, width=60)
		e2.pack(side=LEFT, fill=X, expand=1)
		e2.bind("<KeyRelease>", caps)
		
		f3 = Frame(wrapper)
		f3.pack(pady=5, fill=X)#-----------------------------------
		
		l3 = Label (f3, text="Referencia Bancaria: ")
		l3.pack(side=LEFT)
		e3 = Entry (f3, textvariable=refbanco, width=60)
		e3.pack(side=LEFT, fill=X, expand=1)
		e3.bind("<KeyRelease>", caps)
		
		f4 = Frame(wrapper)
		f4.pack(pady=5, fill=X)#-----------------------------------
		
		b1 = Button (f4, text="Cargar", bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=cargar)
		b1.pack(side=RIGHT)
		
		b2 = Button (f4, text="Agregar", bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=agregar)
		b2.pack(side=RIGHT)
		
		#========================== TREEVIEW ===========================
		
		f5 = Frame(wrapper)
		f5.pack(pady=5, fill=X)#-----------------------------------
		
		tree = Treeview(f5, show="headings", columns=('col1','col2'))
		tree.pack(side=LEFT, fill=X, expand=1)
		tree.column('col1', width=0, anchor='center')
		tree.column('col2', width=150, anchor='w')
		
		tree.heading('col1', text='CC/Nit')
		tree.heading('col2', text='Nombre Completo')
		
		scroll = Scrollbar(f5,orient=VERTICAL,command=tree.yview)
		tree.configure(yscrollcommand=scroll.set)
		
		f6 = Frame(wrapper)
		f6.pack(pady=5, fill=X)#-----------------------------------
		
		delete = Button (f6, text="Eliminar", bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=borrar)
		delete.pack(side=RIGHT)
		
		e4 = Entry(f6, textvariable=busqueda)
		e4.pack(side=LEFT)
		e4.bind("<KeyRelease>", caps)
		
		b4 = Button(f6, text='BUSCAR', image=lupa, command=buscar)
		b4.image = lupa
		b4.pack(side=LEFT)
		
		R1 = Radiobutton(f6, text="CC/nit", variable=info, value=1)
		R1.pack(side=LEFT)
		R2 = Radiobutton (f6, text="Nombre", variable=info, value=2)
		R2.pack(side=LEFT)
		info.set(1)

def caps(event):
	docID.set(docID.get().upper())
	nombre.set(nombre.get().upper())
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
				
def agregar():
	try:
		connect.commit
		sql = "INSERT INTO beneficiarios(b_cc, b_nombre, b_refbanco)VALUES('%s', '%s', '%s'); " % (docID.get(), nombre.get(), refbanco.get())
		cursor.execute(sql)
		showinfo ("Mensaje", "Beneficiario guardado!")
		docID.set("")
		nombre.set("")
		refbanco.set("")
		cargar()
	except MySQLdb.IntegrityError:
		showerror ("Mensaje", "Error al guardar la info!")

def cargar():
	try:
		connect.commit()
		tv = "SELECT b_cc, b_nombre FROM beneficiarios;"
		cursor.execute(tv)
		results = cursor.fetchall()
		tree.delete(*tree.get_children())
		for row in results:
			tree.insert('', END, values=(row[0],row[1]))
	except:
		showerror ("Mensaje", "Error en la carga del Treeview!")
		
def borrar():
	try:
		i = tree.selection()[0] #'[0]'puede o no ser necesario
		value = tree.item(i, 'values')[0] #0=código, 1=desc
		delete = """DELETE FROM beneficiarios WHERE b_cc=("%s");""" % (value)
		cursor.execute(delete)
		connect.commit()
		showinfo("mensaje", "Beneficiario borrada!")
		cargar()
	except MySQLdb.IntegrityError:
		showerror ('Mensaje', "Error al borrar el registro.")
