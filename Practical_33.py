# Num1 = int(input("Enter Your Wise Number:"))
# Num2 = int(input("Enter Your Wise Number:"))

# for i in range(Num1,Num2):
#     print(" "*((Num2-1)-i)," *"*(i))


# Generating Inverse Pyramid Pattern Using Stars

row = int(input('Enter Your Wise Number: '))

for i in range(row,0,-1):
    for j in range(row-i):
        print(' ', end='') 
    
    for j in range(2*i-1):
        print('*',end='') 
    print()