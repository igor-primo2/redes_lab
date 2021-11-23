# lab_redes

## Qual o problema você está resolvendo?

	O problema proposto é a dificuldade de visualizar as liguações http de uma
	página utilizando as utilidades de desenvolvedores de navegodores
	populares. A variação do protocolo HTTP sugerida aqui, chamada HTTP Tupi,
	funciona retornando uma lista das ligações visíveis em formato text/plain
	de uma  página apontada por uma URL fornecida pelo usuário.

	Se o protocolo especificado for HTTP/1.1, a resposta consistirá numa resposta
	HTTP/1.1 com um arquivo de conteúdo text/html. Se o protocolo especificado for 
	HTTP/Tupi, a resposta será um arquivo de conteúdo text/plain com uma lista
	das ligações visíveis na página apontada pela URL fornecida. Se nenhuma
	URL for fornecida, então será utilizada a URL da página inicial do
	DCI DEPARTAMENTO DE CIÊNCIA DA INFORMAÇÃO da UFS.

## Qual departamento da UFS é seu cliente (usuário)?

	DCI DEPARTAMENTO DE CIÊNCIA DA INFORMAÇÃO.

## Qual o formato do protocolo?

### A) Mensagens

	Quanto a mensagens nada é implementado. Se o cliente fizer uma requisição
	HTTP/1.1 apenas a versão do protocolo, o método, e o arquivo solicitado são 
	especificados na primeira linha do cabeçalho. Os outros cabeçalhos são
	'Host: ufs.client.br' e 'Accept-Language: *'.

	Se o cliente fizer uma requisição HTTP/Tupi, entretando, uma URL deve ser
	fornecida. Essa URL será passada via um novo cabeçalho, chamado 
	'URL_Field'. Os outros cabeçalhos 'Host: ufs.client.br' e 'Accept-Language: *'
	também farão parte da requisição.

### B) Campos

	Os campos são, para HTTP/1.1: 'Host' e 'Accept-Language', além do método
	'GET / HTTP/1.1'.
	
	Para HTTP/Tupi: 'Host', 'Accept-Language' e 'URL_Field', além do método
	'GET / HTTP/upi'.

### Valores

	Para HTTP/1.1: 'Host: ufs.client.br', 'Accept-Language: *' e o arquivo
	especificado no método GET deve ser provido pelo usuário/cliente.

	Para HTTP/Tupi: 'Host: ufs.client.br', 'Accept-Language: *', 
	'URL_Field: <url>' e o usuário/cliente deve fornecer a URL.

# Onde está o código do cliente?

	No arquivo tcpclient2.py

# Onde está o código do servidor?

	No arquivo tcpserver2.py

# Descreva o processo de implantação do software.

	Não foi possível implantar o servidor no ambiente CORE porque
	a máquina virtual não possui recursos suficientes para 
	baixar os módulos utilizados pelos códigos.
