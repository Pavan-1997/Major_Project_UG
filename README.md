# Major Project done in my Under Graduation:

## Industrial Automation and Power Line Communication

In this project, we proposed a system where you can easily monitor and control the 
different parameters using sensors. In this we used a Raspberry Pi and Arduino Nano. Blynk is 
used as an open source IOT platform through which data is send from the sensors to the cloud. 
Here we used five sensors for the monitoring the Industrial System. In which all component 
plays crucial role & have individual responsibilities. Since we used five sensors out of which 
three sensors (Temperature, Smoke and Light) are analog sensors and rest of the two sensors 
are digital (Fire and IR) where these sensors are interfaced to the ADC Input Channels. 
Temperature sensor which is used to monitor the temperature inside the industry, whenever it 
raises above the threshold value of 50, the module sends a mobile notification from Blynk, 
displays the current temperature reading value on the Dashboard and LCD, turns ON Buzzer 
and Common LED and also powers ON the Fan through relay. Smoke sensor which is used to 
monitor the smoke inside the industry, whenever it raises above the threshold value of 50, the 
module sends a mobile notification from Blynk, displays the current smoke reading value on 
the Dashboard and LCD, turns ON Buzzer and Common LED. Fire Sensor is used to detect 
flame inside the industry, whenever decreases below the threshold value of 25, the module 
sends a mobile notification from Blynk, displays the current temperature reading value on the 
Dashboard and LCD, turns ON Buzzer and Common LED. Light Sensor is used to monitor the 
light intensity inside the industry, whenever it decreases below the threshold value of 25,the 
module sends a mobile notification from Blynk , displays the current temperature reading value 
on the Dashboard and LCD, turns ON Buzzer and Common LED and also powers ON the Bulb 
through relay.IR Sensor is used for motion detection Sensor i.e. whenever a person enters into 
Restricted Areas, whenever decreases below the threshold value of 25,the module sends a 
mobile notification from Blynk , displays the current temperature reading value on the 
Dashboard ,turns ON Buzzer and Common LED. 

In Power Line Communication the purpose of implementation is to transfer the data 
from one industry to another industry through the existing power lines where both are present 
near to each other. In this we have considered Light Sensor as a parameter to transfer the data 
from Sub Industry to the Main Industry i.e. whenever the Light senor value crosses a threshold 
value 50, a message signal is send from Raspberry Pi to PLC TX through Serial 
Communication. A local carrier signal is internally generated in both PLC TX and PLC RX 
having carrier frequency of 125KHz.Now message signal is modulated with the carrier signal 
(FSK Modulation) and the modulated signal that is obtained is now passed from PLC TX AC 
Line to the PLC RX AC Line. Here AC Line acts as a medium for the modulated signal to pass 
from TX to RX. Now the modulated signal that is received at the PLC RX is demodulated using 
the local carrier signal (FSK Demodulation) and the message signal is now obtained back, this 
message signal is passed to the Arduino Nano through Serial Communication. The message 
signal is now read on the serial monitor through a USB cable connected to Arduino Nano which 
also acts a power supply to PLC RX and Arduino Nano. Serial Monitor displays the message 
to the Main industry officials, whenever the Light value decreases below a threshold value and 
they can take necessary actions immediately. 

Attached are the CODE and reports for my project.
