import socket
from machine import Pin, ADC
import time
import network
from neopixel import NeoPixel


station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("Faisal’s iPhone", "Faisal2001")
station.isconnected()
station.ifconfig()

Potentiometer= ADC(Pin(5))
Potentiometer.atten(ADC.ATTN_11DB)       				#Full range: 3.3v
photocell= ADC(Pin(4))
photocell.atten(ADC.ATTN_11DB)      					 #Full range: 3.3v

led = Pin(48, Pin.OUT)             						# set GPIO48  to output to drive NeoPixel
HOST ='172.20.10.7'                                       # Server IP
PORT = 4444                                            # Server Port
BUF_SIZE = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    # intialize a socket
s.connect((HOST,PORT))                                  # connect to server 
c= ","
while True:
    Po= Potentiometer.read()
    ph= photocell.read()
    neo = NeoPixel(led, 1) # create NeoPixel driver on GPIO48 for 1 pixel
    s.sendall((str(ph)+c+str(Po)).encode()) # send message
    data = s.recv(BUF_SIZE).decode()                  # wait to receive a message
    print(data)
    if data == "True":
        if Po>2000:
     
                neo[0] = (255, 255, 255) # set the first pixel to white
                neo.write()              # write data to all pixels
                r, g, b = neo[0]         # get first pixel colour
                time.sleep_ms(250)
                neo[0] = (0, 0, 0)       # set the first pixel to Black
                neo.write()              # write data to all pixels
                r, g, b = neo[0]
                time.sleep_ms(250)
                neo[0] = (255, 255, 255) # set the first pixel to white
                neo.write()              # write data to all pixels
                r, g, b = neo[0]         # get first pixel colour
                time.sleep_ms(250)
                neo[0] = (0, 0, 0)       # set the first pixel to Black
                neo.write()              # write data to all pixels
                r, g, b = neo[0]
                time.sleep_ms(250)
                print("x")
        else:
                print("y")
                neo[0] = (255, 255, 255) # set the first pixel to white
                neo.write()              # write data to all pixels
                r, g, b = neo[0]         # get first pixel colour
                time.sleep(1)
                neo[0] = (0, 0, 0)       # set the first pixel to Black
                neo.write()              # write data to all pixels
                r, g, b = neo[0]         # get first pixel colour

            time.sleep(1)
    
  
    
  
