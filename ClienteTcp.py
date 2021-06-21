import  socket   
import sys      

def main():
    try:          
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)  
    except socket.error as erro:  
        print('A conexão falhou !!!')
        print('Erro: {}'.format(erro))
        sys.exit()      

    print('Socket criado com SUCESSO!!')

    hostAlvo=input('Digite o Host ou Ip a ser Conectado: ')
    portaAlvo=input('Digite a Porta a ser Conectada: ')

    try:
        s.connect((hostAlvo,int(portaAlvo)))
        print("Cliente TCP conectado com Sucesso"+ hostAlvo + 'e na porta: ' + portaAlvo)
        s.shutdown(2)      
    except socket.error as e:
        print('Não foi possível conectar no host:'+ hostAlvo + 'e na porta:' + portaAlvo)
        print('Error {}'.format(e))
        sys.exit()

if __name__ == ('__main__'):
    main()
