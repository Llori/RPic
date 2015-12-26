import spidev
import time
import os
from time import sleep
import pifacedigitalio as p
## Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

## Function to read SPI data from MCP3008 chip
## Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

## Function to convert data to voltage level,
## rounded to specified number of decimal places.
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(1023)
  volts = round(volts,places)
  return volts

def Percent(data,places):
  voltsp = (data * 100) / float(1023)
  voltsp = round(voltsp,places)
  return voltsp
## Define sensor channels
input1 = 0
input2 = 1
input3 = 2
input4 = 3
input5 = 4
input6 = 5
input7 = 6
input8 = 7


## Define delay between readings
delay = 60

p.init()
while True:
  ## Read input1 data
  input1_level = ReadChannel(input1)
  input1_volts = ConvertVolts(input1_level,2)
  input1_percent = Percent(input1_level,2)
  if input1_percent > 80:
      print("major")
      for value in range (0,2):
        for board in range (0 , 4):
          for pin in range (0,8):
            p.digital_write(2, 1, 0)
            sleep(0.02)
            p.digital_write(2, 0, 0)
  else:
      print("menor")

  ## Read input2 data
  input2_level = ReadChannel(input2)
  input2_volts = ConvertVolts(input2_level,2)
  input2_percent = Percent(input2_level,2)
  if input2_percent > 80:
      print("major")
      for value in range (0,2):
        for board in range (0 , 4):
          for pin in range (0,8):
            p.digital_write(3, 1, 0)
            sleep(0.02)
            p.digital_write(3, 0, 0)
  else:
      print("menor")

  ## Read input3 data
  input3_level = ReadChannel(input3)
  input3_volts = ConvertVolts(input3_level,2)
  input3_percent = Percent(input3_level,2)

  ## Read input4 data
  input4_level = ReadChannel(input4)
  input4_volts = ConvertVolts(input4_level,2)
  input4_percent = Percent(input4_level,2)

  ## Read input5 data
  input5_level = ReadChannel(input5)
  input5_volts = ConvertVolts(input5_level,2)
  input5_percent = Percent(input5_level,2)
    ## Read input6 data
  input6_level = ReadChannel(input6)
  input6_volts = ConvertVolts(input6_level,2)
  input6_percent = Percent(input6_level,2)

  ## Read input7 data
  input7_level = ReadChannel(input7)
  input7_volts = ConvertVolts(input7_level,2)
  input7_percent = Percent(input7_level,2)

  ## Read input8 data
  input8_level = ReadChannel(input8)
  input8_volts = ConvertVolts(input8_level,2)
  input8_percent = Percent(input8_level,2)

  ## Print out results
  f = open("/var/www/dadesact.txt", "a")
  f.write("{}".format(input1_percent))
  f.write("\n")
  f.write("{}".format(input2_percent))
  f.write("\n")
  filename = "/var/www/dadesact.txt"
  myfile = open(filename)
  lines = len(myfile.readlines())
  print "There are %d lines in %s" % (lines, filename)
  print (lines)


  if lines > 10 :
      lines = open('/var/www/dadesact.txt').readlines()
      open('/var/www/dadesact.txt', 'w').writelines(lines[2:])
      print (lines)


  f.close()
  f = open("/var/www/textmcp2.txt", "a")
  f.write("---------------------------------")
  f.write("\n")
  f.write("Voltatge LDR: {} ({}V)".format(input1_level,input1_volts))
  f.write("\n")
  f.write("Percentatge LDR: ({}%)".format(input1_percent))
  f.write("\n")
  f.write("Voltatge POTENCIOMETRE: {} ({}V)".format(input2_level,input2_volts))
  f.write("\n")
  f.write("Percentatge PT: ({}%)".format(input2_percent))
  f.write("\n")
  f.write("{}".format(input1_percent))
  f.write("\n")
  f.write("{}".format(input2_percent))
  f.write("\n")

#  f.write("input3: {} ({}V)".format(input3_level,input3_volts))
#  f.write("\n")
#  f.write("Percentatge3: ({}%)".format(input3_percent))
#  f.write("\n")
#  f.write("input4: {} ({}V)".format(input4_level,input4_volts))
#  f.write("\n")
#  f.write("Percentatge4: ({}%)".format(input4_percent))
#  f.write("\n")
#  f.write("input5: {} ({}V)".format(input5_level,input5_volts))
#  f.write("\n")
#  f.write("Percentatge5: ({}%)".format(input5_percent))
#  f.write("\n")
#  f.write("input6: {} ({}V)".format(input6_level,input6_volts))
#  f.write("\n")
#  f.write("Percentatge6: ({}%)".format(input6_percent))
#  f.write("\n")
#  f.write("input7: {} ({}V)".format(input7_level,input7_volts))
#  f.write("\n")
#  f.write("Percentatge7: ({}%)".format(input7_percent))
#  f.write("\n")
#  f.write("input8: {} ({}V)".format(input8_level,input8_volts))
#  f.write("\n")
#  f.write("Percentatge8: ({}%)".format(input8_percent))
  f.close()
  print "--------------------------"
  print("input1: {} ({}V)".format(input1_level,input1_volts))
  print("Percentatge1: ({}%)".format(input1_percent))
  print("input2: {} ({}V)".format(input2_level,input2_volts))
  print("Percentatge2: ({}%)".format(input2_percent))
#  print("input3: {} ({}V)".format(input3_level,input3_volts))
#  print("Percentatge3: ({}%)".format(input3_percent))
#  print("input4: {} ({}V)".format(input4_level,input4_volts))
#  print("Percentatge4: ({}%)".format(input4_percent))
#  print("input5: {} ({}V)".format(input5_level,input5_volts))
#  print("Percentatge5: ({}%)".format(input5_percent))
#  print("input6: {} ({}V)".format(input6_level,input6_volts))
#  print("Percentatge6: ({}%)".format(input6_percent))
#  print("input7: {} ({}V)".format(input7_level,input7_volts))
#  print("Percentatge7: ({}%)".format(input7_percent))
  print("input8: {} ({}V)".format(input8_level,input8_volts))
  print("Percentatge8: ({}%)".format(input8_percent))
## Wait before repeating loop
  time.sleep(delay)



