# without rstrip()
with open("names.txt", 'r') as file:
    lines = file.readlines()

print(lines)

for line in lines:
    print("hello,", line)

# # with rstrip()
# with open("names.txt") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line.rstrip())

