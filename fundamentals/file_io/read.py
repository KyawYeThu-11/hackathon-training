with open("names.txt", 'r') as file:
    lines = file.readlines()

print(lines)

for line in lines:
    # without rstrip()
    print("hello,", line)
    
    # with rstrip()
    print("hello,", line.rstrip())

