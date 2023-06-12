import pyfiglet
import sys
import socket
from datetime import datetime
  
ascii_banner = pyfiglet.figlet_format("ScanHackPort")
print(ascii_banner)
  
target = input(str("Digite o ip do servidor: "))
"""
if len(sys.argv) == 2:
    #target = socket.gethostbyname(sys.argv[1]) #target
     target = input(str("Digite o ip do servidor: "))
    
else:
    print("Quantidade inválida de argumento")
 
"""

# Add Banner
print("-" * 50)
print("Scaneando Target: " + target)
print("Scaneamento iniciado em:" + str(datetime.now()))
print("-" * 50)
  
try:
    
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result ==0:
            print("Port {} is open".format(port))
        s.close()
         
except KeyboardInterrupt:
        print("\n Saindo do programa !!!!")
        sys.exit()
except socket.gaierror:
        print("\n Não foi possivel neste Hostname !!!!")
        sys.exit()
except socket.error:
        print("\ Servidor não responde !!!!")
        sys.exit()
