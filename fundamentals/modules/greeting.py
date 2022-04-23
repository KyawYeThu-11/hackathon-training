# With main
def main():
    hello('World')
    goodbye('World')

def hello(name):
    print(f'Hello, {name}')

def goodbye(name):
    print(f'Goodbye, {name}')

if __name__ == '__main__':
    main()

# Without main
# def hello(name):
#     print(f'Hello, {name}')

# def goodbye(name):
#     print(f'Goodbye, {name}')

# hello('World')
# goodbye('World')