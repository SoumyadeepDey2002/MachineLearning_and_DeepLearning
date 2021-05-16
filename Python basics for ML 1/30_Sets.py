# Set - unordered collection of unique objects

my_set = {1,2,3,4,5,5}

print(my_set)
#the last 5 did not get added as it was a duplicate

my_set.add(100)
my_set.add(3)

print(my_set)
#3 didn't get added as it wasn't unique, it was already there

#remove duplicates from a array

my_list = [1,2,3,4,5,5,5,5,6]

my_list = list(set(my_list))
print(my_list)

#we cannot access index in set

print(4 in my_set)

new_set = my_set.copy()
print(my_set)

my_set.clear()

print(my_set)
print(new_set)

