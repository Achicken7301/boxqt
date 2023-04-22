# import modules
import utils.CNN
import serial
import queue as q
from database.Database import Database

queue_max_size = 500

q_ax = q.Queue(maxsize=queue_max_size)
q_ay = q.Queue(maxsize=queue_max_size)
q_az = q.Queue(maxsize=queue_max_size)

queue_display = q.Queue(maxsize=queue_max_size)

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
    global acel_gyro_ser, get_data_flag, process_raw_data_flag, q_ax, q_ay, q_az

    acel_gyro_ser.close()

    # Condition to Cancel thread
    get_data_flag = True
    utils.CNN.process_raw_data_flag = True

    # reset every variables
    utils.CNN.count = 0
    utils.CNN.p_value = 0
    utils.CNN.total_p_value = []
    utils.CNN.total_p_value.append(0)

    q_ax.queue.clear()
    q_ay.queue.clear()
    q_az.queue.clear()


def getSensorData(port: str, baudrate: int = 115200):
    global get_data_flag, acel_gyro_ser, process_raw_data_flag

    acel_gyro_ser = serial.Serial(port=port, baudrate=baudrate)

    # Condition to start thread
    get_data_flag = False
    utils.CNN.process_raw_data_flag = False


def importRawData():
    global acel_gyro_ser, get_data_flag, data_plot_buffer
    print("Start importRawData")
    while 1:
        if get_data_flag:
            break

        # print("Still getting data...")
        try:
            b = acel_gyro_ser.readline()
            data_ser = b.decode().splitlines()
            # Store data to window
            """Better queue
            https://stackoverflow.com/questions/20631813/python-fifo-2-dimensional#:~:text=Using%20Queue%20module%20which%20allows%20multi%2Dthread%20use.%20Note%20that%20in%20python%203%20Queue%20has%20been%20renamed%20to%20queue.
            """
            ax_ser, ay_ser, az_ser, gx_ser, gy_ser, gz_ser = data_ser[0].split(",")
            queue[0].append(float(ax_ser))
            queue[1].append(float(ay_ser))
            queue[2].append(float(az_ser))
            queue[3].append(float(gx_ser))
            queue[4].append(float(gy_ser))
            queue[5].append(float(gz_ser))

            # store to queue for display
            if not q_ax.full():
                # queue_display.put(float(ax_ser), float(ay_ser), float(az_ser))
                q_ax.put(float(ax_ser))
                q_ay.put(float(ay_ser))
                q_az.put(float(az_ser))
            else:
                # queue_display.get()
                q_ax.get()
                q_ay.get()
                q_az.get()

        except Exception as e:
            print(f"ERROR WHEN IMPORT DATA:\n{e}\n{data_ser[0].split(',')}")
            # break
