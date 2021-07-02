# 10). Write a program which are divisible by 7 and between a given range 0 and n.

n = int(input("Enter End range limit:"))
print("Your Limit is between 0 to",n,"so Output is....") 
for i in range(0, n+1):
    if i>1:    
        if ((i % 7 == 0)):      
            print(i, "is Divisible by 7 .")
    # else:
    #     print("Not Deivisibe:")       