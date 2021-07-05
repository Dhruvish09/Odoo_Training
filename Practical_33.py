# 33). Write a program to generate Triangle Inverse pyramid Pattern:


# Num1 = int(input("Enter Your Wise Number:"))
# Num2 = int(input("Enter Your Wise Number:"))

# for i in range(Num1,Num2):
#     print(" "*((Num2-1)-i)," *"*(i))

Number = int(input("Enter the number: "))
k = Number - 2 #  number of spaces  


for i in range(Number, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1 # Incerement k value after each iteration 
    for j in range(0, i+1):
        print("* ", end="")
    print()

