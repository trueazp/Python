# python program to print
# factor(s) of a number

# define function to find factor(s)
def factor(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

# input
num = int(input("Enter a number => "))

# print
print("Factor(s) of your number", factor(num))