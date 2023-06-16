import pyfiglet
import sys
import socket
from datetime import datetime
import progressbar

ascii_banner = pyfiglet.figlet_format("ScanHackPort")
print(ascii_banner)
  
target = input(str("Digite o ip do servidor: "))


Wng = """ 

0 até 1023 - São as consideradas “portas conhecidas”. Portas nesse intervalo são fornecidas apenas para serviços estabelecidos e grandes empresas ou centros de pesquisa de confiança.

1024 até 49151 - São as chamadas “portas registradas”. Esse nome significa que as portas nesse intervalo podem ser registradas para protocolos específicos por grandes corporações.

49152 até 65535 - É o intervalo que engloba as portas dinâmicas e as portas privadas. Portas nesse intervalo podem ser usadas por praticamente qualquer um e, portanto, são as com 
maior probabilidade de haver vulnerabilidade.

"""


"""
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #target
    
else:
    print("Quantidade inválida de argumento")
 """

i = 0
bar = progressbar.ProgressBar(
    widgets=[
        progressbar.Percentage()
    ])


# Add Banner
print("-" * 50)
print("Scaneando Ip Andress: " + target)
print("Scaneamento iniciado em:" + str(datetime.now()))
print("-" * 50)
  
try:
    print(Wng)
    port = int(input("Iniciar detecção a partir de qual porta? "))
    LimitedPort = int(input("Finalizar detecção até qual porta? "))
    while (port <= LimitedPort):
        port = port + 1
        i = i+1
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        bar.update(i)
        if result ==0:
            print("Porta {} está aberta.".format(port))
        else:
            print("Porta {} está fechada.".format(port))    
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
