# import modules

import utils.CNN
import serial

global acel_gyro_ser, get_data_flag, queue
get_data_flag = False

ax = []
ay = []
az = []
gx = []
gy = []
gz = []
queue = [ax, ay, az, gx, gy, gz]


def closeSer():
    global acel_gyro_ser
    acel_gyro_ser.close()


def stopGetData():
    global acel_gyro_ser, get_data_flag, process_raw_data_flag, view_data_thread

    acel_gyro_ser.close()

    # Condition to Cancel thread
    get_data_flag = True
    utils.CNN.process_raw_data_flag = True
    view_data_thread = True


def getSensorData(port: str, baudrate: int = 115200):
    global get_data_flag, acel_gyro_ser, process_raw_data_flag, view_data_thread

    acel_gyro_ser = serial.Serial(port=port, baudrate=baudrate)

    # Condition to start thread
    get_data_flag = False
    utils.CNN.process_raw_data_flag = False
    view_data_thread = False


def importRawData():
    global acel_gyro_ser, get_data_flag
    print("Start importRawData")
    while 1:
        if get_data_flag:
            break
        try:
            # print("Still getting data...")
            b = acel_gyro_ser.readline()
            data_ser = b.decode().splitlines()
            # Store data to window
            ax_ser, ay_ser, az_ser, gx_ser, gy_ser, gz_ser = data_ser[0].split(",")
            queue[0].append(ax_ser)
            queue[1].append(ay_ser)
            queue[2].append(az_ser)
            queue[3].append(gx_ser)
            queue[4].append(gy_ser)
            queue[5].append(gz_ser)
        except Exception as e:
            print(e)
            break
