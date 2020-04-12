# python program to print
# mode of a list

# import
import statistics

# define function
def mode(data):
    return statistics.mode(data)

# declare a list
data = []

# input element(s)
for i in range(0, int(input("Input length => "))):
    data.append(int(input()))

print("Modusnya adalah =>", mode(data))