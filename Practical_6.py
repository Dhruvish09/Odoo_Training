# 6). Write a program that accepts a sentence and calculate the number of uppercase letters and lowercase letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

string = input("Enter Your string:")
count1 = 0
count2 = 0
for i in string:
    if(i.isupper()):
        count1 = count1+1
    elif(i.islower()):
        count2 = count2+1
print("UPPER CASE:", count1)
print("LOWER CASE:", count2)
