from capslock import require_root
from capslock import color_output
from capslock import requires_ram

@require_root
def say_hello():
    for _ in range(10):
        print("Hello World")


@color_output("GREEN")
def hello_color():
    return "Hey! How are you!"

@requires_ram(8.1)
def memory_intensive_task():
    print("Running a memory-intensive task...")

if __name__ == '__main__':
    # say_hello()
    # hello_color()
    memory_intensive_task()