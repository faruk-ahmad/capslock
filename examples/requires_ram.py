from capslock import requires_ram

@requires_ram(8)
def memory_intensive_task():
    print("Running a memory-intensive task...")


if __name__ == '__main__':
    memory_intensive_task()