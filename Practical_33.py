Num1 = int(input("Enter Your Wise Number:"))
Num2 = int(input("Enter Your Wise Number:"))

for i in range(Num1,Num2):
    print(" "*((Num2-1)-i)," *"*(i))

# rows = int(input("Enter the number of rows: "))
# k = rows - 2
# # This is used to print the downward pyramid
# for i in range(rows, -1, -1):
#     for j in range(k, 0, -1):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, i+1):
#         print("* ", end="")
#     print()

