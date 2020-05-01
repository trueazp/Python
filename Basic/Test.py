class Main:
  def __init__(self):
    self.__string = "Hello there..."

  def getString(self):
    return self.__string


if __name__ == "__main__":
    a = Main()
    print(a.getString())
    