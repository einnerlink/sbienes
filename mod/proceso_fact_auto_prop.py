#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from tkMessageBox import*
import MySQLdb
from controller import *
import analisis_propietarios

class Proceso_Fact_Auto_Prop(Frame):
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)
                
		global opt
		
		#VARIABLES
		opt = IntVar()
		
		#WIDGETS
		header = Label(self, text="PROCESO DE FACTURACIÓN AUTOMÁTICO PROPIETARIOS", font="bold")
		header.pack(pady=20, side=TOP)
		
		wrapper = Frame (self)
		wrapper.pack()
		
		r1 = Radiobutton(wrapper, text="Generar Análisis", variable=opt, value=0).pack(pady=5, anchor=W)
		r2 = Radiobutton(wrapper, text="Generar Facturación", variable=opt, value=1).pack(pady=5, anchor=W)
		Button(wrapper, text="Iniciar Proceso", command=operacion).pack(pady=5, anchor=W)
		
def operacion():
	if opt.get()==0:
		showinfo('Operación', "Generar Análisis")
		analisis_propietarios.pdf_analisis_prop()
	else:
		showinfo('Operación', "Generar Facturación")
