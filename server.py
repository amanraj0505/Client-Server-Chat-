import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.bind((host,port))
s.listen(5)
x=''
c,addr=s.accept()
print('Got connection from',addr)
while x!='exit' :
		
		x=c.recv(1024)
                print x
		x=raw_input('Enter message:')
                c.send(x)
s.close	
