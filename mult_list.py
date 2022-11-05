#multiply all the numbers in a list

def mult_list(lists):
    result = 1
    for x in lists:
        result = result * x
    return result

list = [2, 3, 4]
list2 = [9, 9, 9, 9]
list3 = [4, 44, 444, 4444]

print(mult_list(list))
print(mult_list(list2))
print(mult_list(list3))