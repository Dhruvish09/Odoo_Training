my_list = [2,3,-4,5,-6,1,67,31]
new_list = []

while my_list:
    min = my_list[0]
    for i in my_list:
        if i < min:
            min = i
    new_list.append(min)
    my_list.remove(min)

print(new_list)