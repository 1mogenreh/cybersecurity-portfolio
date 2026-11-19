import socket
import sys

def scan(host, ports):
    print(f"Scanning {host}...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((host, port)) == 0:
            print(f"Port {port} is OPEN")
        s.close()
    print("Scan complete.")

if __name__ == "__main__":
    target = sys.argv[1]
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3306, 3389, 8080]
    scan(target, common_ports)
