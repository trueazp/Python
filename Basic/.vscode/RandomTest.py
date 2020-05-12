import random

if __name__ == "__main__":
  list = ["Hi", "Hola", "Hello", "Bonjour", "Hi", "Hola"]
  emptyList = [1]
  emptyList.pop()
  mySet = set([])
  # print random number in between the given parameters
  print("%.2f" %random.uniform(2.75, 4.00))
  # print random element in list
  print(list[random.randrange(0, len(list), 1)])
  # random print
  print("Hello", 12)
  # check if list is empty
  if not emptyList:
    print(True)
  else:
    print(False)