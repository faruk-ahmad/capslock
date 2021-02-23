"""
This module introduces some decorators that can
be used for some frequent tasks.

Author: Faruk Ahmad
Date: 23/02/2021
Email: faruk.csebrur@gmail.com
"""

import os
import functools
import time



def timing(_func, *, plot=False):
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

if __name__ == '__main__':
    pass