from subprocess import call
import time


class Maker():
  def __init__(self, lib):
  	self.lib = lib
  def create_make(self):
  	call(["touch", "Makefile"])
 	f = open("Makefile", 'a+')
 	f.write   	
  def write_make(self):
   	f.write("{0}".format(self.lib))
  	f.close()
maker = Maker("SoftwareSerial")
maker.create_make()
time.sleep(1)
maker.write_make()
