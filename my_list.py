my_list = [] # Initialize an empty list

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print('initial append to the empty list:', my_list)

my_list.insert(1, 15) # Insert 15 at index 1(second position)
print('After adding 15 to the second position:', my_list)

my_list.extend([50, 60, 70]) # Extend the list with multiple elements
print('After extending list:', my_list)

my_list.pop() # Remove the last element
print('After removing the last element:', my_list)

my_list.sort() # Sort the list
print('After sorting the list:', my_list)
