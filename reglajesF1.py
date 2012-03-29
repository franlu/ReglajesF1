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

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onButtonPressed(self, button):
        print "Hello World!"

def main():
	builder = Gtk.Builder()
	builder.add_from_file("rF1.glade")
	builder.connect_signals(Handler())

	window = builder.get_object("reglajes")
	window.show_all()

	Gtk.main()

	return 0

if __name__ == '__main__':
	main()

