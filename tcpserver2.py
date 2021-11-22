import socket
import string
from datetime import datetime
import os
from bs4 import BeautifulSoup, SoupStrainer
import requests

HOST = ''
PORT = 5000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    con, client = tcp.accept()
    print('conectado por', client)
    while True:
        request = con.recv(1024).decode("utf-8")
        if not request: break
        first_line = request.split('\r\n')[0]
        file_path = first_line.split(' ', 2)[1]

        print('file path: ', file_path)

        if file_path == "/":
            file_path = "/response.html"

        try:
            with open('.{}'.format(file_path)) as f:
                file_ = f.readlines()
        except IOError:
            file_ = []

        if first_line.find('HTTP/Tupi') == -1:
            #resposta http/1.1 normal
            now = datetime.now()
            now_s = now.strftime("%a, %-d %b %Y %H:%M:%S %Z")
            if not file_:
                size_err = os.path.getsize('./error.html')
                try:
                    with open('./error.html') as f:
                        file_ = f.readlines()
                except IOError:
                    pass 
                response = 'HTTP/1.1 404 Not Found\r\n'
                response += 'Date: {}\r\n'.format(now_s)
                response += 'Server: server\r\n'
                response += 'Content-Length: {}\r\n'.format(size_err)
                response += 'Content-Type: text/html\r\n\r\n'
                response += ''.join(file_)
            else:
                size_file = os.path.getsize('.{}'.format(file_path))
                response = 'HTTP/1.1 200 OK\r\n'
                response += 'Date: {}\r\n'.format(now_s)
                response += 'Server: server\r\n'
                response += 'Content-Length: {}\r\n'.format(size_file)
                response += 'Content-Type: text/html\r\n\r\n'
                response += ''.join(file_)

        else:
            now = datetime.now()
            now_s = now.strftime("%a, %-d %b %Y %H:%M:%S %Z")
            url_field = request.split('\r\n')[3]
            url = url_field.split(' ')[1]
            print(url)
            if not url:
                size_err = os.path.getsize('./error.html')
                try:
                    with open('./error.html') as f:
                        file_ = f.readlines()
                except IOError:
                    pass 
                response = 'HTTP/Tupi 404 Not Found\r\n'
                response += 'Date: {}\r\n'.format(now_s)
                response += 'Server: Server\r\n'
                response += 'Content-Length: {}\r\n'.format(size_err)
                response += 'Content-Type: text/html\r\n\r\n'
                response += ''.join(file_)
            else:
                response = 'HTTP/Tupi 200 OK\r\n'
                response += 'Date: {}\r\n'.format(now_s)
                response += 'Server: Server\r\n'
                response += 'Content-Type: text/plain\r\n\r\n'

                #url = "https://ccsa.ufs.br/pagina/20168-departamento-de-ciencia-da-informacao"

                page = requests.get(url)    
                if page.status_code != 200:
                    print('Um problema ocorreu e a requisição retornou código ', page.status_code)
                    sys.exit(1)

                data = page.text
                soup = BeautifulSoup(data, features="html.parser")

                for link in soup.find_all('a'):
                    ref = link.get('href')
                    if isinstance(ref, str):
                        response += ref + '\n'

        con.send(bytes(response, "utf-8"))

    print('finalizando conexao com cliente', client)
    con.close()
