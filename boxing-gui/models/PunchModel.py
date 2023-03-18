class Punch:
    def __init__(self) -> None:
        self.is_punched = False
        self.count = 1
        self.total_punch_value = [0]

    def setPeakForce(self):
        self.peak_force = max(self.number_force_punches)

    def getPeakForce(self):
        return self.peak_force

    def isPunched(self, value):
        self.total_punch_value[self.count] = value
        self.count += 1

    def setPunch(self, value: bool):
        self.is_punched = value
        return self.is_punched

    def getPunch(self):
        return self.is_punched
