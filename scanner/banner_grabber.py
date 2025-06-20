import socket

class BannerGrabber:
    def __init__(self, target, open_ports):
        self.target = target
        self.ports = open_ports

    def grab_banners(self):
        print("\nGrabbing banners...\n")
        for port in self.ports:
            try:
                sock = socket.socket()
                sock.settimeout(2)
                sock.connect((self.target, port))
                banner = sock.recv(1024).decode().strip()
                print(f"[Banner] Port {port}: {banner}")
                sock.close()
            except:
                print(f"[!] No banner or connection refused on port {port}")
