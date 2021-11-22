import socket
import sys

HOST = '127.0.0.1'
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

file_name = ''
url = ''

print('Informe o protocolo HTTP (1.1 ou Tupi): ')
prot = input()
if prot == "1.1":
    print('Informe o nome do arquivo: ')
    file_name = input()
elif prot == "Tupi":
    print('Informe a URL: ')
    url = input()
else:
    print('Foi mal')
    sys.exit(1)


while file_name != '\x18' and prot == "1.1":
    request = 'GET /{} HTTP/1.1\r\n'.format(file_name)
    request += 'Host: depressed.boy.depr\r\n'
    request += 'Accept-Language: pt\r\n'
    print("sending request: \n", request)
    tcp.send(bytes(request, "utf-8"));
    response = tcp.recv(1024).decode("utf-8")
    print("received response: \n", response)

    print('Informe o nome do arquivo: ')
    file_name = input()

while url != '\x18' and prot == "Tupi":
    if url == '':
        url = "https://ccsa.ufs.br/pagina/20168-departamento-de-ciencia-da-informacao"
    request = 'GET / HTTP/Tupi\r\n'
    request += 'Host: depressed.boy.depr\r\n'
    request += 'Accept-Language: pt\r\n'
    request += 'URL_Field: {}\r\n'.format(url)
    print("sending request: \n", request)
    tcp.send(bytes(request, "utf-8"));
    response = tcp.recv(1024).decode("utf-8")
    print("received response: \n", response)
    print('Informe a URL: ')
    url = input()
        

tcp.close()
