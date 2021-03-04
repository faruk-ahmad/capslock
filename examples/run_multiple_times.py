from datetime import datetime

from capslock import run_multiple_times

@run_multiple_times(times=10)
def current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S.%f")

if __name__ == '__main__':
    print(current_time())