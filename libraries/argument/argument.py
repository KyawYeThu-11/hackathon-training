import sys

def main():
    # Check usage
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python argument.py input_file [output_file]")

    input = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) == 3 else 'output.txt'

    names = []

    with open(input, 'r') as file:
        for line in file:
            names.append(line)

    with open(output, 'a') as file:
        for name in names:
            file.write(f'Hello, {name}')


# def main():
#     # Check for proper usage
#     if len(sys.argv) != 2:
#         sys.exit("Usage: python argument.py name")

#     name = sys.argv[1]

#     print(f'Hello, {name}')
    

main()

