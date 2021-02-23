import os
import unittest
from capslock import timing
from capslock import debug

@timing
def say_hello():
    for _ in range(100):
        print("Hello World")

@debug
def add(n1, n2):
    return n1 + n2

if __name__ == '__main__':
    add(10, 20)