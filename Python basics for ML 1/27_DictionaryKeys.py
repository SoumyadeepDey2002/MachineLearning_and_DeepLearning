# So far the dictionary keys were string
# well they can be anything that is immutable

#like int, float, string, tuples,
#but not lists as elements in lists can be changed

dictionary = {
    5 : [1,2,3],
    3.14 : 'pi',
    'ok' : 'boomer',
    True : 'this is the Truth!!!',
    'ok' : 123
}
# the value of ok was overwritten,avoid this

print(dictionary[5])
print(dictionary[3.14])
print(dictionary[True])
print(dictionary['ok'])