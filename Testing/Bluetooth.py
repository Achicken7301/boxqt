import serial
import time

print("Start")
# This will be different for various devices and on windows it will probably be a COM port.
port = "COM7"
# Start communications with the bluetooth unit
bluetooth = serial.Serial(port, 115200)
print("Connected")
bluetooth.flushInput()  # This gives the bluetooth a little kick
for i in range(5):  # send 5 groups of data to the bluetooth
    print("Ping")
    # These need to be bytes not unicode, plus a number
    bluetooth.write(b"BOOP "+str.encode(str(i)))
    # This reads the incoming data. In this particular example it will be the "Hello from Blue" line
    input_data = bluetooth.readline()
    # These are bytes coming in so a decode is needed
    print(input_data.decode())
    time.sleep(0.1)  # A pause between bursts
bluetooth.close()  # Otherwise the connection will remain open until a timeout which ties up the /dev/thingamabob
print("Done")
