import os

# getcwd
print(os.getcwd())

# listdir
print(os.listdir('images'))

for image in os.listdir('images'):
    old_name = f'images/{image}'
    new_name = f'images/{image[:-4]}.jpg'
    os.rename(old_name, new_name)

# data_folder_path = os.path.join(os.getcwd(), 'images')

# for file in os.listdir(data_folder_path):
#     file_path_old = os.path.join(data_folder_path, file)
#     file_path_new = os.path.join(data_folder_path, f'{file[:-4]}.jpg')
#     os.rename(file_path_old, file_path_new)