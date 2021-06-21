import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print('Socket Criado com Sucesso!!')

host ='localhost'
porta = 5432

s.bind((host,porta))         
mensagem='\nServidor : de BOA NA LAGOA ?'

while 1:          #se for true
    dados,end = s.recvfrom(4096)   

    if dados:
        print('Servidor enviando Mensagens...')
        s.sendto(dados + (mensagem.encode()),end)  
