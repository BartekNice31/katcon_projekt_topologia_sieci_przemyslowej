import socket

def check_tcp(ip, port=502, timeout=1):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return True
    except:
        return False