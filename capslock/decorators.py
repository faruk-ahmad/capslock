"""
This module introduces some decorators that can
be used for some frequent tasks.
"""

import os
import sys
import functools
import time
import numpy as np
from datetime import datetime

from capslock.utils import BCOLOR
from capslock.utils import read_timing_db, write_timing_db, plot_time




def timing(_func=None, *, plot=False):
    """Return the runtime/execution time of the decorated function
    """
    def timing_decorator(func):
        @functools.wraps(func)
        def timing_decorator_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            value = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Finished {func.__name__!r} in {run_time} secs.")
            try:
                when, what = read_timing_db(func.__name__)
                d = datetime.now()
                date_info = str(d.date()) + '\n' + str(d.time()).split('.')[0]
                when = np.append(when, date_info)
                what = np.append(what, run_time)
                write_timing_db(func.__name__, when[-5:], what[-5:]) # -5:  store last 5 run time records
                if plot:
                    plot_time(func.__name__)
            except Exception as e:
                print(f"Could not track timings: {e}")
            return value
        return timing_decorator_wrapper

    if _func is None:
        return timing_decorator
    return timing_decorator(_func)


def debug(_func, *, write=False):
    """Prints/writes debuging info for the decorated function
    """
    def debug_decorator(func):
        @functools.wraps(func)
        def debug_decorator_wrapper(*args, **kwargs):
            args_repr = [repr(arg) for arg in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            print(f"Calling {func.__name__}({signature})")
            value = func(*args, **kwargs)
            print(f"{func.__name__!r} returned {value!r}")
            return value
        return debug_decorator_wrapper
    
    if _func is None:
        return debug_decorator
    return debug_decorator(_func)


def run_multiple_times(times):
    """
    Runs the decorated function multiple times, and print out outputs.

    Parameters
    ----------
        times : int
            How many times the decorated function should run
    """
    def run_recurrent(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            outputs = []
            for _ in range(times):
                output = func(*args, **kwargs)
                outputs.append(output)
            return outputs
        return wrapper
    return run_recurrent


def require_root(func):
    """Runs the decorated function only if user has root/sudo permission
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if os.getuid() == 0:
            result = func(*args, **kwargs)
            return result
        else:
            print(f"[PERMISSION REQUIRED!] You need to be a root user to execute function [{func.__name__}()]")
            sys.exit(0)
    return wrapper

def color_output(color):
    """Print/Writes colorful info of the decorated function

    Args:
        color (str): color name(
            at present support  BLUE, CYAN, GREEN, YELLOW, RED, BOLD, UNDERLINE
            )
    """
    def color_decorator(func):
        @functools.wraps(func)
        def color_decorator_wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            bcolors = BCOLOR()
            mycolor = bcolors.mycolor(color)
            if mycolor:
                print(f"{mycolor}{str(value)}{bcolors.ENDC}")
            return value
        return color_decorator_wrapper
    if color is None:
        return color_decorator
    return color_decorator

if __name__ == '__main__':
    pass