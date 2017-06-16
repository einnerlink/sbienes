#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from tkMessageBox import*
import MySQLdb
from controller import *
import analisis_arrendatarios
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

class Proceso_Fact_Auto_Arre(Frame):
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)
                
                global opt
                
                #VARIABLES
                opt = IntVar()
                
                #WIDGETS
                header = Label(self, text="PROCESO DE FACTURACIÓN AUTOMÁTICO ARRENDATARIOS", font="bold")
                header.pack(pady=20, side=TOP)
                
                wrapper = Frame (self)
                wrapper.pack()
                
                r1 = Radiobutton(wrapper, text="Generar Análisis", variable=opt, value=0).pack(pady=5, anchor=W)
                r2 = Radiobutton(wrapper, text="Generar Facturación", variable=opt, value=1).pack(pady=5, anchor=W)
                Button(wrapper, text="Iniciar Proceso", bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=operacion).pack(pady=5, anchor=W)
                
def operacion():
        if opt.get()==0:
                showinfo('Operación', "Generar Análisis")
                #analisis_arrendatarios.pdf_analisis_arre()
                try:
                        connect.commit()
                        #Consulta de códigos y valores de la tabla 'configuracion'
                        cursor.execute("SELECT cod_canon, cod_subtotalarrend, cod_ivaarrend, retefuente, ivajuridico, rteiva, resolucion FROM configuracion;")
                        dato1 = cursor.fetchall()
                        #Consulta de datos generales del propietario y el arrendatario para la factura
                        #cursor.execute("SELECT p_cc, dueño, r_carpeta, relacionip.i_cod, i_dir, FORMAT(SUM( i_vlrenta), 3, 'es_CO'), i_tel, contratos.a_cc, inquilino, a_tpersona, a_contribuyente FROM contratos INNER JOIN relacionip ON contratos.r_id = relacionip.r_id INNER JOIN inmuebles ON relacionip.i_cod = inmuebles.i_cod INNER JOIN arrendatarios ON contratos.a_cc = arrendatarios.a_cc;")
                        cursor.execute("SELECT p_cc, dueño, r_carpeta, relacionip.i_cod, i_dir, i_vlrenta, i_tel, contratos.a_cc, inquilino, a_tpersona, a_contribuyente FROM contratos INNER JOIN relacionip ON contratos.r_id = relacionip.r_id INNER JOIN inmuebles ON relacionip.i_cod = inmuebles.i_cod INNER JOIN arrendatarios ON contratos.a_cc = arrendatarios.a_cc;") 
                        dato2 = cursor.fetchall()
                except:
                        pass
                for c in dato1:
                        canon = c[0]
                        subtotal = c[1]
                        iva = c[2]
                        retef = c[3]
                        ivajuridi = c[4]
                        retei = c[5]
                        resolucion = c[6]
                        
                doc = SimpleDocTemplate("facturas/factura_auto_inquilino.pdf", pagesize = (595.27,400.00),
                                                        rightMargin=5,leftMargin=5,
                                                        topMargin=10, bottomMargin=0)
                story=[]
                                                        
                for i in dato2:
                        nit = i[0]
                        prop = i[1]
                        folder = i[2]
                        inm = i[3]
                        loc = i[4]
                        renta = i[5]
                        renta1 = locale.format("%d", renta, grouping=True)
                        tel = i[6]
                        cc = i[7]
                        arrend = i[8]
                        tipo = i[9]
                        contri = i[10]
                        #SI ARREND ES NATURAL(1)
                        if tipo == 1:
                                tipo = 0
                                tipo1 = locale.format("%d", tipo, grouping=True)
                        #SI ARREND ES JURÍDICO(2)
                        if tipo == 2:
                                tipo = renta*ivajuridi/100
                                tipo1 = locale.format("%d", tipo, grouping=True)
                                
                        total = locale.format("%d", renta+tipo, grouping=True)
                        
                        tiempo = datetime.date.today()
                        anio = time.strftime("%Y")
                        mes = time.strftime("%B")
                        
                        #-------------------------------------------- CABECERA DEL DOCUMENTO
                        
                        #VARIABLES
                        logo = Image("img/logo.gif", width=150, height=45) #LOGO
                        logo.hAlign ='LEFT' #Posicion de la img en la hoja
                                
                        info = Paragraph('''<para align=center leading=8><font size=6>CALLE 11A N°42-68 LOC,195 ED. EL DORADO<br/>
                                                TELEFONO: 3110513 FAX:2664154<br/>
                                                AFILIADO A FENALCO<br/>
                                                M.A.V.U N°000078</font></para>''', styleSheet["BodyText"])
        
                        tipoDoc = Paragraph ('''<para align=right><b>FACTURA DE VENTA<br/>N°</b></para>''', styleSheet["BodyText"])
        
                        #TABLA 1
                        tabla1 = Table([[logo, info, tipoDoc]], colWidths=[200,150,140], rowHeights=None)
                        tabla1.setStyle([
                                ('VALIGN', (1,0), (2,0), 'TOP'),
                                ('ALIGN', (2,0), (2,0), 'RIGHT')#ALINEAR A LA DER
                                ])
                
                        story.append(tabla1) #Construye la tabla 't' definida anteriormente
                        story.append(Spacer(0,-10)) #Espacio del salto de línea con el siguiente Ejemplo
        
                        #-------------------------------------------- DATOS GENERALES DEL DOCUMENTO
        
                        #VARIABLES
                        inquilino = Paragraph ('''<font size=6><b>Nombre Arrendatario:</b><br/></font>%s'''%arrend, styleSheet["BodyText"])
                        docID = Paragraph ('''<font size=6><b>CC/Nit: </b></font>       %s''' %nit, styleSheet["BodyText"])
                        locImn = Paragraph ('''<font size=6><b>Dirección Inmueble:</b><br/></font>%s'''%loc, styleSheet["BodyText"])
                        telefono = Paragraph ('''<font size=6><b>Teléfono:</b><br/></font>%s'''%tel, styleSheet["BodyText"])
                        IDpropietario = Paragraph ('''<font size=6><b>CC/Nit:</b><br/></font>%s'''%cc, styleSheet["BodyText"])
                        propietario = Paragraph ('''<font size=6><b>Propietario: </b></font>%s'''%prop, styleSheet["BodyText"])
                        fechaFormato = Paragraph ('''<para align=center fontSize=6>Día Mes Año</para>''', styleSheet["BodyText"])
                        hoy = time.strftime("%d/%m/%Y")
                        fecha = Paragraph ('''<para align=center spaceBefore=0>%s</para>''' %hoy, styleSheet["BodyText"])
                        codigoImn = Paragraph ('''<font size=6><b>Código Inmueble:</b><br/></font>%s'''%inm, styleSheet["BodyText"])
        
                        #TABLA 2
                        datos = [[inquilino,'','','','',[fechaFormato,fecha]],
                                        [docID,'','',propietario,'',''],
                                        [locImn,'',telefono,IDpropietario,'',codigoImn]]
                         
                        tabla2 = Table(datos, 
                                                   style=[('BOX',(0,0),(2,2),0.5,colors.black),
                                                                  ('VALIGN', (0,0),(2,0),'TOP'),
                                                                  ('SPAN',(0,0),(2,0)),#Combinar 3 filas (col0,row0) hasta (col2,row0) Arrendatario #0
                                                                  ('SPAN',(0,1),(2,1)),#Combinar 3 filas CC/Nit #1
                                                                  ('SPAN',(0,2),(1,2)),#Combinar 2 filas Dirección #2
                                                                  ('SPAN',(3,1),(5,1)),#Combinar 3 filas Nombre Propietario #
                                                                  ('SPAN',(3,2),(4,2)),#Combinar 2 filas CC/Nit Propietario #
                                                                  ('GRID',(3,1),(4,2),0.5,colors.black),
                                                                  ('GRID',(5,0),(5,2),0.5,colors.black)
                                                                 ],colWidths=[100,90,90,90,80,70], rowHeights=None)
                                                 
                        #Constructor y espaciado
                        story.append(Spacer(0,15)) #Espacio del salto de línea con el siguiente Ejemplo
                        story.append(tabla2) #Construye la tabla 't' definida anteriormente
        
                        #-------------------------------------------- DETALLES DEL DOCUMENTO
        
                        #VARIABLES
                        desc = Paragraph('''<para align=center><b>DESCRIPCION</b></para>''', styleSheet["BodyText"])
                        vlr = Paragraph('''<para align=center><b>VALOR</b></para>''', styleSheet["BodyText"])
                        concepto = Paragraph('''Valor Arrendamiento Mes: %s/%s''' % (mes,anio), styleSheet["BodyText"])
        
                        resol = "Resolucion Dian N°110000658514 de Diciembre de 2015 Consectivo Facturacion 33001 al 36000. P"
        
                        #TABLA 3
                        data=[[desc, '', vlr],          #0
                                  [concepto, '', renta1], #1
                                  ['', '', ''],                 #2
                                  ['', '', ''],                 #3
                                  ['', '', ''],                 #4
                                  ['', '', ''],                 #5
                                  ['', '', ''],                 #6
                                  ['Observaciones', 'SUBTOTAL', renta1], #7
                                  ['', 'IVA', tipo1], #8
                                  [resolucion, 'TOTAL', total]] #9
                                                  
                        #Formato de la tabla
                        tabla3 = Table(data,
                                                style=[('GRID',(0,0),(2,0),0.5,colors.black),#Color regilla de DESCRIPCION & VALOR
                                                       ('BOX',(2,1),(2,9),0.5,colors.black), #Color & grosor de la tabla/marco externo de los VALORES
                                                       #('BACKGROUND',(0,0),(2,0), colors.pink), #Color de fondo de DESCRIPCION & VALOR #0
                                                       ('SPAN',(0,0),(1,0)), #Combinar filas DESCRIPCION #0
                                                       ('BOX',(0,1),(2,6),0.5,colors.black), #Color & grosor de la tabla o marco externo de los DETALLES
                                                       ('ALIGN', (2,1), (2,1), 'RIGHT'),#Centrar renta #1
                                                       ('ALIGN', (2,7), (2,7), 'RIGHT'),#Centrar renta #7
                                                       ('ALIGN', (2,8), (2,8), 'RIGHT'),#Centrar tipo #8
                                                       ('ALIGN', (2,9), (2,9), 'RIGHT'),#Centrar total #9
                                                       #('ALIGN', (2,9), (2,9), 'CENTER'),#Centrar total #9
                                                       ('SPAN',(0,1),(1,1)), #Combinar filas de Detalle #1
                                                       ('SPAN',(0,2),(1,2)), #Combinar filas de Detalle #2
                                                       ('SPAN',(0,3),(1,3)), #Combinar filas de Detalle #3
                                                       ('SPAN',(0,4),(1,4)), #Combinar filas de Detalle #4
                                                       ('SPAN',(0,5),(1,5)), #Combinar filas de Detalle #5
                                                       ('SPAN',(0,6),(1,6)), #Combinar filas de Detalle #6
                                                       ('GRID',(1,7),(2,9),0.5,colors.black),#Color regilla de SUBTOTAL, IVA, TOTAL
                                                       ('BOX',(0,7),(0,9),0.5,colors.black), #Color & grosor de la tabla o marco externo de los OBSERVACIONES Y RESOLUCION
                                                       ('FONTSIZE', (0,9),(0,9),7), #Tamaño de la Resolucion
                                                       #('BACKGROUND',(1,9),(1,9),colors.black),#Color de fondo de TOTAL
                                                       ('TEXTCOLOR',(1,9),(1,9),colors.black), #Color de letra de TOTAL
                                                       #('BACKGROUND',(2,9),(2,9),colors.grey)#Color de fondo de VALOR TOTAL
                                                          ],colWidths=[340,80,100], rowHeights=None)
        
                        story.append(Spacer(0,15)) #Espacio del salto de línea con el siguiente Ejemplo
                        story.append(tabla3) #Construye la tabla 't' definida anteriormente
        
                        #-------------------------------------------- FIN PDF
        
                doc.build(story) #Constructor del documento
        
                if sys.platform == 'linux2':
                        os.system("xdg-open ~/SBIENES/facturas/factura_auto_inquilino.pdf")#DEBIAN
                elif sys.platform == 'linux2':
                        os.system("/usr/bin/gnome-open facturas/factura_auto_inquilino.pdf")#UBUNTU
                else:
                        os.startfile("F:/SBIENES/facturas/factura_auto_inquilino.pdf")#WINDOWS
                
        else:
                #AÑO/MES DEL SISTEMA
                fechasys = time.strftime("%Y%m")
                #AÑO/MES DE MYSQL FACTURA
                cursor.execute("SELECT EXTRACT( YEAR_MONTH FROM fa_fecha)FROM factura_arre;")
                results = cursor.fetchall()
                for fechasys in results:
                        showerror("","No se permite esta operación por este mes!")
                        break
                else:
                        cursor.execute("SELECT ivajuridico FROM configuracion;")
                        dato1 = cursor.fetchall()
                        cursor.execute("SELECT c_cod, now(), relacionip.i_cod, i_vlrenta, a_tpersona FROM contratos INNER JOIN relacionip ON contratos.r_id = relacionip.r_id INNER JOIN inmuebles ON relacionip.i_cod = inmuebles.i_cod INNER JOIN arrendatarios ON contratos.a_cc = arrendatarios.a_cc;")
                        dato2 = cursor.fetchall()
                        connect.commit()
                        for a in dato1:
                                ivaj = a[0]
                                #print ivaj #El mismo resultado que a[0]
                                #print a[0] #El mismo resultado que ivaj = a[0]
                                for i in dato2:
                                        if i[4] == 2:
                                                #showinfo("","Es Jurídico")
                                                #iva = ivaj
                                                iva = i[3]*ivaj/100
                                                total = i[3]+iva
                                        else:
                                                #showinfo("","Es Natural")
                                                iva = 0
                                                #total = i[3]*ivaj/100
                                                total = i[3]+iva
                                        cursor.execute('''INSERT INTO factura_arre(c_cod, fa_fecha, fa_iva, fa_total) 
                                                        SELECT c_cod, now(), '%f', '%f' FROM contratos 
                                                        INNER JOIN relacionip ON contratos.r_id = relacionip.r_id 
                                                        INNER JOIN inmuebles ON relacionip.i_cod = inmuebles.i_cod 
                                                        INNER JOIN arrendatarios ON contratos.a_cc = arrendatarios.a_cc;''' % (iva, total))
                                        connect.commit()
                        showinfo('Operación', "Grabado!")
