#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from tkMessageBox import*
import MySQLdb
import ConnInfo

class mySQL():
	# class variable
	SBIENES = 'sbienes'
	
	#------------------------------------------------------
	def conexion(self):
		# connect by unpacking dictionary credentials
		conn = MySQLdb.connect(**dbConfig)
		print(conn) #showinfo("", "Conectado a %s" % conn)
		# create cursor
		cursor = conn.cursor()
		return conn, cursor
	#------------------------------------------------------
	def close(self, cursor, conn):
		# close cursor
		conn.close()
	#------------------------------------------------------
	def showDBs(self):
		# connect to MySQL
		conn, cursor = self.connect()
		# execute command
		cursor.execute("SHOW DATABASES")
		print(cursor.fetchall())
		# close connection to MySQL
		conn.close()
	#------------------------------------------------------
	def createGuiDB(self):
		# connect to MySQL
		conn, cursor = self.connect()
		try:
			cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".
			format(GUIDB))
		except mysql.Error as err:
				print("Failed to create DB: {}".format(err))
	#------------------------------------------------------
	def dropGuiDB(self):
		# connect to MySQL
		conn, cursor = self.connect()
	#------------------------------------------------------
	def useGuiDB(self, cursor):
		'''Expects open connection.'''
		# select DB
		cursor.execute("USE guidb")
	#------------------------------------------------------
	def createTables(self):
		# connect to MySQL
		conn, cursor = self.connect()
		# create Table inside DB
		cursor.execute("CREATE TABLE Books (		\
			Book_ID INT NOT NULL AUTO_INCREMENT,	\
			Book_Title VARCHAR(25) NOT NULL,		\
			Book_Page INT NOT NULL,					\
			PRIMARY KEY (Book_ID)					\
			) ENGINE=InnoDB")
	#------------------------------------------------------
	def dropTables(self):
		# connect to MySQL
		conn, cursor = self.connect()
	#------------------------------------------------------
	def showTables(self):
		# connect to MySQL
		conn, cursor = self.connect()
		# execute command
		cursor.execute("SHOW TABLES FROM GuiDB")
		print(cursor.fetchall())
	#------------------------------------------------------
	def insertBooks(self, title, page, bookQuote):
		# connect to MySQL
		conn, cursor = self.connect()
		# insert data
	#------------------------------------------------------
	def insertBooksExample(self):
		# connect to MySQL
		conn, cursor = self.connect()
		# insert hard-coded data
	#------------------------------------------------------
	def showBooks(self):
		# connect to MySQL
		conn, cursor = self.connect()
	#------------------------------------------------------
	def showColumns(self):
		# connect to MySQL
		conn, cursor = self.connect()
	#------------------------------------------------------
	def showData(self):
		# connect to MySQL
		conn, cursor = self.connect()
	#------------------------------------------------------
	def Agregar(self):
		# connect to MySQL
		conn, cursor = self.connect()
		# insert data
		cc = cedula.get()
		ref = titulo.get()
		fi = ingreso.get()
		rs = rsocial.get()
		loc1 = residencia.get()
		n = nombres.get()
		a = apellidos.get()
		loc2 = direccion.get()
		tel1 = telefono.get()
		of = oficina.get()
		tel2 = tel.get()
		fax = telfax.get()
		email = correo.get()
		anio = 0
		y = anio
		m = mes.get()
		if m == 'Enero':
			m = 1
		if m == 'Febrero':
			m = 2
		if m == 'Marzo':
			m = 3
		if m == 'Abril':
			m = 4
		if m == 'Mayo':
			m = 5
		if m == 'Junio':
			m = 6
		if m == 'Julio':
			m = 7
		if m == 'Agosto':
			m = 8
		if m == 'Septiembre':
			m = 9
		if m == 'Octubre':
			m = 10
		if m == 'Noviembre':
			m = 11
		if m == 'Diciembre':
			m = 12
		d = dia.get()
		cumple = "%d-%d-%s" %(y,m,d)
		e = envio.get()
		cel = celular.get()
		tp = tipopersona.get()
		c = comision.get()
		rf = retefuente.get()
		ri = reteiva.get()
		gc = gcontribuyente.get()
		gf = gfactura.get()
		gch =gcheque.get()
		o = note.get("1.0",END)
		
		rcc = reprecc.get()
		rn = reprenombres.get()
		rd = repredireccion.get()
		rt1 = repretelefono.get()
		ro = repreoficina.get()
		rt2 = repretel.get()
		rb = reprebanco.get()
		rtc = repretcuenta.get()
		rnc = reprenumcuenta.get()
		
		t1cc = tit1cc.get()
		t1n = tit1nombres.get()
		t1b = tit1banco.get()
		t1tc = tit1tcuenta.get()
		t1nc = tit1numcuenta.get()
		
		t2cc = tit1cc.get()
		t2n = tit1nombres.get()
		t2b = tit1banco.get()
		t2tc = tit1tcuenta.get()
		t2nc = tit1numcuenta.get()
		
		conexion.commit()
		sql = "INSERT INTO propietarios (p_cc, p_titulo, p_ingreso, p_rsocial, p_reside, p_nombres, p_apellidos, p_direccion, p_telefono, p_oficina, p_tel, p_fax, p_email, p_dia, p_mes, p_cumple, p_envio, p_celular, p_tpersona, p_comision, p_retefuente, p_reteiva, p_contribuyente, p_gfactura, p_gcheque, p_nota, cc_represent, nombres_represent, dir_represent, tel_represent, oficina_represent, telofi_represent, banco_represent, tcuenta_represent, numcuenta_represent, cc_titular1, nombres_titular1, banco_titular1, tcuenta_titular1, numcuenta_titular1, cc_titular2, nombres_titular2, banco_titular2, tcuenta_titular2, numcuenta_titular2) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%s', '%s', '%s', '%s', '%d', '%f', '%d', '%d', '%d', '%d', '%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (cc, ref, fi, rs, loc1, n, a, loc2, tel1, of, tel2, fax, email, d, m, cumple, e, cel, tp, c, rf, ri, gc, gf, gch, o, rcc, rn, rd, rt1, ro, rt2, rb, rtc, rnc, t1cc, t1n, t1b, t1tc, t1nc, t2cc, t2n, t2b, t2tc, t2nc)
		cursor.execute(sql)
		showinfo ("Mensaje", "Datos guardados")
		cedula.set("")
		titulo.set("")
		ingreso.set("")
		rsocial.set("")
		residencia.set("")
		nombres.set("")
		apellidos.set("")
		direccion.set("")
		telefono.set("")
		oficina.set("")
		tel.set("")
		telfax.set("")
		correo.set("")
		mes.set("")
		dia.set("")
		envio.set("")
		celular.set("")
		tipopersona.set(0)
		comision.set(0)
		retefuente.set(0)
		reteiva.set(0)
		gcontribuyente.set(0)
		gfactura.set(0)
		gcheque.set(0)
		note.delete('1.0', '2.0')
		
		reprecc.set("")
		reprenombres.set("")
		repredireccion.set("")
		repretelefono.set("")
		repreoficina.set("")
		repretel.set("")
		reprebanco.set("")
		repretcuenta.set("")
		reprenumcuenta.set("")
		
		tit1cc.set("")
		tit1nombres.set("")
		tit1banco.set("")
		tit1tcuenta.set("")
		tit1numcuenta.set("")
		
		tit2cc.set("")
		tit2nombres.set("")
		tit2banco.set("")
		tit2tcuenta.set("")
		tit2numcuenta.set("")
#------------------------------------------------------
if __name__ == '__main__':
	# Create class instance
	mySQL = mySQL()
