#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       reglagesF1.py
#       
#       Copyright 2012 Fco Javier Lucena <fran.lucena@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import sqlite3

from electre import Electre
from gi.repository import Gtk

class Electre_GUI:
	
	def onButtonPressed(self,button):
		print "Creando instancia para Electre"
		Electre(8,8)
		datos ={'d1': str(row[0][1]) + ' Km',
				 'd2': str(row[0][2]) + ' Vueltas',
				 'd3': str(row[0][3]) + ' Seg',
				 'd4': str(row[0][4]) + ' m',
				 'd5': str(row[0][5]) + ' Km/h',
				 'd6': str(row[0][11]) + '/' + str(row[0][6]) ,
				 'd7': row[0][7],
				 'd8': row[0][8],
				 'd9': row[0][9],
				 'd10': str(row[0][10]),
				}
		
		self.populate_entry_optimo(datos)
		
    
	def onCircuitActivate(self, menuitem):
				
		circuito = menuitem.get_label()
		image = self.builder.get_object("image1")
		image.set_from_file(self.get_image(circuito))
				
		entry1 = self.builder.get_object("entry1")
		entry2 = self.builder.get_object("entry2")
		entry3 = self.builder.get_object("entry3")
		entry4 = self.builder.get_object("entry4")
		entry5 = self.builder.get_object("entry5")
		entry6 = self.builder.get_object("entry6")
		entry7 = self.builder.get_object("entry7")
		entry8 = self.builder.get_object("entry8")
		entry9 = self.builder.get_object("entry9")
		entry10 = self.builder.get_object("entry10")
		
				
		datos = self.get_datos(circuito)
		
		entry1.set_text(datos['d1'])
		entry2.set_text(datos['d2'])
		entry3.set_text(datos['d3'])
		entry4.set_text(datos['d4'])
		entry5.set_text(datos['d5'])
		entry6.set_text(datos['d6'])
		entry7.set_text(datos['d7'])
		entry8.set_text(datos['d8'])
		entry9.set_text(datos['d9'])
		entry10.set_text(datos['d10'])
		
		return True
		
	def onAboutDialog(self, *args):
		self.about = self.builder.get_object("aboutdialog1")
		self.about.show_all()
		
	def onCloseAbout(self, *args):
		self.about = self.builder.get_object("aboutdialog1")
		self.about.hide()
		
	
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file("rF1.glade")
		self.handlers = {"onDeleteWindow": Gtk.main_quit,
						"onButtonPressed": self.onButtonPressed,
						"onCircuitActivate": self.onCircuitActivate,
						"onAboutDialog": self.onAboutDialog,
						"onCloseAbout": self.onCloseAbout,}
        
		self.builder.connect_signals(self.handlers)
		self.init_combobox()
		self.window = self.builder.get_object("reglajes")
		self.window.show_all()
		
	def init_combobox(self):
		
		renderer_text = Gtk.CellRendererText()
		
		combobox1 = self.builder.get_object("combobox1")
		combobox1.pack_start(renderer_text, True)
		combobox1.add_attribute(renderer_text, "text", 0)
		
		combobox2 = self.builder.get_object("combobox2")
		combobox2.pack_start(renderer_text, True)
		combobox2.add_attribute(renderer_text, "text", 0)
		
		combobox3 = self.builder.get_object("combobox3")
		combobox3.pack_start(renderer_text, True)
		combobox3.add_attribute(renderer_text, "text", 0)
		
		combobox4 = self.builder.get_object("combobox4")
		combobox4.pack_start(renderer_text, True)
		combobox4.add_attribute(renderer_text, "text", 0)
		
		combobox5 = self.builder.get_object("combobox5")
		combobox5.pack_start(renderer_text, True)
		combobox5.add_attribute(renderer_text, "text", 0)
		
		combobox6 = self.builder.get_object("combobox6")
		combobox6.pack_start(renderer_text, True)
		combobox6.add_attribute(renderer_text, "text", 0)
		
		combobox7 = self.builder.get_object("combobox7")
		combobox7.pack_start(renderer_text, True)
		combobox7.add_attribute(renderer_text, "text", 0)
		
		combobox8 = self.builder.get_object("combobox8")
		combobox8.pack_start(renderer_text, True)
		combobox8.add_attribute(renderer_text, "text", 0)
		
		combobox9 = self.builder.get_object("combobox9")
		combobox9.pack_start(renderer_text, True)
		combobox9.add_attribute(renderer_text, "text", 0)
		
		combobox10 = self.builder.get_object("combobox10")
		combobox10.pack_start(renderer_text, True)
		combobox10.add_attribute(renderer_text, "text", 0)
		
		
		
		combobox11 = self.builder.get_object("combobox11")
		combobox11.pack_start(renderer_text, True)
		combobox11.add_attribute(renderer_text, "text", 0)
		
		combobox12 = self.builder.get_object("combobox12")
		combobox12.pack_start(renderer_text, True)
		combobox12.add_attribute(renderer_text, "text", 0)
		
		combobox13 = self.builder.get_object("combobox13")
		combobox13.pack_start(renderer_text, True)
		combobox13.add_attribute(renderer_text, "text", 0)
		
		combobox14 = self.builder.get_object("combobox14")
		combobox14.pack_start(renderer_text, True)
		combobox14.add_attribute(renderer_text, "text", 0)
		
		combobox15 = self.builder.get_object("combobox15")
		combobox15.pack_start(renderer_text, True)
		combobox15.add_attribute(renderer_text, "text", 0)
		
		combobox16 = self.builder.get_object("combobox16")
		combobox16.pack_start(renderer_text, True)
		combobox16.add_attribute(renderer_text, "text", 0)
		
		combobox17 = self.builder.get_object("combobox17")
		combobox17.pack_start(renderer_text, True)
		combobox17.add_attribute(renderer_text, "text", 0)
		
		combobox18 = self.builder.get_object("combobox18")
		combobox18.pack_start(renderer_text, True)
		combobox18.add_attribute(renderer_text, "text", 0)
		
		return True


	def populate_entry_optimo(self,datos):
		
		entry11 = self.builder.get_object("entry11")
		entry12 = self.builder.get_object("entry12")
		entry13 = self.builder.get_object("entry13")
		entry14 = self.builder.get_object("entry14")
		entry15 = self.builder.get_object("entry15")
		entry16 = self.builder.get_object("entry16")
		entry17 = self.builder.get_object("entry17")
		entry18 = self.builder.get_object("entry18")
		entry19 = self.builder.get_object("entry19")

		entry11.set_text(datos['d1'])
		entry12.set_text(datos['d2'])
		entry13.set_text(datos['d3'])
		entry14.set_text(datos['d4'])
		entry15.set_text(datos['d5'])
		entry16.set_text(datos['d6'])
		entry17.set_text(datos['d7'])
		entry18.set_text(datos['d8'])
		entry19.set_text(datos['d9'])

	def get_image(self, circuito):
		
		images ={'Albert Park': 'resources/albert_park.jpg',
				 'Sepang': "resources/sepang.jpg",
				 'Shangai': 'resources/shangai.jpg',
				 'Bahrein': 'resources/bahrein.jpg',
				 'Montmelo': 'resources/catalunya.jpg',
				 'Monte Carlo': 'resources/monacocir.jpg',
				 'Estambul Park': 'resources/estambul.jpg',
				 'Silverstone': 'resources/silverstone.jpg',
				 'Nurburgring': 'resources/alemania_circuito.jpg',
				 'Hungaroring': 'resources/hungria.jpg',
				 'Valencia': 'resources/valencia.jpg',
				 'Spa': 'resources/spa.jpg',
				 'Monza': 'resources/monza.jpg',
				 'Marina Bay': 'resources/singapur.jpg',
				 'Suzuka': 'resources/japon.jpg',
				 'Interlagos': 'resources/brasil.jpg',
				 'Abu Dhabi': 'resources/abu.jpg',
				 'Portada': 'resources/portada.jpg',}
		
		if images.has_key(circuito):
			return images[circuito]
		else:
			return images['Portada']
		
	def get_datos(self, circuito):
		
		db = "speed_circuits.db"
		connection=sqlite3.connect(db)
		cursor=connection.cursor()
		cursor.execute("select * from circuits where Nombre = '%s'" % circuito)
		row = cursor.fetchall()
		cursor.close()
		
		datos ={'d1': str(row[0][1]) + ' Km',
				 'd2': str(row[0][2]) + ' Vueltas',
				 'd3': str(row[0][3]) + ' Seg',
				 'd4': str(row[0][4]) + ' m',
				 'd5': str(row[0][5]) + ' Km/h',
				 'd6': str(row[0][11]) + '/' + str(row[0][6]) ,
				 'd7': row[0][7],
				 'd8': row[0][8],
				 'd9': row[0][9],
				 'd10': str(row[0][10]),
				}
				
		return datos

	

def main():
	window = Electre_GUI()
	Gtk.main()

	return 0

if __name__ == '__main__':
	main()

