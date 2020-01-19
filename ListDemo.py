#create a list with three numbers, and its total of the numbers added together should be 100.

my_list=[50, 20, 30]
# add a  value
my_list.append(1)
print (my_list)
# to remove a value from a lost use remove function
my_list.remove(20)
print(my_list)
#searches for the given element from the start of the list and returns its index
print(my_list.index(1))
#removes and returns the element at the given index
print(my_list.pop(1))
# add the element at the end
my_list.extend([25,28])
print(my_list)
#insert the element at the given position
my_list.insert(0,"joe")
print(my_list)
#slicing
list = ['a','b','c','d']
print(list[1:-1])
print(list[0:-3])