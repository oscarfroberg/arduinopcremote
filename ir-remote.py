#! /usr/bin/env python

# Read the output of an Arduino which may be printing sensor output,
# and at the same time, monitor the user's input and send it to the Arduino.
# See also
# http://www.arcfn.com/2009/06/arduino-sheevaplug-cool-hardware.html

import sys, serial, select, subprocess, os

class Arduino() :
  def run(self) :
    # Port may vary, so look for it:
    baseport = "/dev/ttyACM"
    self.ser = None
    for i in xrange(0, 9) :
      try :
        self.ser = serial.Serial(baseport + str(i), 115200, timeout=2)
        break
      except :
        self.ser = None
        pass

    if not self.ser :
      print "Couldn't open a serial port"
      sys.exit(1)
    print "Opened /dev/ttyUSB" + str(i)

    self.ser.flushInput()
      while True :
        inp, outp, err = select.select([sys.stdin, self.ser], [], [], .2)

        # If the user has typed anything, send it to the Arduino:
        if sys.stdin in inp :
          line = sys.stdin.readline()
          self.ser.write(line)

        # If the Arduino has printed anything, display it:
        if self.ser in inp :
          line = self.ser.readline().strip()
          print "Arduino:", line
  
  if line == "M":
    os.system('quodlibet --play-pause')
    os.system('echo -n  "pause" | nc -U /home/media/vlc.sock')
  if line == "N":
    os.system('quodlibet --next')
    os.system('echo -n "key key-jump+medium" | nc -U /home/media/vlc.sock')
  if line == "P":
    os.system('quodlibet --previous')
    os.system('echo -n "key key-jump-medium" | nc -U /home/media/vlc.sock')
  if line == "u":
    os.system('quodlibet --volume-up')
    os.system('echo -n "volup 2" | nc -U /home/media/vlc.sock')
  if line == "d":
    os.system('quodlibet --volume-down')
    os.system('echo -n "voldown 2" | nc -U /home/media/vlc.sock')
  if line == "U":
    os.system('amixer set PCM 10%+ -c 1')
  if line == "D":
    os.system('amixer set PCM 10%- -c 1')
  if line == "q":
    os.system('quodlibet --quit')
    os.system('echo -n "quit" | nc -U /home/media/vlc.sock')
  if line == "f":
    os.system('echo -n "f" | nc -U /home/media/vlc.sock')
  if line == "s":
    os.system('quodlibet &')
  if line == "b":
    os.system('echo -n "key key-jump-extrashort" | nc -U /home/media/vlc.sock')

arduino = Arduino()
try :
  arduino.run()
except serial.SerialException :
  print "Disconnected (Serial exception)"
except IOError :
  print "Disconnected (I/O Error)"
except KeyboardInterrupt :
  print "Interrupt"
