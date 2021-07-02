# 25). With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved. 

duplicate = [12,24,35,24,88,120,155,88,120,155]
x  = list(set(duplicate))
print("Duplicate List is:",duplicate)
print("Filter List is:",x)
