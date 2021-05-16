basket = [1,2,3,4,5]

print(basket)
print(len(basket))

#adding
basket.append(100)
#append doesn't return any value 
print(basket)

#inserting
basket.insert(2,400)
print(basket)

#extend
basket.extend([600,601])
print(basket)

#removing
basket.pop()
#returns what ever you have just removed
print(basket)

basket.remove(1) 
#takes in the value to remove
print(basket)

#basket.clear()
#print(basket)

#other methods

print(basket.index(5))
#takes in the value and returns the index where it is present
print(basket.index(100,2,6))
#search in ranges

#keywords in python to search

print(400 in basket)

basket = [1,2,1,2,1,4,7,7,5,7]

print(basket.count(7))
#frequency of 7 in the list


#sorting
print(basket)
basket.sort()
print(basket)

#sorted function, unlike sort returns a sorted list
l1 = sorted([3,4,2,1])


#reverse
basket.reverse()
print(basket)





