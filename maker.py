import argparse


includes = []
parser = argparse.ArgumentParser(description='generate a Makefile')
parser.add_argument('--board', dest='board')
parser.add_argument('--port', dest='monitor_port')
parser.add_argument('--library', nargs = '*', dest='library')

args = parser.parse_args()
board = args.board
monitor_port = args.monitor_port
for include in args.library:
  includes.append(include)


def write_make():
  f = open("Makefile", 'a+')
  f.writelines("include ./Applications/Arduino.app/Contents/Resources/Java/arduino-mk/Arduino.mk\r\n")
  f.writelines("BOARD = {0}\r\n".format(board))
  f.writelines("ARDUINO_LIBS = ")
  for include in includes:
    f.writelines(" {0}".format(include))
  f.writelines("\r\nMONITOR_PORT = {0}".format(monitor_port))
  f.close()
   
write_make()

''' i need a way to set these paths in osx, i think
ARDUINO_DIR   = /Applications/Arduino.app/Contents/Resources/Java
ARDMK_DIR     = /usr/local
'''
