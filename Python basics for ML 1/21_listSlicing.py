arr = [1,2,3,10,20,45]

print(arr)
print(arr[2:5])
print(arr[0::2])

arr[1] = 'cars'
print(arr)

# shallow copy
arr2 = arr
arr[0] = 500
print(arr2)
#the changes show in arr2 too as arr2 just has the address
#of where the list is stored, not the list itself

#full copy
arr3 = arr[:]
arr[0] = 600
print(arr3)
#copies the entire list as a sub array

