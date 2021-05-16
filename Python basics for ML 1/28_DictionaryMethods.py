user = {
    'name' : 'Soumyadeep',
    'greet' : 'hello',
}

#find if a key is present or not
print(user.get('age'))

#if there is no height key we will use 5ft
print(user.get('height',5))

#anotherway to create dict, keys can be only variables
user2 = dict(name='John Doe',age=55)

print(user2)

#finding if key exists

print('name' in user)

#check if the value of key exist
print('hello' in user.values())

#items
print(user.items())

user3 = user.copy()

#clear the dictionary
user.clear()

print(user)
print(user3)

user3.pop('greet')

print(user3)

#pop something random
#user3.popitem()

#update
user3.update({'name':'Nobita'})
print(user3)

