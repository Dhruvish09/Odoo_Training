# 17). Please write a program to shuffle and print the list [3,6,7,8].

import random


test_list = [3, 6, 7, 8]
print("The original list is : " + str(test_list))

random.shuffle(test_list)
print("The shuffled list is : " + str(test_list))
