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

from electre import Electre
from gi.repository import Gtk

class Electre_GUI:
	
	def onButtonPressed(self,button):
		print "Creando instancia para Electre"
		Electre(8,8)
    
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
		
		entry1.set_text(datos[d1])
		entry2.set_text(datos[d2])
		entry3.set_text(datos[d3])
		entry4.set_text(datos[d4])
		entry5.set_text(datos[d5])
		entry6.set_text(datos[d6])
		entry7.set_text(datos[d7])
		entry8.set_text(datos[d8])
		entry9.set_text(datos[d9])
		entry10.set_text(datos[d10])
		
		return True
	
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file("rF1.glade")
		self.handlers = {"onDeleteWindow": Gtk.main_quit,
						"onButtonPressed": self.onButtonPressed,
						"onCircuitActivate": self.onCircuitActivate,}
        
		self.builder.connect_signals(self.handlers)
		self.window = self.builder.get_object("reglajes")
		self.window.show_all()
		
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
		
		#conectar con db
		
		datos ={'d1': ,
				 'd2': ,
				 'd3': ,
				 'd4': ,
				 'd5': ,
				 'd6': ,
				 'd7': ,
				 'd8': ,
				 'd9': ,
				 'd10': ,
				}
				
		return datos

	

def main():
	window = Electre_GUI()
	Gtk.main()

	return 0

if __name__ == '__main__':
	main()

