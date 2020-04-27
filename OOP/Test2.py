class Clone:
    
    def __init__(self, number, protocol66):
        self.number = number
        self.protocol66 = False

    def _executeOrder66(self):
        if self.protocol66 == True:
            print(self.number, "Good soldiers, follow orders!")
            print("Kill the Jedi...")
        else:
            print(self.number, "What am i doing..?")

    def _activateChip(self):
        self.protocol66 = True
        return self.protocol66

    def _report(self):
        print("Report! Clone Trooper", self.number)
        

class Trooper(Clone):

    def __init__(self, name, legion, number, protocol66):
        Clone.__init__(self, number, protocol66)
        self.name = name
        self.legion = legion

    def _report(self):
        print("Sir, yes sir!!")
        print("Report! Clone Trooper", self.number)
        print("I am from", self.legion, "battalion!")
        print("You can call me", self.name)


class Main:
    if __name__ == "__main__":
        clone1 = Trooper("Fox", "332", "CT-3636",False)
        clone1._report()
        clone1._activateChip()
        clone1._executeOrder66()
        print()

        clone2 = Trooper("Rex", "501", "CT-7567", False)
        clone2._report()
        clone2._executeOrder66()
        print()