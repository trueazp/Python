# python program
# to print Fibonacci number list
# within the given length

# define function
def fibonacci(n):
  a = 0
  b = 1

  if n < 0:
    return "Incorrect input"
  elif n == 0:
    return a
  elif n == 1:
    return b
  else:
    for i in range(2, n):
      c = a + b
      a = b
      b = c
    return b

# driver code
if __name__ == "__main__":
  list = []
  for i in range(int(input("Length ::> "))):
    list.append(fibonacci(i))
  print(list)