import socket
from scanner.utils import is_valid_ip
import time

class PortScanner:
    def __init__(self, target, start_port, end_port):
        self.target = socket.gethostbyname(target) if not is_valid_ip(target) else target
        self.start_port = start_port
        self.end_port = end_port

    def scan_ports(self):
        open_ports = []
        print(f"\nScanning {self.target} from port {self.start_port} to {self.end_port}...\n")

        for port in range(self.start_port, self.end_port + 1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((self.target, port))
                if result == 0:
                    print(f"[+] Port {port} is open")
                    open_ports.append(port)
                sock.close()
            except KeyboardInterrupt:
                print("Scan cancelled by user.")
                break
            except socket.error as e:
                print(f"Socket error: {e}")
                break
        return open_ports
