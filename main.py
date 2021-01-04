import re
import os
import socket
import sys
import time

#TODOS OS COMANDOS UTILIZADOS SÃO DO SISTEMA OPERACIONAL WINDOWS.
print (""" 
     [ 1 ] Wi-Fi Capter
     [ 2 ] Web Info Connect
     [ 3 ] System Cleaner
     [ 4 ] ChatBot
     [ 5 ] Exit
	 """)
choice = (int(input('Selecione uma das opções: ')))
if choice == 1:
   #mostrar informacoes da rede,  adicionar duas opcoes variadas.
   os.system('sudo apt-get install net-tools')
   time.sleep(3)
   os.system('clear')
   print ('===================================================================')
   infonet = os.system('ifconfig')
   print ('===================================================================')
   print (' ')
   print ('Todos os dados serão salvos.')
   time.sleep(5)
   os.system('clear')
   ip = ('192.168.0.1').split('.')
   for i in range(1,200):
      ip[1] = str(i)
      newip = '.'.join(ip)
      ping = os.system('ping -c 1 -4 -W 1 {}'.format(newip))
      if ping == 0:
         print ('=================================')
    hst = print ('O {} está ativo'.format(newip))
         print ('=================================')
elif choice == 2:
    #conectar com um site, pegar informações, buscar informações com google dork, observar possíveis falhas, adicionar 2 opçoes variadas.
    os.system('sudo apt-get install netifaces')
    os.system('clear')
    8888888888888888
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect('{}', 6677).format(ip)
    data = socket.recv(2048)
    print ('data')
elif choice == 3:
     os.system('sudo apt-get autoremove')
     os.system('sudo apt-get autoclean')
     os.system('sudo apt-get clean')
     os.system('sudo -i')
     os.system('# sync; echo 1 > /proc/sys/vm/drop_caches')
     os.system('sudo -i')
     os.system('# sync; echo 2 > /proc/sys/vm/drop_caches')
     os.system('sudo -i') 
     os.system('# sync; echo 3 > /proc/sys/vm/drop_caches') 
     os.system('sudo -i')
     os.system('# swapoff -a && swapon -a')
elif choice == 4:
     print ('test')	 #bot que capta informaçoes e cria banco de dados com MySql
elif choice == 5:
     print ('Obrigado por utilizar o PyJect! Volte sempre.')
     time.sleep(3.0);
     os.system('cls');
     sys.exit();

else:
     print ('Me desculpe, não consegui entender o seu comando. Me diga o que deseja fazer:')
     print (""" 
     [ 1 ] Sair
     [ 2 ] Reiniciar
     [ 3 ] Elefante.
		""")

     choice1 = int(input('Selecione uma opcao: '))
     if choice1 == 1:
        print ('Obrigado por utilizar o PyJect! Volte sempre.')
        time.sleep(3.0);
        os.system('cls');
        sys.exit();
     elif choice1 == 2:
          print ('Aguarde um minuto')
          os.system('cls');
          os.system('python main.py');
     elif choice1 == 3:
          print (""" 
     ║\
     ║▒\
     ║▒▒\
     ║░▒║
     ║░▒║
     ║░▒║
     ║░▒║  Passe os Bytes agora mesmo!
     ║░▒║
     ║░▒║
     ║░▒║
     ║░▒║
    ▓▓▓▓▓▓▓
     ]█▓[
     ]█▓[
     ]█▓[
	""")
          time.sleep(5.0);
          sys.exit();
