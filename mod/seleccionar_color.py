#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
Color Chooser Dialog
Diálogo para Seleccionar el Color
'''
from Tkinter import*
import MySQLdb
from controller import *
from tkColorChooser import askcolor

class Selector_Color(Frame):
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)
                
		#WIDGETS
		#Label(self, text="Proceso de Facturación Automático Propietario: ").pack()
		Button(self, text="Seleccionar Color", command=getColor).pack()

def getColor():
    color = askcolor()
    print color
