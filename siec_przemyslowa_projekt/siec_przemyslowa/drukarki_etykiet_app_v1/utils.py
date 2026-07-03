import subprocess
import platform
from scapy.all import ARP, Ether, srp

def is_device_online(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"

    result = subprocess.run(
        ["ping", param, "1", ip],
        capture_output=True,
        text=True
    )
    # print(result.stdout)
    # print("Return code:", result.returncode)
    print("result stdout:")
    print(result.stdout)
    print("result stderr:")
    print(result.stderr)

    # return result.returncode == 0
    if ('Request timed out' in result.stdout):
        print("Urzadzenie jest wyłączone lub poza siecią")
    else:
        print("Urządzenie jest dostępne")
    return not ('Request timed out' in result.stdout)

def arp_ping(ip, timeout=2):
    # Ramka Ethernet broadcast
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    # Zapytanie ARP
    arp = ARP(pdst=ip)

    # Połączenie warstw
    packet = ether / arp

    # Wysłanie pakietu
    answered, unanswered = srp(
        packet,
        timeout=timeout,
        verbose=False
    )

    if answered:
        _, response = answered[0]
        return {
            "online": True,
            "ip": response.psrc,
            "mac": response.hwsrc
        }

    return {
        "online": False,
        "ip": ip,
        "mac": None
    }

# print(is_device_online('172.27.50.20'))