#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
SBIENES
Created on Feb 29, 2016
@author: einnerlink
'''
from Tkinter import*
from ttk import*
import time
import sys
#reload(sys)  
#sys.setdefaultencoding('Cp1252')
from tkMessageBox import*
import MySQLdb
from mod import conexion #Conexion: para el login
from mod import inicio #Inicio
from mod import propietarios #Propietarios
from mod import arrendatarios #Arrendatarios
from mod import terceros #Terceros
from mod import inmuebles #Inmuebles
from mod import cuentas_contables #CuentasContables
from mod import relacionip #RelacionIP
from mod import factura_inquilino #FacturaInquilino
from mod import factura_propietario #FacturaProp
from mod import proceso_fact_auto_arre #
from mod import proceso_fact_auto_prop #
from mod import analisis_arrendatarios #AnalisisArre
from mod import analisis_propietarios #AnalisisProp
from mod import reajustes_propietario #ReajustesProp
from mod import reporte_propietario #Reporteprop
from mod import concepto_gastos #ConceptoGastos
from mod import gastos #Gastos
from mod import beneficiarios #Beneficiarios
from mod import acerca #Acerca
from mod import contratos #Contratos
from mod import recibo_caja #ReciboCaja
from mod import admindocs #Admindocs
from mod import config #Config
from mod import seleccionar_color
from mod import export_db #exportDB
from mod import export_csv #exportCSV

def aviso():
        showerror ('Mensaje', "En construcción")
        
def salir():
                if askokcancel("Salir", "¿Desea salir del programa?"):
                        #cursor.close()
                        sys.exit (1)
                        
class Gui(Tk):
        def __init__(self):
                Tk.__init__(self)
                fav = PhotoImage(file='img/favicon.gif')
                self.call('wm', 'iconphoto', self._w, fav)
                self.login()
        
        def icowin(self):
                self.icon = PhotoImage(file='img/favicon.gif')
                self.tk.call('wm', 'iconphoto', self._w, self.icon)
                
        def login(self):
                self.title("Login")
                self.grid_rowconfigure(0,weight=1)
                self.grid_columnconfigure(0,weight=1)
                
                #widgets
                lf = LabelFrame(self, text="Login")
                l1 = Label(lf, text="Usuario:")
                self.e1 = Entry(lf, width=18)
                self.e1.focus_set()
                l2 = Label(lf, text="Contraseña:")
                self.e2 = Entry(lf, width=18, show="*")
                b1= Button(lf, text="Acceder", command = self.dbconnexion)
                
                # distribución
                lf.grid(padx=10, pady=10, row=1, column=1)
                l1.grid(row=0, column=1)
                self.e1.grid(row=0, column=2, padx=10)
                l2.grid(row=1, column=1)
                self.e2.grid(row=1, column=2, padx=10)
                b1.grid(row=4, column=2, pady=8)
                
        def interfaz(self):
                #Linux
                """self.win=Toplevel(self)
                self.win.wm_title("Superbienes SAS")
                self.win.protocol("WM_DELETE_WINDOW", salir)
                self.win.wm_attributes("-zoomed", "1")#Esto es para maximizar el toplevel
                self.win.config(bg="beige")#Le da color al fondo"""
                
                #Windows
                self.win=Toplevel(self)
                self.win.wm_title("Superbienes SAS")
                self.win.protocol("WM_DELETE_WINDOW", salir)
                self.win.wm_state(newstate="zoomed")
                
                #========================= CONTENEDOR =========================
                
                self.container = Frame(self.win)
                self.container.pack(side='top')
                
                #======================== BARRA DE MENU ========================
                
                #Frame que contienes las opciones de menu
                barramenu = Menu(self.container, bg='navy', foreground='white')
                
                #PRIMER MENU: Archivo-------------------------------------------
                #Submenus: Abrir, Nuevo, Guardar, Cerrar
                
                menuArchivo = Menu(barramenu, tearoff=0, background='#000099', foreground='white', activebackground='red3', activeforeground='white')
                
                menuArchivo.add_command(label="Abrir", command=aviso, state=DISABLED)
                
                menuArchivo.add_command (label="Nuevo", command=aviso, state=DISABLED)
                
                menuArchivo.add_command (label="Guardar", command=aviso, state=DISABLED)
                
                menuArchivo.add_separator()#----------------------------
                
                menuArchivo.add_command (label="Cerrar", command=salir)
                
                barramenu.add_cascade(label="Archivo", menu=menuArchivo)#Ver Submenu

                #SEGUNDO MENU: Gestion------------------------------------------
                #Submenus: Propietarios, Inquilinos, Inmuebles, relaciones, etc.
                
                menuMaestros = Menu(barramenu, tearoff=0, background='#000099', foreground='white', activebackground='red3', activeforeground='white')
                
                menuMaestros.add_command(label='Propietarios', command=lambda:
                                                        self.show_frame(propietarios.Propietarios))
                
                #menuMaestros.add_command(label='Propietarios', accelerator='Ctrl+P', command=lambda:
                #                                       self.show_frame(propietarios.Propietarios))
                #prop_text.bind('Control-p', lambda:self.show_frame(propietarios.Propietarios))
                
                menuMaestros.add_command (label="Arrendatarios", command=lambda:
                                                        self.show_frame(arrendatarios.Arrendatarios))
                menuMaestros.add_command (label="Terceros", command=lambda:
                                                        self.show_frame(terceros.Terceros))
                menuMaestros.add_command (label="Inmuebles", command=lambda:
                                                        self.show_frame(inmuebles.Inmuebles))
                menuMaestros.add_separator()#----------------------------
                
                menuMaestros.add_command (label="Cuentas Contables", command=lambda:
                                                        self.show_frame(cuentas_contables.CuentasContables))
                menuMaestros.add_separator()#----------------------------
                
                menuMaestros.add_command (label="Relación Inmuebles/Propietario", command=lambda:
                                                        self.show_frame(relacionip.RelacionIP))
                menuMaestros.add_command (label="Relación de Inmuebles", command=aviso, state=DISABLED)
                
                barramenu.add_cascade(label='Maestros', menu=menuMaestros)#Ver Submenu

                #TERCER MENU: Tesoreria-----------------------------------------
                #Submenus: Facturas, Egresos, Contratos, etc.
                
                menuTesoreria = Menu(barramenu, tearoff=0, background='#000099', foreground='white', activebackground='red3', activeforeground='white')
                
                                #SUBMENU Tesoreria: ------------------------------------
                
                submenu = Menu(menuTesoreria, tearoff=0, background='#000099', foreground='white', activebackground='red3', activeforeground='white')
                                
                submenu.add_command(label="Generar Factura Individual Arrendatario", command=lambda:
                                                                                                                        self.show_frame(factura_inquilino.FacturaInquilino))
                submenu.add_command(label="Generar Factura Individual Propietario", command=lambda:
                                                                                                                        self.show_frame(factura_propietario.FacturaProp))                                                                                                                       
                submenu.add_separator()#----------------------------
                                
                submenu.add_command(label="Proceso de Facturación Automático Arrendatario", command=lambda:
                                                                                                                        self.show_frame(proceso_fact_auto_arre.Proceso_Fact_Auto_Arre))
                submenu.add_command(label="Proceso de Facturación Automático Propietario", command=lambda:
                                                                                                                        self.show_frame(proceso_fact_auto_prop.Proceso_Fact_Auto_Prop))                                                                                                                 
                submenu.add_separator()#----------------------------
                
                submenu.add_command(label="Analisis de Facturación Arrendatario", command=lambda:
                                                                                                                        self.show_frame(analisis_arrendatarios.pdf_analisis_arre()))
                submenu.add_command(label="Analisis de Facturación Propietario", command=lambda:
                                                                                                                        self.show_frame(analisis_propietarios.AnalisisProp))            
                submenu.add_separator()#----------------------------
                
                submenu.add_command(label="Reajustes a Propietarios", command=lambda:
                                                                                                                        self.show_frame(reajustes_propietario.ReajustesProp))
                
                menuTesoreria.add_cascade(label='Facturación', menu=submenu)#Ver Submenu
                
                #---------------------------
                
                        #SUBMENU Egresos: ------------------------------------
                
                submenu = Menu(menuTesoreria, tearoff=0, background='#000099', foreground='white', activebackground='red3', activeforeground='white')
                
                submenu.add_command(label="Concepto de Gastos", command=lambda:
                                                                                                        self.show_frame(concepto_gastos.ConceptoGastos))
                
                submenu.add_command(label="Gastos", command=lambda:
                                                                                                        self.show_frame(gastos.Gastos))
                
                submenu.add_command(label="Beneficiarios", command=lambda:
                                                                                                        self.show_frame(beneficiarios.Beneficiarios))
                                                                                                        
                menuTesoreria.add_cascade(label='Egresos', menu=submenu)#Ver Submenu
                
                #---------------------------
                
                menuTesoreria.add_command (label="Cheques", command=aviso, state=DISABLED)
                
                menuTesoreria.add_command (label="Pagos por otros medios", command=aviso, state=DISABLED)
                
                menuTesoreria.add_separator()#----------------------------
                
                menuTesoreria.add_command (label="Contratos", command=lambda:
                                                                                                        self.show_frame(contratos.Contratos))
                
                menuTesoreria.add_command (label="Asignar Novedades", command=None, state=DISABLED)
                
                menuTesoreria.add_command (label="Recibos de caja", command=lambda:
                                                                                                                self.show_frame(recibo_caja.ReciboCaja))
                
                menuTesoreria.add_separator()#----------------------------
                
                menuTesoreria.add_command (label="Administrador de documentos", command=lambda:
                                                                                                                self.show_frame(admindocs.Admindocs))
                
                barramenu.add_cascade(label='Tesorería', menu=menuTesoreria)#Ver Submenu
                
                #CUARTO MENU: Reporte-----------------------------------------
                #Submenus: 
                
                menuReporte = Menu(barramenu, tearoff=0, background='#000099', foreground='white', activebackground='red3', activeforeground='white')
                
                menuReporte.add_command(label='Propietarios', command=lambda:
                                                        self.show_frame(reporte_propietario.Reporteprop))
                
                menuReporte.add_command (label="Arrendatarios", command=aviso)
                
                menuReporte.add_command (label="Bancos", command=aviso, state=DISABLED)
                
                menuReporte.add_command (label="Movimientos Contables", command=aviso, state=DISABLED)
                
                menuReporte.add_separator()#----------------------------
                
                menuReporte.add_command (label="Relación Inmuebles/Propietario/Inquilino", command=aviso, state=DISABLED)
                
                menuReporte.add_separator()#----------------------------
                
                menuReporte.add_command (label="Diferencias en novedades y canón", command=aviso, state=DISABLED)
                
                menuReporte.add_separator()#----------------------------
                
                menuReporte.add_command (label="Facturación por período", command=aviso, state=DISABLED)
                
                barramenu.add_cascade(label='Reportes', menu=menuReporte)#Ver Submenu
                
                #QUINTO MENU: Acceso--------------------------------------------
                #Submenus: Configuracion, Acceso
                
                menuAjustes = Menu(barramenu, tearoff=0, background='#000099', foreground='white', activebackground='red3', activeforeground='white')
                
                menuAjustes.add_command(label='Configuración', command=lambda: 
                                                        self.show_frame(config.Config))
                
                menuAjustes.add_command(label='Preferencia de Color', command=lambda: 
                                                        self.show_frame(seleccionar_color.Selector_Color))
                
                menuAjustes.add_command(label='Base de datos', command=lambda: 
                                                        self.show_frame(export_db.exportDB))
                
                menuAjustes.add_command(label='Exportar CSV', command=lambda: 
                                                        self.show_frame(export_csv.exportCSV))
                
                barramenu.add_cascade(label='Ajustes', menu=menuAjustes)#Ver Submenu
                
                #SEXTO MENU: Ayuda--------------------------------------------
                #Submenus: Acerca de
                
                menuAyuda = Menu(barramenu, tearoff=0, background='#000099', foreground='white', activebackground='red3', activeforeground='white')
                
                menuAyuda.add_command(label='Acerca', command=lambda: 
                                                        self.show_frame(acerca.Acerca))
                
                menuAyuda.add_separator()#----------------------------
                
                barramenu.add_cascade(label='Ayuda', menu=menuAyuda)#Ver Submenu
                
                #Visualizar BARRA MENU en el TOP
                self.win.config(menu=barramenu)
                
                #CONTROL DE LAS VENTANAS--------------------------------------------

                self.frames ={}
                for F in (inicio.Inicio, propietarios.Propietarios, arrendatarios.Arrendatarios, terceros.Terceros, inmuebles.Inmuebles, cuentas_contables.CuentasContables, relacionip.RelacionIP, factura_inquilino.FacturaInquilino, factura_propietario.FacturaProp, proceso_fact_auto_arre.Proceso_Fact_Auto_Arre, proceso_fact_auto_prop.Proceso_Fact_Auto_Prop, analisis_arrendatarios.AnalisisArre, analisis_propietarios.AnalisisProp, reajustes_propietario.ReajustesProp, concepto_gastos.ConceptoGastos, gastos.Gastos, beneficiarios.Beneficiarios, reporte_propietario.Reporteprop, acerca.Acerca, contratos.Contratos, recibo_caja.ReciboCaja, admindocs.Admindocs, config.Config, seleccionar_color.Selector_Color, export_db.exportDB, export_csv.exportCSV):
                        frame = F(self.container, self)
                        self.frames[F] = frame
                        frame.grid(row=0, column=0, sticky='nsew')
                        
                #self.win.bind('<Control-p>', self.show_frame(propietarios.Propietarios))

                #VENTANA VENTANA INICIAL--------------------------------------------
                self.show_frame(inicio.Inicio)
                        
        def show_frame(self, cont):
                frame = self.frames[cont]
                frame.tkraise()
                
        def dbconnexion(self):
                u = self.e1.get()
                p = self.e2.get()
                try:
                        val = conexion.Conexion(u, p)
                        self.interfaz()
                        self.state(newstate='withdraw')
                except MySQLdb.Error, e:
                        showerror("Error", "Acceso denegado!\nIntente de nuevo")
                        self.login()
        """
        def dbconnexion(self):
                u = self.e1.get()
                p = self.e2.get()
                try:
                        conn = MySQLdb.connect (host = "localhost",
                                        user = "%s" % (u),
                                        passwd = "%s" % (p),
                                        db = "sbienes")
                        self.interfaz()
                        self.state(newstate='withdraw')
                except MySQLdb.Error, e: # error if wrong username or password 
                        #print "Error %d: %s" % (e.args[0], e.args[1])
                        #sys.exit (1)
                        #cursor = conn.cursor ()
                        showerror("Error", "Acceso denegado!\nIntente de nuevo")
                        self.login()
        """

Gui()
mainloop()
