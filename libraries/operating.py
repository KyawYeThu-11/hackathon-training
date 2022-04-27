import os

# getcwd
print(os.getcwd())

# listdir
print(os.listdir('images'))

for image in os.listdir('images'):
    old_name = f'images/{image}'
    new_name = f'images/{image[:-4]}.jpg'
    # print(old_name, new_name)
    os.rename(old_name, new_name)