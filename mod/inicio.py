#!/usr/bin/python
from Tkinter import*

class Inicio(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		logo = PhotoImage(file='img/favicon.gif')

		self.caja = Frame(self)
                self.caja.pack(fill=X)

		self.label = Label(self.caja, image=logo)
		self.label.image = logo
		self.label.pack(pady=200)
