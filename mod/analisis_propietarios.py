#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
import MySQLdb
from controller import *
import os
import datetime
import time
import locale
locale.setlocale(locale.LC_ALL, "")
#LIBRERÍA PLATYPUS DE REPORTLAB PARA CREAR TABLAS
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,
Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
styleSheet = getSampleStyleSheet()
style = styleSheet['BodyText']

try:
	connect.commit()
	config = "SELECT cod_comision, cod_subtototalprop, cod_ivaprop, comision, iva, retefuente, ivajuridico, rteiva FROM configuracion;"
	cursor.execute(config)
	dato1 = cursor.fetchall()
	search = "SELECT dueño, relacionip.p_cc, r_carpeta, relacionip.i_cod, inmueble, inquilino, contratos.a_cc, i_tel, i_vlrenta, p_tpersona, p_retefuente, p_reteiva, p_contribuyente FROM contratos INNER JOIN relacionip ON contratos.r_id = relacionip.r_id INNER JOIN inmuebles ON relacionip.i_cod = inmuebles.i_cod INNER JOIN propietarios ON relacionip.p_cc = propietarios.p_cc;"
	cursor.execute(search)
	dato2 = cursor.fetchall()
except:
	pass
	#showerror ("Mensaje", "Error al cargar los registros!")

class AnalisisProp(Frame):
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)
                
		#WIDGETS
		header = Label(self, text="ANALISIS FACTURACION DE PROPIETARIOS", font="bold")
		header.pack(pady=20, side=TOP)
		
		#Label(self, text="Análisis de Facturación de los Propietarios: ").pack()
		Button(self, text="PDF", command=pdf_analisis_prop).pack()
		
def pdf_analisis_prop():
	
	doc = SimpleDocTemplate("analisis/analisis_propietarios.pdf", pagesize = letter,
							#rightMargin=72,leftMargin=72,
							#topMargin=10,bottomMargin=18)
							topMargin=10)
	story=[]
	
	#CABECERA
	text = Paragraph('''<para align=center><strong><font size=14>ANALISIS FACTURACION PROPIETARIOS</font></strong></para>''', styleSheet["BodyText"])
	
	story.append(text)
	story.append(Spacer(5, 50))
	"""
	t4bl4 = Table([
					['ANALISIS FACTURACION PROPIETARIOS']
					], colWidths=150, rowHeights=None)
	t4bl4.setStyle([
				('ALIGN', (0,0), (0,0), 'CENTER') #Alineación horizontal del texto
					])
	story.append(t4bl4)
	story.append(Spacer(0,15))
	"""
	
	for conf in dato1:
		cod_comision = conf[0]
		cod_subtototalprop = conf[1]
		cod_ivaprop = conf[2]
		comision = conf[3]
		iva = conf[4]
		retefuente = conf[5]
		ivajuridico = conf[6]
		rteiva = conf[7]
		
		#subtotal = conf[1]
		#iva = conf[2]
		#retef = conf[3]
		#retei = conf[4]
		
	for i in dato2:
		prop = i[0] 	#dueño
		nit = i[1]		#p_cc
		folder = i[2]	#r_carpeta
		inm = i[3]	#relacionip.i_cod
		loc = i[4]		#inmueble
		arrend = i[5]	#inquilino
		cc = i[6]		#a_cc
		tel = i[7]		#i_tel
		renta = i[8]	#i_vlrenta
		tipo = i[9]		#p_tpersona
		propReteF = i[10]	#p_retefuente
		propReteI = i[11]	#p_reteiva
		propContrib = i[12]	#p_contribuyente
		#SI PROP ES NATURAL(1)
		if tipo == 1:
			tipo = 0
		#SI PROP ES JURÍDICO(2)
		if tipo == 2:
			tipo = renta*ivajuridico/100
			
		vlcomision = renta*comision/100
		total = renta+tipo

		tiempo = datetime.date.today()
		anio = time.strftime("%Y")
		mes = time.strftime("%B")
				
		#var = Paragraph(''' ''' % , styleSheet["BodyText"])
		inmueble = Paragraph('''%s Código Imnueble: %s''' % (folder, inm), styleSheet["BodyText"])
		telefono = Paragraph('''Teléfono: %s: ''' % tel, styleSheet["BodyText"])
		concepto = Paragraph('''Comisión Por Administración Mes: %s/%s''' % (mes,anio), styleSheet["BodyText"])
		
		tabla = Table([
					['Propietario: ', prop, 'CC/Nit: ', nit,'',''],
					['Carpeta: ', inmueble, 'Dirección: ', loc,'',''],
					['Arrendatario: ', arrend, 'CC/Nit: ', cc,'Teléfono: ',tel],
					['', concepto, '',cod_comision,'Valor',vlcomision],
					['','','',cod_subtototalprop,'Subtotal',vlcomision],
					['','','',cod_ivaprop,'IVA',tipo],
					['','','','','Total',total]
					], colWidths=[80,200,50,60,50,150], rowHeights=None)
		tabla.setStyle([
					('SPAN',(3,1),(5,1)), #Combinar filas Loc
					('SPAN',(1,2),(2,2)), #Combinar filas Arrendatario
					('SPAN',(1,3),(2,3)), #Combinar filas concepto
					('LINEABOVE', (0,7),(5,7),1,colors.black)
					#('INNERGRID',(0,0),(-1,-1),1,colors.red), #Color de línea interna de la tabla
					#('ALIGN', (0,0), (-1, -1), 'LEFT') #Alineación horizontal del texto
					])
		story.append(tabla)
		story.append(Spacer(0,15))
		
	
	#------------------------------------------------ FIN DEL DOCUMENTO
	
	doc.build(story)
	if sys.platform == 'linux2':
		os.system("xdg-open ~/SBIENES/analisis/analisis_propietarios.pdf")#EN DEBIAN
	elif sys.platform == 'linux2':
		os.system("/usr/bin/gnome-open ~/SBIENES/analisis/analisis_propietarios.pdf")#UBUNTU
	else:
		os.startfile("D:/SBIENES/analisis/analisis_propietarios.pdf")#WINDOWS
