# write mode
name = input("What's your name? ")

with open('names.txt', 'w') as file:
    file.write(f"name")

# # append mode
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")



