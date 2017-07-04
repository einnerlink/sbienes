'''
PARA REALIZAR EL LOGIN
'''
import MySQLdb

def Conexion(u, p):
	conexion = MySQLdb.connect (host = "localhost", 
					user = "%s" % (u),
					passwd = "%s" % (p),
					db = "database")
	cursor = conexion.cursor ()
