# python program to print
# the first 3 largest numbers in a list

# import
import sys

# define function
def ranking(values):
    # supporting variables
    min = -sys.maxsize - 1
    largest1 = min
    largest2 = min
    largest3 = min

    # sorting sequence
    for i in values[0:]:
        if i > largest1:
            largest3 = largest2
            largest2 = largest1
            largest1 = i
        elif i > largest2:
            largest3 = largest2
            largest2 = i
        elif i > largest3:
            largest3 = i
    
    ranked = [largest1, largest2, largest3]
    return ranked

# declare a list
values = []

# input element(s)
print("Enter random 5 number")
for i in range(0, 5):
    values.append(int(input()))

# print
print("Rank 1 =", ranking(values)[0])
print("Rank 2 =", ranking(values)[1])
print("Rank 3 =", ranking(values)[2])