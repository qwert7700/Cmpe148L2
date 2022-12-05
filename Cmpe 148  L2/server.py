import socket # for socket
import sys
 
# create a socket object      
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket successfully created")

# prepare a server socket   
# port number           
port = 80               
#Ip address field is an empty string so we can listen to all computers on network 
# Binding IP address and port number to socket 
serverSocket.bind(('', port))        
     
# placing the socket in listening mode
serverSocket.listen(5)             

while True:

    # Establish the connection
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()    

    try:
 
      message = connectionSocket.recv(1024)
      filename = message.split() [1]
      f = open(filename[1: ])
      outputdata = f.read()

      # send one HTTP header line into socket
      connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

      # send the content of the requested file to the client
      for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

      connectionSocket.send("\r\n".encode())

      connectionSocket.close()

    except IOError:
      #Send respond message for file not found 	
      connectionSocket.send("HTTP/1.1 404 Not found\r\n\r\n".encode())
      connectionSocket.send("<html><head></head><body><h1>404 Not found</h1></body></html>\r\n".encode())
		
	    # Close the client connection socket	
      connectionSocket.close()

    serverSocket.close()
    sys.exit() 
