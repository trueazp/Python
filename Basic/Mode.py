# python program to print
# mode of a list

# import
import statistics

# define function to find mode
def mode(data):
    element = 0
    count = 0
    for i in data[0:]:
        temp_element = i
        temp_count = 0
        for j in data[0:]:
            if j == temp_element:
                temp_count += 1
        if (temp_count > count):
            element = temp_element
            count = temp_count
    if count == 1:
        return data
    else:
        return element


# declare a list
data = []

# input element(s)
for i in range(0, int(input("Input length => "))):
    data.append(int(input()))

print("Modusnya adalah =>", mode(data))