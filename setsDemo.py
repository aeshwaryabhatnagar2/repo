my_set={"one","two","three"}
set_one = {1.0, "Hello",(1,2,3)}
#to add a value
my_set.add("four")
my_set.add("fourty")
print(my_set)
print(my_set.union(set_one))
my_set.update([2,3,5])
print(my_set)