import socket
s=socket.socket()
host=socket.gethostname()
port=12345
x=''
s.connect((host,port))
while x!='exit' :
		
		x = raw_input('Enter Message:')
		s.send(x)
		x=s.recv(1024)
                print x
s.close
