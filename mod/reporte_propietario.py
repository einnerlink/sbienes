#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from ttk import*
from tkMessageBox import*
import os
import MySQLdb
from controller import *
#from ttk import Progressbar
#PLATYPUS
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,
Paragraph, Table, TableStyle, Image)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

try:
	connect.commit()
	search = "SELECT p_cc, dueño, i_cod, inmueble FROM relacionip;"
	#search = "SELECT p_cc, dueño, inmueble FROM relacionip;"
	cursor.execute(search)
	dato = cursor.fetchall()
except:
	pass
	#showerror ("Mensaje", "Error al cargar los registros!")

	
class Reporteprop(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		#WIDGETS
		Label(self, text="Listado de inmuebles con sus respectivos propietarios: ").pack()
		Button(self, text="PDF", command=pdf).pack()
		
def pdf():
	doc = SimpleDocTemplate("reportes/reporte_propietario.pdf", pagesize = letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=10,bottomMargin=18)
	story=[]
	for i in dato:
		cc = i[0]
		n = i[1]
		c = i[2]
		d = i[3]
	# También funciona	
	"""
	for cc, n, c, d in dato:
		nit = cc
		nombre = n
		cod = c
		loc = d
	"""
	
	#-------------------------------------------------------------------
	
	#ENCABEZADO
	logo = Image("img/logo.gif", width=200, height=50) #LOGO
	logo.hAlign ='LEFT' #Posicion de la img en la hoja
	
	estilo=getSampleStyleSheet()
	p1 = Paragraph("LISTADO DE PROPIETARIOS", estilo['Heading1'])#TITULO CON ESTILO H1
	
	header = Table([
		[logo, p1]
		], colWidths=300, rowHeights=None)
	story.append(header)
	story.append(Spacer(0,15))
	
	#-------------------------------------------------------------------

	#DETALLES
	detalles = Table([
					['NIT/CC', 'NOMBRES', 'COD','DIR CASA']
					], colWidths=150, rowHeights=None)
	detalles.setStyle([
		('TEXTCOLOR', (0, 0), (2, -1), colors.black),#Color del texto
		#('INNERGRID',(0,0),(-1,-1),1,colors.red), #Color de línea interna de la tabla
		('ALIGN', (0,0), (-1, -1), 'LEFT') #Alineación horizontal del texto
		])
	story.append(detalles)
	story.append(Spacer(0,15))
	
	#TABLA DE DATOS
	t = Table(dato, colWidths=None, rowHeights=None)
	"""
	t = Table([
			['NIT/CC', 'Nombres', 'Dir Casa'],
			[cc, n, d]
			], colWidths=None, rowHeights=None)
	t.setStyle([
		('TEXTCOLOR', (0, 0), (0, -1), colors.black),#Color del texto
		#('BACKGROUND',(0,0),(-1,-1),colors.cyan), #Color de fondo de la tabla
		#('BOX',(0,0),(-1,-1),1.25,colors.black), #Color de línea de la tabla
		('INNERGRID',(0,0),(-1,-1),1,colors.black), #Color de línea interna de la tabla
		('ALIGN', (0,0), (-1, -1), 'LEFT'), #Alineación horizontal del texto
	    ])"""
	story.append(t)
	story.append(Spacer(0,15))
	
	#------------------------------------------------ FIN DEL DOCUMENTO
	
	doc.build(story)
	if sys.platform == 'linux2':
		os.system("xdg-open ~/SBIENES/reportes/reporte_propietario.pdf")#DEBIAN
	elif sys.platform == 'linux2':
		os.system("/usr/bin/gnome-open reportes/reporte_propietario.pdf")#UBUNTU
	else:
		os.startfile("D:/SBIENES/reportes/reporte_propietario.pdf")#WINDOWS
