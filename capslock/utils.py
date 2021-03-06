"""
This module defins some utility functions for
capslock library.
"""

from matplotlib import pyplot as plt
import numpy as np
import os

ROOT_PATH = '.capslock'
if not os.path.exists(ROOT_PATH):
    os.mkdir(ROOT_PATH)

def read_timing_db(func_name):
    """Read the stored timings of previous runs
    """
    when = []
    what = []
    db_path = os.path.join(ROOT_PATH, func_name + '.npz')
    if os.path.exists(db_path):
        try:
            data = np.load(db_path)
            when = data['times']
            what = data['speed']
        except Exception as e:
            print(f"Reading failed. {e}")
        else:
            return when, what
    return np.array(when), np.array(what)


def write_timing_db(func_name, when, what):
    """Write the timings of previous runs to db
    """
    db_path = os.path.join(ROOT_PATH, func_name + '.npz')
    try:
        np.savez(db_path, times=when, speed=what)
    except Exception as e:
        print(f"Writing failed. {e}")

def plot_time(func_name, num_of_runs=5):
    """Plots the execution time of last N runs of
    the decorated method"
    """
    try:
        save_path = os.path.join('./', func_name + '.png')

        when, what = read_timing_db(func_name)
        slice_id = -1 * num_of_runs
        x = np.array([i+1 for i in range(len(what))])
        plt.plot(x[slice_id:], what[slice_id:], '-ro', label="runtime")
        plt.xticks(x[slice_id:], when[slice_id:], size='small', rotation=45, fontsize=7)
        plt.xlabel('Date-Time')
        plt.ylabel('Rum Time')
        plt.title(f"Run Time Tracking for {func_name}() function")
        plt.legend()
        plt.tight_layout()
        plt.savefig(save_path)
        # plt.show()
    except Exception as e:
        print(f"Could not plot the run times. Please check your code. {e}")

class BCOLOR:
    """Python color to decorate consol output
       Thanks to this stackoverflow thread
       https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
    """
    ENDC = '\033[0m'
    def mycolor(self, color):
        if color == 'BLUE':
            return '\033[94m'
        if color == 'CYAN':
            return '\033[96m'
        if color == 'GREEN':
            return '\033[92m'
        if color == 'YELLOW':
            return '\033[93m'
        if color == 'RED':
            return '\033[91m'
        if color == 'BOLD':
            return '\033[1m'
        if color == 'UNDERLINE':
            return '\033[4m'
        else:
            print(f"No {color} decorator color found!")
            print("please input color from this list:")
            print("BLUE, CYAN, GREEN, YELLOW, RED, BOLD, UNDERLINE")