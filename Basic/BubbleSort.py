# python program
# to do bubble sort

# define function
def bubble_sort(list):
  length = len(list)
  # traverse through all list's elements
  for i in range(length - 1):
    # last i element are already in place
    for j in range(0, length - i - 1):
      # swapping between elements
      if list[j] > list[j + 1]:
        list[j], list[j + 1] = list[j + 1], list[j]

# driver code
if __name__ == "__main__":
  list = []
  for i in range(int(input("Length ::> "))):
    list.append(int(input()))
  bubble_sort(list)

  print("Sorted List :", list)