# 20). By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].


num = [12,24,35,70,88,120,155]

output = [x for x in num if x%5==0 and x%7==0]
print(output)