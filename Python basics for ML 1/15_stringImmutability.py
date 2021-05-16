#String variables can be reassigned with new strings
#but indexes values cannot be changed

word = 'yowhatsup'

# word[3] = 'r' ,gives error

#crafty way to change

word = word[0:3] + 'r' + word[4:]
print(word)

