from scanner.port_scanner import PortScanner
from scanner.banner_grabber import BannerGrabber

def main():
    target = input("Enter IP or hostname: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    scanner = PortScanner(target, start_port, end_port)
    open_ports = scanner.scan_ports()

    if open_ports:
        grabber = BannerGrabber(target, open_ports)
        grabber.grab_banners()
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
