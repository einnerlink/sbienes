#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from ttk import Combobox, Treeview
from tkMessageBox import*
import MySQLdb
from controller import *

class ReajustesProp(Frame):
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)

		global cc, nombre, inmuebles, valor, mes, meses, cbox
		
		lupa = PhotoImage(file='img/lupa.gif')
		cc = StringVar()
		nombre = StringVar()
		inmuebles = StringVar()
		valor = DoubleVar()
		
		mes = StringVar()
		meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto","Septiembre", "Octubre", "Noviembre", "Diciembre"]
		
		#WIDGETS
		
		#=========================== HEADER ============================
		
		self.titleL = Label(self, text="REAJUSTES A PROPIETARIOS", font="bold")
		self.titleL.pack(pady=20, side=TOP)
		
		#=========================== WRAPPER ===========================
		
		self.wrapper = Frame (self)
		self.wrapper.pack(side=TOP, fill=Y)
		
		lf = LabelFrame(self.wrapper, text="Propietario / Inmueble")
		lf.pack(fill=X)
		
		f = Frame(lf)
		f.pack(pady=5, fill=X)#-----------------------------------
		
		e = Entry (f, textvariable=cc, width=20)
		e.pack(side=LEFT)
		
		b1 = Button(f, image=lupa, command=buscar)
		b1.image = lupa
		b1.pack(side=LEFT)
		
		cbox = Combobox(f, textvariable=inmuebles, width=30)
		cbox.pack(side=LEFT, fill=X, expand=1)
		
		f0 = Frame(lf)
		f0.pack(side=TOP,pady=5, fill=X)#-----------------------------------
		
		e2 = Entry (f0, textvariable=nombre, width=60, state=DISABLED)
		e2.pack(side=LEFT, fill=X, expand=1)
		
		f1 = Frame(self.wrapper)
		f1.pack(pady=5, fill=X)#-----------------------------------
		
		l1 = Label(f1, text='Valor reajuste: ')
		l1.pack(side=LEFT)
		
		e1 = Entry (f1, textvariable=valor, width=20)
		e1.pack(side=LEFT)
		
		l2 = Label(f1, text='Mes: ')
		l2.pack(side=LEFT)
		
		Cbx2 = Combobox(f1, textvariable=mes, values=meses, width=10)
		Cbx2.set('')
		Cbx2.pack(side=LEFT)
		
		f2 = Frame(self.wrapper)
		f2.pack(pady=5, fill=X)#-----------------------------------
		
		b1 = Button (f2, text="Cancelar", command=cancelar)
		b1.pack(side=RIGHT)
		
		b2 = Button (f2, text="Grabar e Imprimir", command=guardar)
		b2.pack(side=RIGHT)
		
def buscar():
	try:
		connect.commit()
		sql = """SELECT dueño FROM relacionip WHERE p_cc=("%s");""" % (cc.get())
		cursor.execute(sql)
		results = cursor.fetchone()
		for d in results:
			nombre.set(d)
		try:
			connect.commit()
			query = """SELECT i_cod FROM relacionip WHERE p_cc=("%s");""" % (cc.get())
			cursor.execute(query)
			res = cursor.fetchall()
			for i in results:
				cbox['values'] = res
		except:
			pass
			
		#EJEMPLO
		"""	
		#for i in results:
			nombre.set(i[0])
			#cbox['values'] = results #FUNCIONA PERO ARROJA p+i
			#cbox['values'] = i # DEVUELVE SOLO EL ULTIMO VALOR
			inm = i[1]
			print inm
			#print i[1]
			cbox['values'] = (0, imn)"""
	except:
		showerror("Error","No existe ese num de id.")
	
def guardar():
	try:
		pass
	except MySQLdb.IntegrityError:
		showerror ("Mensaje", "")
		
def cancelar():
	try:
		cc.set("")
		nombre.set("")
		cbox['values'] = []
		inmuebles.set("")
		valor.set(0.0)
		mes.set("")
	except MySQLdb.IntegrityError:
		showerror ('Mensaje', "")
	
