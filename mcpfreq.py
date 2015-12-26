import spidev
import time
import os
from time import sleep

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
delay = 5
k = 509

while True:

  ## Read input1 data
  m1_level = ReadChannel(input1) - k
  m1_volts = ConvertVolts(m1_level,2)
  m1_percent = Percent(m1_level,2)

  print "--------------------------"
  print("mesura1: {} ({}V)".format(m1_level,m1_volts))
  print("Percentatge mesura1: ({}%)".format(m1_percent))

  sleep (0.002)
  ## Read mesura data
  m2_level = ReadChannel(input1) - k
  sleep (0.002)
  m3_level = ReadChannel(input1) - k
  sleep (0.002)
  m4_level = ReadChannel(input1) - k
  sleep (0.002)
  m5_level = ReadChannel(input1) - k
  sleep (0.002)
  m6_level = ReadChannel(input1) - k
  sleep (0.002) 
  m7_level = ReadChannel(input1) - k
  sleep (0.002)
  m8_level = ReadChannel(input1) - k
  sleep (0.002)
  m9_level = ReadChannel(input1) - k
  sleep (0.002)
  m10_level = ReadChannel(input1) - k
  sleep (0.002)

  print("mesura2: {} ".format(m2_level))
  print("mesura3: {} ".format(m3_level))
  print("mesura4: {} ".format(m4_level))
  print("mesura5: {} ".format(m5_level))
  print("mesura6: {} ".format(m6_level))
  print("mesura7: {} ".format(m7_level))
  print("mesura8: {} ".format(m8_level))
  print("mesura9: {} ".format(m9_level))
  print("mesura10: {} ".format(m10_level))  

  operation = (((m1_level**2+m2_level**2+m3_level**2+m4_level**2+m5_level**2+m6_level**2+m7_level**2+m8_level**2+m9_level**2+m10_level**2))/10)**0.5
  print(operation)

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
#  print("input8: {} ({}V)".format(input8_level,input8_volts))
#  print("Percentatge8: ({}%)".format(input8_percent))
  sleep (delay)



