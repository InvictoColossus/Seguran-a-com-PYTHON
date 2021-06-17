import os

ip_ou_host=input('Digite seu ip ou host a ser Verificado:')

os.system('ping -n 6 {}'.format(ip_ou_host))
