import csv

punching_bag_data_path = "boxing-gui/database/punching_bag.csv"


class PunchingBag:
    all = []

    def __init__(
        self,
        hanging_style: int = 1,
        length: float = 0.0,
        l2top: float = 0.0,
        l2btm: float = 0.0,
        mass: float = 0.0,
    ) -> None:

        self.hanging_style = hanging_style
        self.length = length
        self.l2top = l2top
        self.l2btm = l2btm
        self.mass = mass

        PunchingBag.all.append(self)

    def __repr__(self) -> str:
        return f"Bag({self.hanging_style}, {self.length}, {self.l2top}, {self.l2btm}, {self.mass})"

    def getDataFromCSV(self):
        # COPY from this: https://youtu.be/Ej_02ICOIgs?t=3653
        with open(punching_bag_data_path, "r") as f:
            reader = csv.DictReader(f)
            bag_infos = list(reader)

        for bag_info in bag_infos:
            self.hanging_style = bag_info.get("hanging_style")
            self.length = float(bag_info.get("length"))
            self.l2top = float(bag_info.get("l2top"))
            self.l2btm = float(bag_info.get("l2btm"))
            self.mass = float(bag_info.get("mass"))
            
    @staticmethod
    def saveSetting(bagInfos):
        bag_infos = bagInfos.__dict__
        
        with open('boxing-gui/database/punching_bag.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=bag_infos.keys())
            writer.writeheader()
            writer.writerow(bag_infos)
