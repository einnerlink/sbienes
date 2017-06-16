#!/usr/bin/python
#-*- coding:utf-8 -*-
from Tkinter import*
from ttk import Combobox, Treeview
from tkMessageBox import*
import MySQLdb
from controller import *

class RelacionIP(Frame):
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)

                global cbox, inmueble, loc, nit, nombre, carpeta, grupo, porcentaje, tree, busqueda
                global e1, e2, nitE
                
                lupa = PhotoImage(file='img/lupa.png')
                
                inmueble = IntVar()
                loc = StringVar()
                nit = StringVar()
                nombre = StringVar()
                carpeta = IntVar()
                grupo = IntVar()
                porcentaje = DoubleVar()

                lupa = PhotoImage(file='img/lupa.png')
                
                #BUSQUEDA = ["Nombre","CC/Nit"]
                busqueda = StringVar()
                #busqueda.trace("w", lambda name, index, mode: buscar())
                dato = StringVar()
                
                #WIDGETS
                
                #=========================== HEADER ============================
                
                self.titleL = Label(self, text="RELACIÓN INMUEBLES/PROPIETARIO", font="bold")
                self.titleL.pack(pady=20, side=TOP)
                
                #=========================== WRAPPER ===========================
                
                self.wrapper = Frame (self)
                self.wrapper.pack(side=TOP, fill=Y)
                
                self.f = Frame(self.wrapper)
                self.f.pack(pady=5, fill=X)#-----------------------------------

                l1 = Label(self.f, text='Inmueble:')
                l1.pack(side=LEFT)
                
                e1 = Entry (self.f, textvariable=inmueble)
                e1.pack(side=LEFT)
                e1.bind('<Return>', buscarI)

                b1 = Button (self.f, text="Buscar", image=lupa, command=topInmueble)
                b1.image=lupa
                b1.pack(side=LEFT)
                
                self.f0 = Frame(self.wrapper)
                self.f0.pack(pady=5, fill=X)#-----------------------------------
                
                l2 = Label (self.f0, text="Dirección: ")
                l2.pack(side=LEFT)
                
                e2 = Entry (self.f0, textvariable=loc, width=90, state=DISABLED)
                e2.pack(side=LEFT, fill=X, expand=1)
                
                self.f1 = Frame(self.wrapper)
                self.f1.pack(pady=5, fill=X)#-----------------------------------
                
                self.nit = Label (self.f1, text="CC/Nit")
                self.nit.pack(side=LEFT)
                
                nitE = Entry (self.f1, textvariable=nit)
                nitE.pack(side=LEFT)
                nitE.bind('<Return>', buscarP)
                
                self.add = Button (self.f1, text="Buscar", image=lupa, command=topPropietario)
                self.add.pack(side=LEFT)
                
                self.f2 = Frame(self.wrapper)
                self.f2.pack(pady=5, fill=X)#-----------------------------------
                
                self.nombre = Label (self.f2, text="Nombre: ")
                self.nombre.pack(side=LEFT)
                self.nombreE = Entry (self.f2, textvariable=nombre, width=90, state=DISABLED)
                self.nombreE.pack(side=LEFT, fill=X, expand=1)
                
                self.f3 = Frame(self.wrapper)
                self.f3.pack(pady=5, fill=X)#-----------------------------------
                
                self.carpeta = Label (self.f3, text="Carpeta: ")
                self.carpeta.pack(side=LEFT)
                self.carpetaE = Entry (self.f3, textvariable=carpeta, width=5)
                self.carpetaE.pack(side=LEFT)
                carpeta.set(1)
                
                self.grupo = Label (self.f3, text="Grupo: ")
                self.grupo.pack(side=LEFT)
                self.grupoE = Entry (self.f3, textvariable=grupo, width=5)
                self.grupoE.pack(side=LEFT)
                grupo.set(1)
                
                self.porcentaje = Label (self.f3, text="Porcentaje: ")
                self.porcentaje.pack(side=LEFT)
                self.porcentajE = Entry (self.f3, textvariable=porcentaje, width=5)
                self.porcentajE.pack(side=LEFT)
                
                self.chkb0 = Checkbutton(self.f3, text="Representante")
                self.chkb0.pack(side=LEFT)
                
                self.update = Button (self.f3, text="Cargar", bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=cargar)
                self.update.pack(side=RIGHT)
                
                self.add = Button (self.f3, text="Agregar", bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=agregar)
                self.add.pack(side=RIGHT)
                
                self.f4 = Frame(self.wrapper)
                self.f4.pack(pady=5, fill=X)#-----------------------------------
                
                tree = Treeview(self.f4, show="headings", columns=('col1','col2','col3','col4','col5','col6'))
                tree.pack(side=LEFT, fill=X, expand=1)
                
                tree.column('col1', width=5, anchor='center')
                tree.column('col2', width=150, anchor='center')
                tree.column('col3', width=5, anchor='center')
                tree.column('col4', width=150, anchor='center')
                tree.column('col5', width=1, anchor='center')
                tree.column('col6', width=1, anchor='center')
                
                tree.heading('col1', text='Cod')
                tree.heading('col2', text='Imnueble')
                tree.heading('col3', text='CC/nit')
                tree.heading('col4', text='Dueño')
                tree.heading('col5', text='Grupo')
                tree.heading('col6', text='%')
                
                self.scroll = Scrollbar(self.f4,orient=VERTICAL,command=tree.yview)
                tree.configure(yscrollcommand=self.scroll.set)
                
                """
        #EJEMPLO 2 SÍ FUNCIONA (0)
                self.tree = Treeview(self.f4, height=5, columns=2)
                self.tree.pack()
                self.tree.heading('#0', text='CC/Nit', anchor=W)
                self.tree.heading(2, text='Nombre', anchor=W)"""
                
                self.f5 = Frame(self.wrapper)
                self.f5.pack(pady=5, fill=X)#-----------------------------------
                
                self.delete = Button (self.f5, text="Eliminar", bg='navy', foreground='white', activebackground='red3', activeforeground='white', command=borrar)
                self.delete.pack(side=RIGHT)
                
                e3 = Entry(self.f5, textvariable=busqueda)
                e3.pack(side=LEFT)
                #e3.bind("<KeyRelease>", caps)
                
                b3 = Button(self.f5, text='BUSCAR', image=lupa, command=buscar)
                b3.image = lupa
                b3.pack(side=LEFT)

def buscarI(event):
        connect.commit()
        try:
                i = inmueble.get()
                sql = "SELECT i_dir FROM inmuebles WHERE i_cod='%d'" % (i)
                cursor.execute(sql)
                connect.commit()
                dato = cursor.fetchone()
                for l in dato:
                        loc.set(l)

        except TypeError, e:
                showerror("Error", e)
                e1.focus()
                inmueble.set(0)
                loc.set("")
                
        except MySQLdb.IntegrityError, e:
                showerror("Error", e)
                e1.focus()
                inmueble.set(0)
                loc.set("")
                
        except:
                showerror("Error", "No existe ese código.")
                e1.focus()
                inmueble.set(0)
                loc.set("")

def topInmueble():
        global topB, topB_scroll, topB_lb
        
        topB = Toplevel()
        topB.title("Inmuebles")
        topB.geometry("300x300")
        
        topB.wm_attributes("-topmost", 1)#Inabilitar este en WIN
        topB.focus_set()#Mantiene el toplevel sobre root/w
        topB.transient() #Se minimiza solo cuando root lo hace
        topB.grab_set() #Impite que se interactue con la ventana root/w
                        
        topB_scroll = Scrollbar(topB, orient=VERTICAL)
        topB_scroll.pack(side=RIGHT, fill=Y)
        topB_lb = Listbox(topB, yscrollcommand=topB_scroll.set, height=20, width=20)
        topB_scroll.config (command=topB_lb.yview)
        topB_lb.pack(fill=BOTH)
        topB_lb.bind("<Double-Button-1>", cargarInmueble)
        
        try:
                connect.commit()
                display = "SELECT i_cod FROM inmuebles;"
                cursor.execute(display)
                registros = cursor.fetchall()
                topB_lb.delete(0, END)
                for item in registros:
                        codigos = item[0]
                        topB_lb.insert(END, codigos)

        except TypeError, e:
                showerror("Error al cargar los inmuebles", e)
                
        except MySQLdb.IntegrityError, e:
                showerror("Error", e)

def cargarInmueble(event):
        i = topB_lb.curselection()[0]
        val = topB_lb.get(i)
        connect.commit()
        edit = "SELECT i_cod, i_dir FROM inmuebles WHERE i_cod=('%s');" % (val)
        cursor.execute(edit)
        sol = cursor.fetchall()
        for item in sol:
                d1 = item[0] #i_cod
                d2 = item[1] #i_dir
                inmueble.set(d1)
                loc.set(d2)
        topB.destroy()
                
def buscarP(event):
        connect.commit()
        try:
                n = nit.get()
                search = "SELECT p_nombres, p_apellidos FROM propietarios WHERE p_cc='%s';" % (n)
                cursor.execute(search)
                connect.commit()
                dato = cursor.fetchall()
                for n, a in dato:
                        v = n + " " + a
                        nombre.set(v)

        except TypeError, e:
                showerror("Error", e)
                nitE.focus()
                nit.set(0)
                nombre.set("")
                
        except MySQLdb.IntegrityError, e:
                showerror("Error", e)
                nitE.focus()
                nit.set(0)
                nombre.set("")
                
        except:
                showerror("Error", "La Cédula o Nit no figura en la base de datos!")
                nitE.focus()
                nit.set(0)
                nombre.set("")

def topPropietario():
        global topB, topB_scroll, topB_lb
        
        topB = Toplevel()
        topB.title("Propietarios")
        topB.geometry("300x300")
        
        topB.wm_attributes("-topmost", 1)#Inabilitar este en WIN
        topB.focus_set()#Mantiene el toplevel sobre root/w
        topB.transient() #Se minimiza solo cuando root lo hace
        topB.grab_set() #Impite que se interactue con la ventana root/w
                        
        topB_scroll = Scrollbar(topB, orient=VERTICAL)
        topB_scroll.pack(side=RIGHT, fill=Y)
        topB_lb = Listbox(topB, yscrollcommand=topB_scroll.set, height=20, width=20)
        topB_scroll.config (command=topB_lb.yview)
        topB_lb.pack(fill=BOTH)
        topB_lb.bind("<Double-Button-1>", cargarPropietario)
        
        try:
                connect.commit()
                display = "SELECT p_nombres FROM propietarios;"
                cursor.execute(display)
                registros = cursor.fetchall()
                topB_lb.delete(0, END)
                for item in registros:
                        nombre = item[0]
                        topB_lb.insert(END, nombre)

        except TypeError, e:
                showerror("Error al cargar los propietarios", e)
                
        except MySQLdb.IntegrityError, e:
                showerror("Error", e)

def cargarPropietario(event):
        i = topB_lb.curselection()[0]
        val = topB_lb.get(i)
        connect.commit()
        edit = "SELECT p_nombres, p_apellidos, p_cc FROM propietarios WHERE p_nombres='%s';" % (val)
        cursor.execute(edit)
        sol = cursor.fetchall()
        for n, a, c in sol:
                v = n + " " + a
                nombre.set(v)
                nit.set(c)
                
        topB.destroy()
        
def agregar():
        connect.commit()
        try:
                v0 = inmueble.get()
                v1 = loc.get()
                v2 = nit.get()
                v3 = nombre.get()
                v4 = carpeta.get()
                v5 = grupo.get()
                v6 = porcentaje.get()
                sql = "INSERT INTO relacionip (i_cod, inmueble, p_cc, dueño, r_carpeta, r_grupo, r_porcent) VALUES ('%d', '%s', '%s', '%s', '%d', '%d', '%f');" % (v0, v1, v2, v3, v4, v5, v6)
                cursor.execute(sql)
                showinfo ("Mensaje", "Relación agregada!")
                inmueble.set("")
                nit.set("")
                nombre.set("")
                grupo.set("")
                porcentaje.set("")
                cargar()
        except MySQLdb.IntegrityError:
                showerror ("Mensaje", "La dirección del inmueble no existe o está mal escrita!")

def cargar():
        try:
                connect.commit()
                tv = "SELECT i_cod, inmueble, p_cc, dueño, r_grupo, r_porcent FROM relacionip order by dueño;"
                cursor.execute(tv)
                results = cursor.fetchall()
                #tree.delete()
                tree.delete(*tree.get_children())
                for row in results:
                        tree.insert('', END, values=(row[0],row[1],row[2],row[3],row[4],row[5]))
        except:
                showerror ("Mensaje", "Error en la carga del Treeview!")

def borrar():
        try:
                connect.commit()
                i = tree.selection()[0] #'[0]'puede o no ser necesario
                value = tree.item(i, 'values')[0] #0=cc, 1=nombre, 2=dir
                delete = """DELETE FROM relacionip WHERE i_cod=("%s");""" % (value)
                cursor.execute(delete)
                connect.commit()
                showinfo("mensaje", "Relación borrada!")
                cargar()
        except MySQLdb.IntegrityError:
                showerror ('Mensaje', "No se puede borrar o actualizar porque hace parte de una relación.")
                
# CONVIERTE LA ENTRADA DE LOS ENTRIES EN MAYÚSCULA
def caps(event):
        pass
        
def buscar():
        v = busqueda.get()
        children = tree.get_children() #OBTIENE LOS iid DE LOS ITEMS
        for child in children:
                i = tree.item(child, 'values')[0]
                if v == i:
                        tree.selection_set(child)
                        showinfo("Mensaje", "Dato encontrado!")
                else:
                        pass

