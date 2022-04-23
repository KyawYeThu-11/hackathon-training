# no 'with' + write mode
name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()

# # no 'with' + append mode
# name = input("What's your name? ")

# file = open("names.txt", "a")
# file.write(f'{name}\n')
# file.close()


# # with keyword
# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")



