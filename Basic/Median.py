# python program to print
# median of a list of number(s)

# define median function
def median(list_of_num):
    list_of_num.sort()
    if len(list_of_num) % 2 == 1:
        return list_of_num[int((len(list_of_num) - 1) / 2)]
    elif len(list_of_num) % 2 == 0:
        middle_index_1 = int(len(list_of_num) / 2)
        middle_index_2 = int(len(list_of_num) / 2) - 1
    return (list_of_num[middle_index_1] + list_of_num[middle_index_2]) / 2

# declare a list
list_of_num = []

# input element(s)
for i in range(0, int(input("Enter length => "))):
    list_of_num.append(int(input()))
    
print("Median =>", median(list_of_num))