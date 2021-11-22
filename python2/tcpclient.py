import socket

HOST = '127.0.0.1'
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print 'Informe o nome do arquivo: '
file_name = raw_input()
print 'Informe o protocolo HTTP (1.1 ou Tupi): '
prot = raw_input()

while file_name <> '\x18':
    request = 'GET /{} HTTP/{}\r\n'.format(file_name, prot)
    request += 'Host: depressed.boy.depr\r\n'
    request += 'Accept-Language: la\r\n'
    print "sending request: \n", request
    tcp.send(request);
    response = tcp.recv(1024)
    print "received response: \n", response

    print 'Informe o nome do arquivo: '
    file_name = raw_input()
    print 'Informe o protocolo (HTTP/1.1 ou HTTP/Tupi): '
    prot = raw_input()

tcp.close()
