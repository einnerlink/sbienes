#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
#from ttk import*
from tkMessageBox import showinfo,showerror
import MySQLdb
import os
		
class exportDB(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)		
		
		#========================= HEADER ===========================
		
		self.header = Label(self, text="EXPORTAR BASE DE DATOS", font="bold")
		self.header.pack(pady=20, side=TOP)
		
		f = Frame(self)
		f.pack(fill=X)#-------------------------------
		
		texto = """Utilice esta opción para exportar la base de datos MySQL para tener un respaldo de toda la información de su empresa."""
		msg = Message(f, width=500, text=texto)
		msg.pack()
		
		csv = PhotoImage(file='img/db_to_sql.gif')
		l = Label(f, image=csv)
		l.image = csv
		l.pack()
		
		Button(self, text="Exportar DB", command=gensql).pack(side=RIGHT)

def gensql():
	try:
		#connect.commit()
		os.system("mysqldump -u root -p sbienes > backup/sbienes.sql")
		showinfo("Mensaje", "Base de datos guardada!")
	except:
		showerror ("Error", "Error al exportar la base de datos!")
