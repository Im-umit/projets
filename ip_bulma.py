import socket
import requests
from ipwhois import IPWhois

def get_ip_address(domain):
    """Web sitesinin IP adresini alır."""
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

def check_port(ip, port):
    """Belirli bir IP adresi ve port için portun açık olup olmadığını kontrol eder."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

def get_geolocation(ip):
    """IP adresine göre coğrafi konumu alır."""
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        return response.json()
    except requests.exceptions.RequestException as e:
        return None

def scan_ports(ip, ports):
    """Bir IP adresindeki açık portları tarar."""
    open_ports = []
    for port in ports:
        if check_port(ip, port):
            open_ports.append(port)
    return open_ports

def main():
    while True:
        domain = input("Web sitesi domainini girin: ")
        
        # Web sitesinin IP adresini al
        ip_address = get_ip_address(domain)
        if ip_address is None:
            print(f"{domain} bulunamadı. Lütfen geçerli bir domain girin.")
            continue  # Geçerli bir domain girilene kadar tekrar sor
        
        print(f"Web sitesinin IP adresi: {ip_address}")
        
        # IP adresi ile coğrafi konumu al
        location = get_geolocation(ip_address)
        if location:
            print(f"Konum: {location.get('city', 'Bilinmiyor')}, {location.get('region', 'Bilinmiyor')}, {location.get('country', 'Bilinmiyor')}")
        else:
            print("Konum bilgisi alınamadı.")
        
        # Açık portları tarama
        ports_to_check = [80, 443, 8080, 22, 21, 3306, 25]  # Sık kullanılan portlar
        open_ports = scan_ports(ip_address, ports_to_check)
        
        if open_ports:
            print(f"Açık portlar: {', '.join(map(str, open_ports))}")
        else:
            print("Hiçbir port açık değil.")
        
        break  # Geçerli bir domain girildiyse döngüden çık

if __name__ == "__main__":
    main()