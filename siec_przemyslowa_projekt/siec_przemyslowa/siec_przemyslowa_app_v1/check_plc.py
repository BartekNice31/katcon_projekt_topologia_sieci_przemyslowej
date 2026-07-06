from . models import PLCMaszyna
import snap7

def check_connection(id_plc:int):
    plc_sterownik=PLCMaszyna.objects.filter(id=id_plc)
    connection=False
    try:
        plc=snap7.client.Client()
        plc.connect(plc_sterownik.Ip_Adres,plc_sterownik.rack,plc_sterownik.rack)
        connection=True
    except Exception as e:
        connection=False
        print(e)
    return connection
