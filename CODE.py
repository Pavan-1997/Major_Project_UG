 8.1 CODE  
 
INDUSTRIAL AUTOMATION

#Import Libraries
import BlynkLib
import time
import RPi.GPIO as GPIO ##GPIO library
import time
import I2C_LCD_driver
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.OUT) 
GPIO.setup(35,GPIO.OUT) 
GPIO.setup(32,GPIO.OUT) 

#Software SPI configuration (ADC)
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

#LCD Initialization
mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_display_string("INDUSTRIAL",1,3)
mylcd.lcd_display_string("AUTOMATION   PLC",2,0)
time.sleep(4)
mylcd.lcd_display_string("TEMP:",1,0)
mylcd.lcd_display_string("SMOKE:",1,8)
mylcd.lcd_display_string("FIRE:",2,0)
mylcd.lcd_display_string("LIGHT:",2,8)
mylcd.lcd_display_string("|",1,7)
mylcd.lcd_display_string("|",2,7)
# Hardware SPI configuration (ADC)
SPI_PORT   = 0
SPI_DEVICE = 0
mcp=Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
print('Reading MCP3008 values, press Ctrl-C to quit...')

#Blynk Authentication  Token
BLYNK_AUTH = '26d0f1db030d445593af98eef1c445b5'
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

while True:
#Temperature Sensor Configuration
   t1=mcp.read_adc(0)
   t2=(t1*500)/1024
   t=(int(t2)-20) 			   	 
   if t<=38:
    GPIO.output(35,0)
    GPIO.output(36,1)
   else:
    blynk.notify("High Temperature") 
    GPIO.output(35,1)
    GPIO.output(36,0)
   print "Temperature:",t
   mylcd.lcd_display_string("%d"%t,1,5)    
   blynk.virtual_write(3,t)  		
   time.sleep(0.5)

#Smoke Sensor Configuration
   s1=mcp.read_adc(1)
   s2=(s1*500)/1024
   s=(int(s2*0.2)) 	
   if s<=85:
    GPIO.output(35,0)
   else:
    blynk.notify("Smoke Detected") 	
    GPIO.output(35,1)
   print "Smoke:",s   
   mylcd.lcd_display_string("%d"%s,1,14)	
   blynk.virtual_write(4,s)
   time.sleep(0.5)

#Fire Sensor Configuration
   f1=mcp.read_adc(2)
   f2=f1*0.1
   f=(int(f2)-1)
   if f<=45:
    GPIO.output(35,1)
    blynk.notify("Fire Detected")
   else: 
    GPIO.output(35,0)
   print "Fire:",f
   blynk.virtual_write(5,f)
   mylcd.lcd_display_string("%d" %f,2,5)    		
   time.sleep(0.5)

#Light Sensor Configuration
   l1=mcp.read_adc(3)
   l2=l1*0.1
   l=(int(l2)+20) 
   if l<=25:
    blynk.notify("No Light")
    GPIO.output(35,1)
    GPIO.output(32,0) 
   else:
    GPIO.output(35,0)
    GPIO.output(32,1) 
   print "Light:",l    		
   blynk.virtual_write(6,l)
   mylcd.lcd_display_string("%d" %l,2,14)
   time.sleep(0.5)

#IR Sensor Configuration
   m1=mcp.read_adc(4)
   m2=m1*0.1
   m=(int(m2)) 
   if m<=45:    
    blynk.notify("Motion Detected")
    GPIO.output(35,1)
   else:
    GPIO.output(35,0)
   print "Motion:",l    		
   blynk.virtual_write(7,m)

POWER LINECOMMUNICATION

import serial
import RPi.GPIO as GPIO      
import os, time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
#CLK  = 18
#MISO = 23
#MOSI = 24
#CS   = 25
#mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
#print('Reading MCP3008 values, press Ctrl-C to quit...')
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.5)
while True: 
	t1=mcp.read_adc(3)
	if (t1>=50):
		port.write('Light Present \n')
        else:
    		port.write('Light Absent \n')	
	print (t1) 	
	time.sleep(1.25)

