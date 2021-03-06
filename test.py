from capslock import require_root

@require_root
def say_hello():
    for _ in range(10):
        print("Hello World")


if __name__ == '__main__':
    say_hello()