username = input('Enter the UserName : ')
password = input('Enter the Password : ')

# we can do this
# print('*' * 5)
# Output is ***** 

hidden_pass = '*' * len(password) 

print(f'your password {hidden_pass} is {len(password)} letters long')
