# 15). Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

l = list()
for i in range(100,200):
        if (i%2==0):
            l.append(i)

print(l[:5])

