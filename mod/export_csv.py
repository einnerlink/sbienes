#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from tkMessageBox import showinfo,showerror
import MySQLdb
import os
from controller import *
	
class exportCSV(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		#========================= HEADER ===========================
		
		self.header = Label(self, text="EXPORTAR BASE DE DATOS A CSV", font="bold")
		self.header.pack(pady=20, side=TOP)
		
		f = Frame(self)
		f.pack(fill=X)#-------------------------------
		
		texto = """Utilice esta opción para exportar la base de datos MySQL a un archivo tipo CSV que puede ser abierto en una hoja de cálculo como Cal o Excel."""
		msg = Message(f, width=500, text=texto)
		msg.pack()
		
		csv = PhotoImage(file='img/db_to_csv.gif')
		l = Label(f, image=csv)
		l.image = csv
		l.pack()
		
		Button(self, text="Exportar CSV", command=gencsv).pack(side=RIGHT)

def gencsv():
	try:
		connect.commit()
		sql = "select dueño, i_dir from relacionip into OUTFILE '/tmp/relacionip.csv';"
		cursor.execute(sql)
		os.system("sudo mv /tmp/relacionip.csv ~/ ")
		showinfo("Mensaje", "Archivo CSV exportado!")
	except:
		showerror ("Mensaje", "Error al exportar archivo.csv")
