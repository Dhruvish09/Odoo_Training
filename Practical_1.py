# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

start = int(input("Enter Start range limit:"))
end = int(input("Enter End range limit:"))
for i in range(start, end+1):
    if ((i%7==0) & (i%5!=0)):
        print(i,"is Divisible by 7 and Not Multiply of 5.")

    
    
    
    
    
    
    
    
    
    
