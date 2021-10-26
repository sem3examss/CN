# first of all import the socket library
import socket            
 
# next create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
          
s.bind(('localhost', 4999))        
 
# put the socket into listening mode
s.listen(3)    
print ("Waiting to connect")           
 
# a forever loop until we interrupt it or
# an error occurs
c, addr = s.accept()  
print ('Server connected to ', addr )
y=''
while True:
    
    x=c.recv(1024).decode()
    print("received name",x)
    y='welcome '+x
    print(y)
    
    c.send(y.encode()) 
    if y=='welcome ':
        print('Completed')
        break
c.close()
