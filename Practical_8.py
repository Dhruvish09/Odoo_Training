# 8). Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# D means deposit while W means withdrawal.
# Then, the output should be:
# 500
# computes net bank amount based on the input
# "D" for deposit, "W" for withdrawal

# define a variable for main amount
import sys
"""
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
¡­
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""

# netAmount = 0
# while True:
#     s = input("enter the operation and then amount")
#     if not s:
#         break
#     values = s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation=="D":
#         netAmount+=amount
#     elif operation=="W":
#         netAmount-=amount
#     else:
#         pass
# print ("Your Balance Is:",netAmount)

string = ' g e e k '
print(string.replace(" ",""))
