# python program
# to do insertion sort

# define function
def insertion_sort(list):
  for i in range(1, len(list)):
    key = list[i]
    j = i - 1
    while j >= 0 and key < list[j]:
      list[j + 1] = list[j]
      j -= 1
    list[j + 1] = key

# driver code
if __name__ == "__main__":
  list = []
  for i in range(int(input("Length ::> "))):
    list.append(int(input()))
  insertion_sort(list)

  print(list)