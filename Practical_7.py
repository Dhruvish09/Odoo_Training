# 7). Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the prografor i in range(1,7):
#     for j in range(1,7):
#         if j<=i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print()m:
# 9
# Then, the output should be:
# 11106

value = input("Enter value: ")

n1 = value * 1
n2 = value * 2
n3 = value * 3
n4 = value * 4

total = int(n1) + int(n2) + int(n3) + int(n4)
print(total)
