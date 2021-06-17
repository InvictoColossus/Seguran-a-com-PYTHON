import os
from time import  sleep

with open('ip.txt') as file:  
    dump = file.read()   
    dump = dump.splitlines()   


    for ip in dump:
       os.system('ping -n 5 {}'.format(ip))
       sleep(5)

