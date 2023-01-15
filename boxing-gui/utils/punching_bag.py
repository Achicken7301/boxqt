class PunchingBag:

    def __init__(self,
                 style: bool = True,
                 length: float = 0.0,
                 l2top: float = 0.0,
                 l2btm: float = 0.0,
                 mass: float = 0.0) -> None:
        self.hanging_style = style
        self.length = length
        self.length2Top = l2top
        self.length2Bottom = l2btm
        self.mass = mass