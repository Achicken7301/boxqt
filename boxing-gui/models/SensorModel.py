import serial
from database.Database import Database


class Sensor(Database):
    def __init__(self) -> None:
        super().__init__()
        self.get_data_flag = True

        # Load port and baudrate from database
        self.port = "COM3"
        self.baudrate = 115200

    def setup(self, port: str = "COM3", baudrate: int = 115200) -> None:
        self.axel_gyro_ser = serial.Serial(port, baudrate)
        # save port and baudrate to database

    def close(self):
        self.axel_gyro_ser.close()

    def getData(self):
        self.setup(port = self.port, baudrate = self.baudrate)
        self.axel_gyro_ser.readlines().decode("utf-8").splitlines()

    def stop_get_data(self):
        self.get_data_flag = False
        self.axel_gyro_ser.close()
