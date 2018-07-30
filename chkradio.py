import socket
import os

ports = [22, 80, 443, 4343, 2222, 8181]

arq = open('ips-radios.txt', 'r')
arq1 = open('ips-vuneraveis.txt', 'w')
linha = arq.readline()
ips = linha.split()
iptmp = ''

for ip in ips:
    response = os.system('ping -c 2 ' + ip + '>> /dev/null')
    if response == 0:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.3)
            code = client.connect_ex((ip, port))
            if code == 0:
                print(str(ip) + ' ' + str(port) + ' -> Porta Aberta!!')
                if iptmp != ip:
                    os.system('echo ' + ip + '>> ips-vuneraveis.txt')
                else:
                    pass
                iptmp = ip
            else:
                pass
    else:
        print(str(ip) + ' is DOWN')
arq.close()
arq1.close()
