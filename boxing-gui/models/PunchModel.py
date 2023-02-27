class Punch:
    def __init__(self) -> None:
        self.is_punched = False

    def setPunch(self, value: bool):
        self.is_punched = value
        return self.is_punched

    def getPunch(self):
        return self.is_punched
