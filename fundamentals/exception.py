# system.exit()
import sys

try:
    age = int(input('Enter your age: '))
except:
    print('What you entered is not a valid age.')
    sys.exit()

if age < 18:
    print('You are not allowed to drive.')
else:
    print('Yes. You may drive.')

# # else
# try:
#     age = int(input('Enter your age: '))
# except NameError:
#     print('What you entered is not a valid age.')
# else:
#     if age < 18:
#         print('You are not allowed to drive.')
#     else:
#         print('Yes. You may drive.')