# python program to print
# mode of a list

# import
import statistics

# define function (shortcut)
def mode_shortcut(data):
    return statistics.mode(data)

# define function (traditional)
def mode(data):
    max_count = (0, 0)
    for i in data:
        occurences = data.count(i)
        if occurences > max_count[0]:
            max_count = (occurences, i)
    return max_count[1]

# declare a list
data = []

# input element(s)
for i in range(0, int(input("Input length => "))):
    data.append(int(input()))

print("Modusnya adalah =>", mode_shortcut(data))
print("Modusnya adalah =>", mode(data))