# python program
# to print pascal triangle

height = int(input("Input height ::> "))

for i in range(0, height):
  coef = 1
  for j in range(1, height - 1):
    print("  ", end="")
  for k in range(0, i + 1):
    print("  ", coef, end="")
    coef = int(coef * (i - k) / (k + 1))
  print()