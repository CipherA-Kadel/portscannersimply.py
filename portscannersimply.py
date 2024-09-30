import socket

import socket

def scan_ports(ip, ports):
    print(f"Escaneando puertos en {ip}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Puerto {port} está abierto")
        else:
            print(f"Puerto {port} está cerrado")
        sock.close()

# Dirección IP objetivo y lista de puertos a escanear
target_ip = "192.168.1.1"
ports_to_scan = [22, 80, 443, 8080]

scan_ports(target_ip, ports_to_scan)