import mysql.connector


class Database:
    def __init__(self) -> None:
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.port = "3306"
        self.database = "boxqt"

    def connect(self):
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database,
        )
        self.mycursor = self.mydb.cursor()

    def disconnect(self):
        self.mydb.close()

    def setup(self, host: str, user: str, password: str, port: str, database: str):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database
