from subprocess import call
import time
includes = ["SoftwareSerial", "Wire", "Servo", "/some/other/path/Library.h"]
class Maker():
  def create_make(self):
    call(["touch", "Makefile"])
  f = open("Makefile", 'a+')
  f.write("include .**I DONT UNDERSTAND MAC PKG***/arduino-mk/Arduino.mk\r\n")
  f.close() 
  def write_make(self):
    try:
      f = open("Makefile", "a+")
      f.write("ARDUINO_LIBS = ")
      f.close()
      for include in includes:
        f = open("Makefile", 'a+')
        f.write(" {0}".format(include))
        f.close()
    except:
      print ("failure to write")
maker = Maker()
maker.create_make()
maker.write_make()
time.sleep(1)
