# 12). Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

import random
my_list = [i for i in range(0,10) if i%2 != 0]
output = random.sample(my_list,5)
print("Your List is:",output)
