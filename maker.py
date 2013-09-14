from subprocess import call
import time
includes = ["SoftwareSerial", "Wire", "Servo", "/some/other/path/Library.h"]
board = "Uno"
monitor_port = "/dev/tty.usb*"

class Maker():
  def create_make(self):
    call(["touch", "Makefile"])

  def write_make(self):
    f = open("Makefile", 'a+')
    f.writelines("include .**I DONT UNDERSTAND MAC PKG***/arduino-mk/Arduino.mk\r\n")
    f.writelines("BOARD = {0}\r\n".format(board))
    f.close() 
    try:
      f = open("Makefile", "a+")
      f.writelines("ARDUINO_LIBS = ")
      f.close()
      for include in includes:
        f = open("Makefile", 'a+')
        f.writelines(" {0}".format(include))
        f.close()
    except:
      print ("failure to write libs")
    try:
      f = open("Makefile", "a+")
      f.writelines("\nMONITOR_PORT= {0}".format(monitor_port))
      f.close()
    except:
      print("failure to write port")

maker = Maker()
maker.create_make()
maker.write_make()
