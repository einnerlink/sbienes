#!/usr/bin/python
import MySQLdb

#CONFIGURAR AQUI#
server='localhost' #Servidor MySQL
user='root'        #Usuario MySQL
passwd='Gsus5@v3s'      #Passwd MySQL
bd='superbienes_db'     #Nombre de Base de Datos

def agregar(server,user,passwd,bd):
    db = MySQLdb.connect(server,user,passwd,bd)
    cursor = db.cursor()
    name = raw_input('[+]Nombre: ')
    telefono = raw_input('[+]Telefono: ')
    cursor.execute("insert into contactos (nombre,telefono) values ('%s','%s')"%(name,telefono))
    print 'Datos agregados correctamente...'
    cursor.fetchall()
    cursor.close()
    run()
def ver (server,user,passwd,bd):
    try:
        db = MySQLdb.connect(server,user,passwd,bd)
        ztux = db.cursor()
        ztux.execute("select * from %s "%(bd))
        a = ztux.fetchall()
        for i in a:
            print i
        ztux.close()
        run()
    except:
        print '[*]Error al conectarse a la base de Datos...'
        run()
    
def buscar(server,user,passwd,bd):
    try:
        db = MySQLdb.connect(server,user,passwd,bd)
        buscar = raw_input('[+]Nombre del contacto: ')
        ztux = db.cursor()
        ztux.execute("select * from %s where nombre='%s'"%(bd,buscar))
        a = ztux.fetchall()
        print a
        ztux.close()
        run()
    except:
        print '[*]Error al conectarse a la base de Datos...'
        run()
        
def editar(server,user,passwd,bd):
    try:
        db = MySQLdb.connect(server,user,passwd,bd)
        print '[1]Nombre\n[2]Telefono'
        opc =raw_input('Que desas editar: ')
        if opc=='1':
            editar = raw_input('[+]Nombre del contacto a editar: ')
            cambiar = raw_input('[+]Escribe el nombre del nuevo contacto: ')
            ztux = db.cursor()
            ztux.execute("update %s set nombre='%s' where nombre='%s'"%(bd,cambiar,editar))
            ztux.close()
            run()
        elif opc=='2':
            editar = raw_input('[+]Nombre del contacto a editar: ')
            cambiar = raw_input('[+]Escribe el nuevo numero del contacto: ')
            ztux = db.cursor()
            ztux.execute("update %s set telefono='%s' where nombre='%s'"%(bd,cambiar,editar))
            ztux.close()
            print 'Contacto Actualizado...'
            run()
        else:
            print 'Opcion Incorrecta...'
            run()
            
    except:
        print '[*]Error al conectar a la base de Datos...'
        run()

def borrar(server,user,passwd,bd):
    try:
        db = MySQLdb.connect(server,user,passwd,bd)
        borrar = raw_input('[+]Nombre del contacto: ')
        ztux = db.cursor()
        ztux.execute("delete from %s where nombre='%s'"%(bd,borrar))
        ztux.close()
        print '[+]Contacto borrado con exito...'
        run()
    except:
        print '[*]Error al conectar a la base de Datos...'
