class Base:
    def __init__(self):
        self.lol = 'lol is protected'

    def _getLol(self):
        return self.lol

class Derived:
    def __init__(self):
        Base.__init__(self)