#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*

class Acerca(Frame):
	def __init__(self, parent, controller):
                Frame.__init__(self, parent)
		
		#WIDGETS
		
		#========================= HEADER ==============================
		
		self.header = Label(self, text="SBIENES", font="bold")
		self.header.pack(pady=20, side=TOP)

		#========================= WRAPPER =============================

		#quote"""Este software ha sido desarrollado para la administración de propiedades de agencias de arrendamiento por Einnerlink\n mediante Python 2.7 y algunas de sus destacadas librerías como MySQLdb, Reportlab, etc.\n\n© 2016 Einnerlink\neinnerlink@gmail.com\neinnerlink.tk\nMedellín - Colombia"""
		quote = """SBIENES es un software para la administración de propiedades de agencias de arrendamiento desarrollado por Einnerlink mediante Python 2.7 y algunas de sus librerías como: Tk, ttk, MySQLdb, Reportlab, etc.\n\n© 2016 Einnerlink\neinnerlink@gmail.com\neinnerlink.tk\nMedellín - Colombia"""
		
				
		self.wrapper = Frame(self)
		self.wrapper.pack(fill=X)#-------------------------------
		
		self.m = Message(self.wrapper, width=500, text=quote)
		#self.m = Message(self.wrapper, width=500, text="Software para la administración de propiedades de agencias de arrendamiento desarrollado por Einnerlink mediante Python 2.7 y algunas de sus destacadas librerías como MySQLdb, reportlab, etc.\n\n© 2016 Einnerlink\neinnerlink@gmail.com\neinnerlink.tk\nMedellín - Colombia")
		self.m.pack()
		"""self.l = Label(self.wrapper, text=quote, justify=CENTER)
		self.l.pack()"""
