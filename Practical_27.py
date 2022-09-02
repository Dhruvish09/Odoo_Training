# By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

# Python program to remove multiple
# elements from a list

# creating a list
list1 = [12,24,35,70,88,120,155]

# given index of elements
# removes 11, 18, 23
remove_index = [0, 2, 4, 6]

for ele in sorted(remove_index, reverse = True):
	del list1[ele]

# printing modified list
print (*list1)
