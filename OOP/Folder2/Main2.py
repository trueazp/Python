from Folder1.Main1 import Main1

class Main2(Main1):

  def __init__(self, name, gender):
    super().__init__(name)
    self.__gender = gender

  def talk(self):
    return super().talk()

  def showGender(self):
    return self.__gender