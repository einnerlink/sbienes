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
        cursor.execute("SELECT cod_canon, cod_subtotalarrend, cod_ivaarrend, retefuente, ivajuridico, rteiva FROM configuracion;")
        dato1 = cursor.fetchall()
        cursor.execute("SELECT p_cc, dueño, r_carpeta, relacionip.i_cod, i_dir, i_vlrenta, i_tel, contratos.a_cc, inquilino, a_tpersona, a_contribuyente FROM contratos INNER JOIN relacionip ON contratos.r_id = relacionip.r_id INNER JOIN inmuebles ON relacionip.i_cod = inmuebles.i_cod INNER JOIN arrendatarios ON contratos.a_cc = arrendatarios.a_cc;")
        dato2 = cursor.fetchall()
except:
        pass
        #showerror ("Mensaje", "Error al cargar los registros!")

class AnalisisArre(Frame):
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)
                
                #WIDGETS
                Label(self, text="Análisis de Facturación de los Arrendatarios: ").pack()
                Button(self, text="PDF", command=pdf_analisis_arre).pack()
                
def pdf_analisis_arre():
        
        doc = SimpleDocTemplate("analisis/analisis_arrendatarios.pdf", pagesize = letter,
                                                        #rightMargin=72,leftMargin=72,
                                                        topMargin=10)
        story=[]
        
        #doc = SimpleDocTemplate("analisis/analisis_propietario.pdf", pagesize = letter,
    #                    rightMargin=72,leftMargin=72,
    #                    topMargin=10,bottomMargin=18)
        
        # Cabecera
        
        text = Paragraph('''<para align=center><strong><font size=14>ANALISIS FACTURACION ARRENDATARIOS</font></strong></para>''', styleSheet["BodyText"])
        
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
        
        for c in dato1:
                canon = c[0]
                subtotal = c[1]
                iva = c[2]
                retef = c[3]
                ivajuridi = c[4]
                retei = c[5]
                
        for i in dato2:
                nit = i[0]
                prop = i[1]
                folder = i[2]
                inm = i[3]
                loc = i[4]
                renta = i[5]
                tel = i[6]
                cc = i[7]
                arrend = i[8]
                tipo = i[9]
                contri = i[10]
                #SI ARREND ES NATURAL(1)
                if tipo == 1:
                        tipo = 0
                #SI ARREND ES JURÍDICO(2)
                if tipo == 2:
                        tipo = renta*ivajuridi/100

                total = renta+tipo

                tiempo = datetime.date.today()
                anio = time.strftime("%Y")
                mes = time.strftime("%B")
                                
                #var = Paragraph(''' ''' % , styleSheet["BodyText"])
                inmueble = Paragraph('''%s Código Imnueble: %s''' % (folder,inm), styleSheet["BodyText"])
                telefono = Paragraph('''Teléfono: %s: '''% tel, styleSheet["BodyText"])
                concepto = Paragraph('''Valor Arrendamiento Mes: %s/%s''' % (mes,anio), styleSheet["BodyText"])
                
                tabla = Table([
                                        ['Propietario: ', prop, 'CC/Nit: ', nit,'',''],
                                        ['Carpeta: ', inmueble, 'Dirección: ', loc,'',''],
                                        ['Arrendatario: ', arrend, 'CC/Nit: ', cc,'Teléfono: ',tel],
                                        [canon, concepto, '','','',renta],
                                        ['','','',subtotal,'Subtotal',renta],
                                        ['','','',iva,'IVA',tipo],
                                        ['','','','','Total',total]
                                        ], colWidths=[80,200,50,60,50,150], rowHeights=None)
                tabla.setStyle([
                                        ('SPAN',(3,1),(5,1)), #Combinar filas Loc
                                        ('SPAN',(1,2),(2,2)), #Combinar filas Arrendatario
                                        ('ALIGN', (5,5), (5,5), 'LEFT'),#Alinear texto de IVA a la IZQ
                                        ('LINEABOVE', (0,7),(5,7),1,colors.black)
                                        #('INNERGRID',(0,0),(-1,-1),1,colors.red), #Color de línea interna de la tabla
                                        #('ALIGN', (0,0), (-1, -1), 'LEFT') #Alineación horizontal del texto
                                        ])
                story.append(tabla)
                story.append(Spacer(0,15))
                
        
        #------------------------------------------------ FIN DEL DOCUMENTO
        
        doc.build(story)
        if sys.platform == 'linux2':
                os.system("xdg-open ~/SBIENES/analisis/analisis_arrendatarios.pdf")#DEBIAN
        elif sys.platform == 'linux2':
                os.system("/usr/bin/gnome-open ~/SBIENES/analisis/analisis_arrendatarios.pdf")#UBUNTU
        else:
                os.startfile("F:/SBIENES/analisis/analisis_arrendatarios.pdf")#WINDOWS
