import csv
import pandas as pd

user_data_path = "boxing-gui/database/user.csv"


class User:
    all = []

    def __init__(
        self,
        meas_sys: int = 1,
        name: str = "fullname1",
        age: int = 0,
        height: float = 0.0,
        weight: float = 0.0,
    ) -> None:

        self.metric_sys = meas_sys
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

        User.all.append(self)

    def __repr__(self) -> str:
        return f"User({self.metric_sys},'{self.name}', {self.age}, {self.height}, {self.weight})"

    def getDataFromCSV(self):
        # COPY from this: https://youtu.be/Ej_02ICOIgs?t=3653
        with open(user_data_path, "r") as f:
            reader = csv.DictReader(f)
            user_infos = list(reader)

        for user_info in user_infos:
            self.name = user_info.get("name")
            self.metric_sys = user_info.get("meas_sys")
            self.age = int(user_info.get("age"))
            self.height = float(user_info.get("height"))
            self.weight = float(user_info.get("weight"))
            
   
    @staticmethod
    def saveSetting(user):
        user_info = user.__dict__
        
        with open('boxing-gui/database/user.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=user_info.keys())
            writer.writeheader()
            writer.writerow(user_info)