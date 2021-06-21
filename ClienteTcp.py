import  socket   # faz o relacionamento da placa de rede e o SO
import sys     #fornece o acesso algumas variáveis e funções que tem no python

def main():
    try:          #pega da biblioteca socket o metodo socket AF_INET mostra q vamos utilizar o protocolo ip
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)  #SOCK_STREAM que passara o protocolo tcp
    except socket.error as erro:  #0 passa o protocolo que fará a comunicação com o servidor o tcp
        print('A conexão falhou !!!')
        print('Erro: {}'.format(erro))
        sys.exit()      #sai do programa de der erro

    print('Socket criado com SUCESSO!!')

    hostAlvo=input('Digite o Host ou Ip a ser Conectado: ')
    portaAlvo=input('Digite a Porta a ser Conectada: ')

    try:
        s.connect((hostAlvo,int(portaAlvo)))
        print("Cliente TCP conectado com Sucesso"+ hostAlvo + 'e na porta: ' + portaAlvo)
        s.shutdown(2)      #Finaliza a Conexão
    except socket.error as e:
        print('Não foi possível conectar no host:'+ hostAlvo + 'e na porta:' + portaAlvo)
        print('Error {}'.format(e))
        sys.exit()

if __name__ == ('__main__'):
    main()
