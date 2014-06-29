import argparse


includes = []
# needs platform detection, and version checking 
ard_dir   = "/usr/share/arduino" #where to find the stuff it needs
ard_mk    = "/usr/local"   #arduino-mk directory
tools_dir = "/usr"
parser = argparse.ArgumentParser(description='generate a Makefile')
parser.add_argument('--board', dest='board')
parser.add_argument('--port', dest='monitor_port')
parse.add_argument('--dir', dest='ard_dir')
parser.add_argument('--libs', nargs = '*', dest='libs')

args = parser.parse_args()
board = args.board
monitor_port = args.monitor_port
for include in args.libs:
  includes.append(include)


def write_make():
  f = open("Makefile", 'a+')
  f.writelines("ARDUINO_DIR = {0}\r\n".format(ard_dir))
  f.writelines("ARD_MK =  {0}\r\n".format(ard_mk))
  f.writelines("AVR_TOOLS_DIR =  {0}\r\n".format(tool_dir))
  f.writelines("BOARD = {0}\r\n".format(board))
  f.writelines("ARDUINO_LIBS =")
  for include in includes:
    f.writelines(" {0}".format(include))
  f.writelines("\r\nMONITOR_PORT = {0}".format(monitor_port))
  f.writelines("include /usr/local/arduino/Arduino.mk\r\n")

  f.close()
   
write_make()
