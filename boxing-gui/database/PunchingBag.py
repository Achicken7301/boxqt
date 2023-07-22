from database.Database import Database


class PunchingBag(Database):
    def __init__(self) -> None:
        super().__init__()
        self.connect()
        self.mycursor = self.mydb.cursor()

    def get_user_bag(self, name: str):
        """
        @paras

        @return
        """
        # INJECTION https://www.w3schools.com/python/python_mysql_where.asp
        query = """        
        SELECT users.name, users.age, users.height, users.weight, users.metric, 
        bags.hanging_style, bags.weight, bags.length, bags.l2top, bags.l2btm
        FROM users
        JOIN bags ON bags.id = users.bag_id
        WHERE users.id = %s LIMIT 1
        """
        # TODO: USER AUTH
        query_auth = """
        SELECT bags.* FROM users
        JOIN bags ON bags.id = users.bag_id
        WHERE users.name LIKE %s LIMIT 1
        """

        # self.mycursor.execute(query, (f"%{name}%",))
        self.mycursor.execute(query, (name,))

        return self.mycursor.fetchone()

    def save_bag_setting(self, bag_infos: dict):
        sql = """
            UPDATE bags 
            SET 
            hanging_style = %s,
            weight = %s,
            length = %s,
            l2top = %s,
            l2btm = %s
            WHERE id = 1
            """
        val = (
            bag_infos["hanging_style"],
            bag_infos["weight"],
            bag_infos["length"],
            bag_infos["l2top"],
            bag_infos["l2btm"],
        )

        self.mycursor.execute(sql, val)

        self.mydb.commit()
