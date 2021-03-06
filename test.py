from capslock import require_root
from capslock import color_function_output

@require_root
def say_hello():
    for _ in range(10):
        print("Hello World")


@color_function_output("GREEN")
def hello_color():
    return "Hey! How are you!"

if __name__ == '__main__':
    # say_hello()
    hello_color()