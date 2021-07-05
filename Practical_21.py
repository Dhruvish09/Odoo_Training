# 21). By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

array = [[ ['0' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)

 