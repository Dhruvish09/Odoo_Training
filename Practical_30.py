# 30).  Write a program to generate below Pattern:

# * 
# * * 
# * * * 
# * * * * 
# * * * * *  

Num1 = int(input("ENter Your NUmber:"))


for i in range(0,Num1):
    for j in range(0,i+1):
        print("*",end=" ")
    print()