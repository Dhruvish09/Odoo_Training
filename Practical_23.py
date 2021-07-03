# 23). By using list comprehension, please write a program to print the list after removing the value 24 in "the list is :"

lst = [12,24,35,24,88,120,155]
lt = set(lst)
lst = list(lt)
lst.sort()
lst.pop(1)

print(lst)