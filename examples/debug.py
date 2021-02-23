from capslock import debug

@debug
def add(number1, number2):
    return number1 + number2

if __name__ == '__main__':
    print(add(20, 30))