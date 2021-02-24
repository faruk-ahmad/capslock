from capslock import timing

@timing(plot=True)
def say_hello():
    for _ in range(10):
        print("Hello World")


if __name__ == '__main__':
    say_hello()