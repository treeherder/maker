arduino makefile maker aimed at raspbian

`--libs` parameter takes any number of arguments

pi@raspberrypi ~/maker $ python maker.py --board uno --port /dev/ttyACM0 --libs Arduino


ARDUINO_DIR = /usr/share/arduino
ARD_MK =  /usr/share
AVR_TOOLS_DIR =  /usr
BOARD = uno
ARDUINO_LIBS = Arduino
ARDUINO_PORT = /dev/ttyACM0
include /usr/share/arduino/Arduino.mk
