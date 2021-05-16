#Dictionary

dictionary = {
    'a':[1,2,3],
    'b':'hello',
    'x': True
}
#unordered key value pair, not right next to each other in memory
print(dictionary['b'])
print(dictionary)

my_list = [
    {
       'a':[1,2,3],
       'b':'hello',
       'x': True
    },
    {
        'a': [4,5,6],
        'b': 'bye',
        'c': False
    }
]

print(my_list[0]['a'][2])
print(my_list[0]['a'][1])

print(my_list[1]['a'])
print(my_list[1]['c'])