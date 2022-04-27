# Types
x = 'hello'
y = 33
z = 33.33

print(f'Type of x is {type(x)}.')
print(f'Type of y is {type(y)}.')
print(f'Type of z is {type(z)}.')

# Methods
captialized_x = x.capitalize()
print(captialized_x)

if x.startswith('h'):
    print('yes')

print(f'The available methods of string type are {dir(x)}.')

# Casting
age = int(input('Enter your age: '))

if age < 18:
    print('You are not allowed to drive.')
else:
    print('Yes. You may drive.')