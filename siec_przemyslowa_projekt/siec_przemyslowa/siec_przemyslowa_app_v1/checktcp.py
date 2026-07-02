import socket

def is_tcp_open(ip, port=502, timeout=1):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return True
    except:
        return False
    
print(is_tcp_open("172.27.50.20", 502))