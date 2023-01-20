import serial
import serial.tools.list_ports

def serial_ports():
    '''
    This function didn't scan from OUTSIDE.
    It's MUST connect to bluetooth via OS 1st in order to work!!!
    '''
    port = []
    cp = serial.tools.list_ports.comports()
    for p in cp:
        if "BTHENUM" in p.hwid:
            start_of_address = p.hwid.rfind("&")
            end_of_address = p.hwid.rfind("_")
            address = p.hwid[start_of_address + 1:end_of_address]
            if int(address, 16) == 0:
                port_type = "incoming"
            else:
                port_type = "outgoing"
                # get Outgoing ports ONLY
            if port_type == "outgoing":
                port.append(p.name)
    return port

if __name__ == '__main__':
    print(serial_ports())