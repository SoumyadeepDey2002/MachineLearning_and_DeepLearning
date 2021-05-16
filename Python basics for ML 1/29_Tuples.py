#immutable lists

my_tuple = (1,2,3,4,5)

print(my_tuple)
print(my_tuple[1])
print(5 in my_tuple)

my_tuple = (45,34,66)
#reassignment is possible

print(my_tuple)

user = {
    (1,2): [1,2,3,4,5],
    'greet' : 'hello',
     45 : 5
}

print(user[(1,2)])

#slicing tuples
new_tuple = my_tuple[1:4]
print(my_tuple)
print(my_tuple[1:2])

#multiple variable declaration

x,y,z, *other = (1,2,3,4,5)

print(other)

t1 = (1,1,3,3,3,5)

# tuple methods

print(t1.count(1))
#frequency of 1 in the tuple

print(t1.index(5))

# functions

print(len(t1))