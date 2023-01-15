import serial.tools.list_ports

# https://stackoverflow.com/questions/55816358/how-to-obtain-bluetooth-port-direction-with-pyserial

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
        print(p.hwid)
        print(p.name, address, port_type)
        if port_type == "outgoing":
            port.append(p.name)
print(port)