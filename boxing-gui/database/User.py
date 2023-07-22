from database.Database import Database


class User(Database):
    def __init__(self) -> None:
        super().__init__()
        self.connect()
        self.mycursor = self.mydb.cursor()

        # entities
        self.table = "users"
        self.age = "age"
        self.name = "name"
        self.height = "height"
        self.weight = "weight"
        self.metric = "metric"
        self.bag_id = "bag_id"
        self.baudrate = "baudrate"

    def get_user_by(
        self, name: str
    ):  # INJECTION https://www.w3schools.com/python/python_mysql_where.asp
        query = f"""
            SELECT * FROM {self.table}
            -- WHERE {self.name} LIKE %s LIMIT 1
            WHERE id = %s LIMIT 1
        """
        self.mycursor.execute(query, (f"%{name}%",))
        return self.mycursor.fetchone()

    def save_user_setting(self, user_infos: dict):
        sql = f"""
            UPDATE users 
            SET 
            {self.name} = %s,
            {self.age} = %s,
            height = %s,
            weight = %s,
            metric = %s
            WHERE id = 1
            """
        val = (
            user_infos["name"],
            user_infos["age"],
            user_infos["height"],
            user_infos["weight"],
            user_infos["metric"],
        )

        self.mycursor.execute(sql, val)
        self.mydb.commit()

    def save_user_sensor_settings(self, sensor_infos: dict):
        pass
