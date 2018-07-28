# Checagem de Vunerabilidade Gateway de Internet dos Clientes da ConsulData #

import socket, os


ports = [22, 80, 443, 4343, 2222, 8181]

arq = open('ips-radios.txt','r')
linha = arq.readline()
ips = linha.split()


for ip in ips:
        response = os.system('ping -c 1 ' + ip)
        if response == 0:
            print(str(ip) + (' is UP'))
            for port in ports:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.1)
                code = client.connect_ex((ip, port))
                if code == 0:
                    print (str(port) + (" -> Porta Aberta -- VUNERAVEL"))
                else:
                    print (str(port) + (" -> Porta Fechada -- Tudo OK... "))
        else:
            print(str(ip) + (' is DOWN'))
arq.close()