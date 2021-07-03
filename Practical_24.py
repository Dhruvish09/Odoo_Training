# 24). With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
  
# Driver Code
lst1 = [1,3,6,78,35,55]
lst2 = [12,24,35,24,88,120,155]
print(intersection(lst1, lst2))