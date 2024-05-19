import socket
import time 
import matplotlib.pylab as plt

HOST ='172.20.10.7'                                       # Server IP
PORT = 4444                                            # Server Port
BUF_SIZE = 1024                                         # Buffer Size
i=24                                                    # recive 24 item of data before disconnect
j=0
x=1
z=0
Potentiometer = []
photocell = []
D=[]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # initialize a socket
s.bind((HOST,PORT))                                     # register port with OS
print("I am waiting for a client ...")
s.listen(1)                                             # wait for a connection

conn, add = s.accept()                                  # accept connection and retrieve conn object and address
print("I got a connection form ",add)
while i>0:
    i= i-1                                              #send 10 times 
    time.sleep(1)
    data= conn.recv(BUF_SIZE).decode()                 # check if data accepted
    if not data:                                        # no data, pass
        break
    print('I received: '+ str(data))
    value= data.split(",")
    D.append(value)

    print(value)
    v= value[j]
    print(v)
    if int(v) > 1000:
        conn.sendall("False".encode()) 
    else:   
        conn.sendall("True".encode()) 
    time.sleep(0.5)
conn.close()
print(D)
z=0
for sublist in D:
    photocell.append(int(sublist[0]))
    Potentiometer.append(int(sublist[1]))

print("photocell:", photocell)
print("Potentiometer", Potentiometer)

plt.plot(Potentiometer)
plt.ylabel('Potentiometer')
plt.xlabel('Time')
plt.show()

plt.plot(photocell)
plt.ylabel('photocell')
plt.xlabel('Time')
plt.show()
