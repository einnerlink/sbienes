#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
#from ttk import*
from tkMessageBox import*
import MySQLdb
from controller import *

class Config(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		global caja, canon, terceros, papeleria, c_comision, c_iva, c_retefuente, c_ivajuridico, vlfacturainquilino
		global intereses, impuestos, retefuenteS, c_reteiva, subtotalinquilino, ivainquilino, subtotalprop, ivaprop
		global comisioninquilino, otrosingresos, colpatria, conavi, ctabancaria, vlpapeleria, comision, iva, rtefuente
		global ivajuridico, comisioninicial, interesesmora, incremento, reteiva, porcretefuenteS, diainicioperiodo
		global numesesrenovacion, resolucion, impresora, puerto, numdiasplazo, unidcd, recibos, facturas, cheques, comprobantes
		global update
		
		#Variables
		caja = StringVar()
		canon = StringVar()
		terceros = StringVar()
		papeleria = StringVar()
		c_comision = StringVar()
		c_iva = StringVar()
		c_retefuente = StringVar()
		c_ivajuridico = StringVar()
		vlfacturainquilino = StringVar()
		intereses = StringVar()
		impuestos = StringVar()
		
		retefuenteS = StringVar()
		c_reteiva = StringVar()
		subtotalinquilino = StringVar()
		ivainquilino = StringVar()
		subtotalprop = StringVar()
		ivaprop = StringVar()
		comisioninquilino = StringVar()
		otrosingresos = StringVar()
		colpatria = StringVar()
		conavi = StringVar()
		ctabancaria = StringVar()
		
		vlpapeleria = DoubleVar()
		comision = DoubleVar()
		iva = DoubleVar()
		rtefuente = DoubleVar()
		ivajuridico = DoubleVar()
		comisioninicial = DoubleVar()
		interesesmora = DoubleVar()
		incremento = DoubleVar()
		reteiva = DoubleVar()
		porcretefuenteS = DoubleVar()

		diainicioperiodo = IntVar()
		numesesrenovacion = IntVar()
		resolucion = StringVar()
		impresora = StringVar()
		puerto = StringVar()
		numdiasplazo = IntVar()
		unidcd = StringVar()
		
		recibos = StringVar()
		facturas = StringVar()
		cheques = StringVar()
		comprobantes = StringVar()
		
		#WIDGETS
		
		#=========================== HEADER ============================
		
		self.titleL = Label(self, text="CONFIGURACIÓN", font="bold")
		self.titleL.pack(pady=20, side=TOP)
		
		#========================== WRAPPER 1 ==========================
		
		wrapper1 = Frame(self)
		wrapper1.pack(anchor=W,pady=5, padx=10)
		
		#====================== CUENTAS CONTABLES ======================
		
		lf1 = LabelFrame(wrapper1, text="Cuentas contables")
		lf1.pack(side=LEFT, padx=10, ipadx=10, ipady=10)
		
		#---------------------------------------
		
		cont1 = Frame(lf1)
		cont1.pack(side=LEFT)
		
		l = Label(cont1, text="Caja").pack(pady=5)
		l = Label(cont1, text="Canon arrendamiento").pack()
		l = Label(cont1, text="Terceros").pack()
		l = Label(cont1, text="Papelería").pack()
		l = Label(cont1, text="Comisión").pack()
		l = Label(cont1, text="IVA").pack()
		l = Label(cont1, text="Retefuente").pack()
		l = Label(cont1, text="IVA Jurídico").pack()
		l = Label(cont1, text="Valor factura arrendatario").pack()
		l = Label(cont1, text="Intereses").pack()
		l = Label(cont1, text="Impuestos asumidos").pack()
		
		#---------------------------------------
		
		cont2 = Frame(lf1)
		cont2.pack(side=LEFT)
		
		e = Entry(cont2, textvariable=caja).pack()
		e = Entry(cont2, textvariable=canon).pack()
		e = Entry(cont2, textvariable=terceros).pack()
		e = Entry(cont2, textvariable=papeleria).pack()
		e = Entry(cont2, textvariable=c_comision).pack()
		e = Entry(cont2, textvariable=c_iva).pack()
		e = Entry(cont2, textvariable=c_retefuente).pack()
		e = Entry(cont2, textvariable=c_ivajuridico).pack()
		e = Entry(cont2, textvariable=vlfacturainquilino).pack()
		e = Entry(cont2, textvariable=intereses).pack()
		e = Entry(cont2, textvariable=impuestos).pack()
	
		#---------------------------------------
		
		cont3 = Frame(lf1)
		cont3.pack(side=LEFT)
		
		l = Label(cont3, text="RteFuente_S").pack()
		l = Label(cont3, text="Rete IVA").pack()
		l = Label(cont3, text="Subtotal arrendatario").pack()
		l = Label(cont3, text="IVA arrendatario").pack()
		l = Label(cont3, text="Subtotal propietario").pack()
		l = Label(cont3, text="IVA propietario").pack()
		l = Label(cont3, text="Comisión arrendatario").pack()
		l = Label(cont3, text="Otros ingresos").pack()
		l = Label(cont3, text="Colpatria").pack()
		l = Label(cont3, text="Conavi").pack()
		l = Label(cont3, text="Cuenta Bancaria Cheques").pack()
		
		cont4 = Frame(lf1)
		cont4.pack(side=LEFT)
		
		e = Entry(cont4, textvariable=retefuenteS).pack()
		e = Entry(cont4, textvariable=c_reteiva).pack()
		e = Entry(cont4, textvariable=subtotalinquilino).pack()
		e = Entry(cont4, textvariable=ivainquilino).pack()
		e = Entry(cont4, textvariable=subtotalprop).pack()
		e = Entry(cont4, textvariable=ivaprop).pack()
		e = Entry(cont4, textvariable=comisioninquilino).pack()
		e = Entry(cont4, textvariable=otrosingresos).pack()
		e = Entry(cont4, textvariable=colpatria).pack()
		e = Entry(cont4, textvariable=conavi).pack()
		e = Entry(cont4, textvariable=ctabancaria).pack()
		
		#========================= PORCENTAJES =========================
		
		lf2 = LabelFrame(wrapper1, text="Porcentajes")
		lf2.pack(ipadx=10, ipady=10)
		
		#---------------------------------------
		
		cont5 = Frame(lf2)
		cont5.pack(side=LEFT)
		
		l = Label(cont5, text="Valor papelería").pack()
		l = Label(cont5, text="Comisión").pack()
		l = Label(cont5, text="IVA").pack()
		l = Label(cont5, text="Rete Fuente").pack()
		l = Label(cont5, text="IVA Jurídico").pack()
		l = Label(cont5, text="Comisión Inicial").pack()
		l = Label(cont5, text="Intereses Mora").pack()
		l = Label(cont5, text="Incremento").pack()
		l = Label(cont5, text="RetIVA").pack()
		l = Label(cont5, text="Porc Rte Fuente_S").pack()
		
		#---------------------------------------
		
		cont6 = Frame(lf2)
		cont6.pack(side=LEFT)
		
		e = Entry(cont6, textvariable=vlpapeleria).pack()
		e = Entry(cont6, textvariable=comision).pack()
		e = Entry(cont6, textvariable=iva).pack()
		e = Entry(cont6, textvariable=rtefuente).pack()
		e = Entry(cont6, textvariable=ivajuridico).pack()
		e = Entry(cont6, textvariable=comisioninicial).pack()
		e = Entry(cont6, textvariable=interesesmora).pack()
		e = Entry(cont6, textvariable=incremento).pack()
		e = Entry(cont6, textvariable=reteiva).pack()
		e = Entry(cont6, textvariable=porcretefuenteS).pack()
		
		#========================== WRAPPER 2 ==========================
		
		wrapper2 = Frame(self)
		wrapper2.pack(side=LEFT)
		
		#============================ OTRAS ============================
		
		lf3 = LabelFrame(wrapper2, text="Otras")
		lf3.pack(side=LEFT, padx=10, ipadx=10, ipady=10)
		
		#---------------------------------------
		
		cont7 = Frame(lf3)
		cont7.pack(side=LEFT)
		
		l = Label(cont7, text="Día Inicio Periodo").pack()
		l = Label(cont7, text="# Meses Renovación").pack()
		l = Label(cont7, text="Resolución").pack()
		l = Label(cont7, text="Impresora").pack()
		l = Label(cont7, text="Puerto").pack()
		l = Label(cont7, text="# Días Plazo").pack()
		l = Label(cont7, text="Unidad Quemador").pack()
		
		#---------------------------------------
		
		cont8 = Frame(lf3)
		cont8.pack()
		
		e = Entry(cont8, textvariable=diainicioperiodo).pack()
		e = Entry(cont8, textvariable=numesesrenovacion).pack()
		e = Entry(cont8, textvariable=resolucion).pack()
		e = Entry(cont8, textvariable=impresora).pack()
		e = Entry(cont8, textvariable=puerto).pack()
		e = Entry(cont8, textvariable=numdiasplazo).pack()
		e = Entry(cont8, textvariable=unidcd).pack()
		
		#========================= CONSECUTIVOS ========================

		lf4 = LabelFrame(wrapper2, text="Consecutivos")
		lf4.pack(ipadx=10, ipady=10)
		
		#---------------------------------------
		
		cont9 = Frame(lf4)
		cont9.pack(side=LEFT)
		
		l = Label(cont9, text="Recibos de caja").pack()
		e = Entry(cont9, textvariable=recibos).pack()
		l = Label(cont9, text="Cheques").pack()
		e = Entry(cont9, textvariable=cheques).pack()
		
		cont10 = Frame(lf4)
		cont10.pack()
		
		l = Label(cont10, text="Facturas").pack()
		e = Entry(cont10, textvariable=facturas).pack()
		l = Label(cont10, text="Comprobantes de pago").pack()
		e = Entry(cont10, textvariable=comprobantes).pack()
		
		#========================== BOTONES ============================
		
		wrapper3 = Frame(self)
		wrapper3.pack(side=RIGHT)
				
		load = Button(wrapper3, text='Cargar', width=20, bg='navy', foreground='white', activebackground='red3', activeforeground='white',command=cargar)
		load.pack()
		
		update = Button(wrapper3, text='Actualizar', width=20, bg='navy', foreground='white', activebackground='red3', activeforeground='white',command=actualizar, state=DISABLED)
		update.pack()
		
		#modify = Button(wrapper3, text='Modificar', width=20, bg='navy', foreground='white', activebackground='red3', activeforeground='white',command=modificar)
		#modify.pack()
		
		add = Button(wrapper3, text='Guardar', width=20, bg='navy', foreground='white', activebackground='red3', activeforeground='white',command=agregar)
		add.pack()

def cargar():
	#connect.commit()
	query = "SELECT * FROM configuracion;"
	cursor.execute(query)
	registros = cursor.fetchall()
	for item in registros:
		caja.set(item[1])
		canon.set(item[2])
		terceros.set(item[3])
		papeleria.set(item[4])
		c_comision.set(item[5])
		c_iva.set(item[6])
		c_retefuente.set(item[7])
		c_ivajuridico.set(item[8])
		vlfacturainquilino.set(item[9])
		intereses.set(item[10])
		impuestos.set(item[10])
		retefuenteS.set(item[12])
		c_reteiva.set(item[13])
		subtotalinquilino.set(item[14])
		ivainquilino.set(item[15])
		subtotalprop.set(item[16])
		ivaprop.set(item[17])
		comisioninquilino.set(item[18])
		otrosingresos.set(item[19])
		colpatria.set(item[20])
		conavi.set(item[21])
		ctabancaria.set(item[22])
		vlpapeleria.set(item[23])
		comision.set(item[24])
		iva.set(item[25])
		rtefuente.set(item[26])
		ivajuridico.set(item[27])
		comisioninicial.set(item[28])
		interesesmora.set(item[29])
		incremento.set(item[30])
		reteiva.set(item[31])
		porcretefuenteS.set(item[32])
		diainicioperiodo.set(item[33])
		numesesrenovacion.set(item[34])
		resolucion.set(item[35])
		impresora.set(item[36])
		puerto.set(item[37])
		numdiasplazo.set(item[38])
		unidcd.set(item[39])
		recibos.set(item[40])
		facturas.set(item[41])
		cheques.set(item[42])
		comprobantes.set(item[43])
	update.configure(state="normal")
	
def agregar():
	try:
		v1 = caja.get()
		v2 = canon.get()
		v3 = terceros.get()
		v4 = papeleria.get()
		v5 = c_comision.get()
		v6 = c_iva.get()
		v7 = c_retefuente.get()
		v8 = c_ivajuridico.get()
		v9 = vlfacturainquilino.get()
		v10 = intereses.get()
		v11 = impuestos.get()
	
		v12 = retefuenteS.get()
		v13 = c_reteiva.get()
		v14 = subtotalinquilino.get()
		v15 = ivainquilino.get()
		v16 = subtotalprop.get()
		v17 = ivaprop.get()
		v18 = comisioninquilino.get()
		v19 = otrosingresos.get()
		v20 = colpatria.get()
		v21 = conavi.get()
		v22 = ctabancaria.get()
		
		v23 = vlpapeleria.get()
		v24 = comision.get()
		v25 = iva.get()
		v26 = rtefuente.get()
		v27 = ivajuridico.get()
		v28 = comisioninicial.get()
		v29 = interesesmora.get()
		v30 = incremento.get()
		v31 = reteiva.get()
		v32 = porcretefuenteS.get()
		
		v33 = diainicioperiodo.get()
		v34 = numesesrenovacion.get()
		v35 = resolucion.get()
		v36 = impresora.get()
		v37 = puerto.get()
		v38 = numdiasplazo.get()
		v39 = unidcd.get()
	
		v40 = recibos.get()
		v41 = facturas.get()
		v42 = cheques.get()
		v43 = comprobantes.get()
		
		connect.commit()
		sql = "INSERT INTO configuracion (cod_caja, cod_canon, cod_terceros, cod_papeleria, cod_comision, cod_iva, cod_retefuente, cod_ivajuridico, cod_vlfactura, cod_intereses, cod_impuestos, cod_rtefuenteS, cod_reteiva, cod_subtotalarrend, cod_ivaarrend, cod_subtototalprop, cod_ivaprop, cod_comiarrend, cod_otrosingresos, cod_colpatria, cod_conavi, cod_ctabancaria, vlpapeleria, comision, iva, retefuente, ivajuridico, comisionini, interesesmora, incremento, rteiva, porc_retefuenteS, diainiperio, numesesrenova, resolucion, impresora, puerto, numdiasplazo, unitcd, recibos, facturas, cheques, comprobantes) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%d','%d','%s','%s','%s','%d','%s','%s','%s','%s','%s');" % (v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40, v41, v42, v43)
		cursor.execute(sql)
		showinfo ("Mensaje", "Datos guardados")
	except MySQLdb.OperationalError:
		showerror('Mensaje', "Error al guardar los datos en la DB!!!")
		
def modificar():
	pass
	
def actualizar():
	v1 = caja.get()
	v2 = canon.get()
	v3 = terceros.get()
	v4 = papeleria.get()
	v5 = c_comision.get()
	v6 = c_iva.get()
	v7 = c_retefuente.get()
	v8 = c_ivajuridico.get()
	v9 = vlfacturainquilino.get()
	v10 = intereses.get()
	v11 = impuestos.get()
	
	v12 = retefuenteS.get()
	v13 = c_reteiva.get()
	v14 = subtotalinquilino.get()
	v15 = ivainquilino.get()
	v16 = subtotalprop.get()
	v17 = ivaprop.get()
	v18 = comisioninquilino.get()
	v19 = otrosingresos.get()
	v20 = colpatria.get()
	v21 = conavi.get()
	v22 = ctabancaria.get()
	
	v23 = vlpapeleria.get()
	v24 = comision.get()
	v25 = iva.get()
	v26 = rtefuente.get()
	v27 = ivajuridico.get()
	v28 = comisioninicial.get()
	v29 = interesesmora.get()
	v30 = incremento.get()
	v31 = reteiva.get()
	v32 = porcretefuenteS.get()
		
	v33 = diainicioperiodo.get()
	v34 = numesesrenovacion.get()
	v35 = resolucion.get()
	v36 = impresora.get()
	v37 = puerto.get()
	v38 = numdiasplazo.get()
	v39 = unidcd.get()
	
	v40 = recibos.get()
	v41 = facturas.get()
	v42 = cheques.get()
	v43 = comprobantes.get()
	
	if askyesno("Salir", "¿Desea modificar esta información?"):
		connect.commit()
		sql = "UPDATE configuracion SET cod_caja='%s', cod_canon='%s', cod_terceros='%s', cod_papeleria='%s', cod_comision='%s', cod_iva='%s', cod_retefuente='%s', cod_ivajuridico='%s', cod_vlfactura='%s', cod_intereses='%s', cod_impuestos='%s', cod_rtefuenteS='%s', cod_reteiva='%s', cod_subtotalarrend='%s', cod_ivaarrend='%s', cod_subtototalprop='%s', cod_ivaprop='%s', cod_comiarrend='%s', cod_otrosingresos='%s', cod_colpatria='%s', cod_conavi='%s', cod_ctabancaria='%s', vlpapeleria='%f', comision='%f', iva='%f', retefuente='%f', ivajuridico='%f', comisionini='%f', interesesmora='%f', incremento='%f', rteiva='%f', porc_retefuenteS='%f', diainiperio='%d', numesesrenova='%d', resolucion='%s', impresora='%s', puerto='%s', numdiasplazo='%d', unitcd='%s', recibos='%s', facturas='%s', cheques'%s', comprobantes='%s');" % (v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22, v23, v24, v25, v26, v27, v28, v29, v30, v31, v32, v33, v34, v35, v36, v37, v38, v39, v40, v41, v42, v43)	
		cursor.execute(sql)
		showinfo ("Mensaje", "Datos actualizados!")
	
