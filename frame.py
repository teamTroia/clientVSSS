class Objeto:
    def __init__(self):
        self.x=0
        self.y=0
        self.orientation=0

class Frame:
    def __init__(self):
        self.robots_blue = [Objeto(), Objeto(), Objeto()]
        self.robots_yellow = [Objeto(), Objeto(), Objeto()]
        self.ball=Objeto()