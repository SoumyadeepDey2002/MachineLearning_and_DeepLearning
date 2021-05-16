# Set Methods - 

# .difference()
# .discard()
# .difference_update()
# .intersection()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}

#print(set1.difference(set2))
#returns a set of set1 - st2, removing elements in set1 that are present in set2

#print(set1.discard(5))
#print(set1)

#set1.difference_update(set2)
#modifies set1 as set1 = set.defference(set2)

print(set1.intersection(set2))

print(set1.isdisjoint(set2))
#do they have nothing in common?

print(set1.union(set2))
#union of two sets

#another way to do union
print(set1 | set2)

#another way to do intersection
print(set1 & set2)

print(set1.issubset(set2))
print(set2.issubset(set2))

print(set2.issuperset(set1))
print(set1.issuperset(set2))



