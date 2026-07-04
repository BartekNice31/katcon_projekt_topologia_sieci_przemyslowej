import socket

def print_label(zpl:str='',printer_ip:str='',port:int=9100):
    print(printer_ip,port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((printer_ip, port))
    sock.sendall(zpl.encode())
    sock.close()