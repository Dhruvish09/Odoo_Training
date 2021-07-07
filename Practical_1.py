# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

        
try:
    start = int(input("Enter Start range limit:"))
    end = int(input("Enter End range limit:"))
    for i in range(start, end+1):
        if ((i % 7 == 0) & (i % 5 != 0)):
            print(i, "is Divisible by 7 and Not Multiply of 5.")
except:
    print("Something Is Wrong Please Enter Valid Input")    
else:
    print("No More Number found! for Divisible by 7 and Not Multiply by 5")
finally:
    print("Thanx For Data Input")
    
# for i in range(start, end+1):
#     if ((i % 7 == 0) & (i % 5 != 0)):
#         print(i, "is Divisible by 7 and Not Multiply of 5.")
#     else:
#         print("No Number found! for Divisible by 7 and Not Multiply by 5")
#         
    
    
# listOfLambdas = [lambda i=i: i*i for i in range(1, 6)]
# for f in listOfLambdas:
#     print (f())
# Import required libraries
