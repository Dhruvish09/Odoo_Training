# 32). Write a program to generate Triangle pyramid Pattern:

Number= int(input("Enter the number of rows: "))  
k = (2 * Number) - 2  
for i in range(0, Number):  
    for j in range(0, k):  
        print(end=" ")  
    k = k - 1  # decrementing m after each loop  
    for j in range(0, i + 1):  
        # printing full Triangle pyramid using stars  
        print("* ", end=' ')  
    print(" ")  