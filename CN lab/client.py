# Import socket module
import socket
from time import localtime            
 
# Create a socket object

 
# Define the port on which you want to connect
              


c = socket.socket()        
c.connect(('localhost',4999))


data = list(map(str, input().split()))
# connect to the server on local computer

# i=0
for i in data:
        print("sending name",i)
        c.send(i.encode())
        y=c.recv(1024).decode()
        print(y)
        if(y=='welcome '+i):
            print("name",i,"  is sent")
            # i+=1
        else:
            print("resending name",i)
# receive data from the server and decoding to get the string.
# close the connection
c.close()    
     