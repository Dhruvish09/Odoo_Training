# 31). Write a program to print the below pattern


Row = int(input("Enter the number of rows:"))  
k = 2 * Row - 2  #  number of spaces  
for i in range(0, Row):  
    for j in range(0, k):  
        print(end=" ")  
    k = k - 2   # decrement k value after each iteration  
    for j in range(0, i + 1):  
        print("* ", end="")  # printing star  
    print("")  