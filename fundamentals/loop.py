# while loop
n = 0
while n < 5:
    print("meow")
    n = n + 1

while True:
    n = int(input("What's n? "))
    if n > 1:
        break

# for loop
for i in [0, 1, 2]:
    print(f"meow {i}")

# the same as repeat n times
for _ in range(n):
    print("meow")


# # integrating with functions while doing revision
# # step 1
# def main():
#     meow(5)

# def meow(n):
#     for _ in range(n):
#         print('meow')

# main()


# # step 2
# def main():
#     meow(get_number())


# def get_number():
#     while True:
#         n = int(input("What's n? "))
#         if n > 1:
#             return n


# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()

