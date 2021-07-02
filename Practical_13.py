# 13). Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.

# import random

# for i in random.randrang(0,10):
#     if i%5==0 and i%7==0:
#         print("Your List is:",random.randrange(i))
#     else:
#         print("Number Not suitable for condition")

import random
start = int(input("Enter Your Start Number:"))
end = int(input("Enter Your End Number:"))
lst = [i for i in range(start,end) if i%5 == 0 and i%7 == 0]
resp = random.sample(lst,5)
print(resp)
