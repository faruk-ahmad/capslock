# CAPSLOCK
----------------------------------------------
#### A utility python library for writing certain tasks in python easily & elegantly.
-----------------------------------------------
[The library is still in development. The doc is not completed yet. You can contribute to improve the library.]
## Background
<p align= "justify">

```capslock``` is a high level utility library written in python for writing certain frequently needed task in faster & efficient way. For example, if you want to keep track of the execution time of one of your method while optimizing it, witing code for tracking execution time can be done easily using capslock.
</p>

--------------------------------------------------


## Installation
Install using the following command - 
```bash
pip install capslock
```

Uninstall using the following command - 
```bash
pip uninstall capslock
```

## Getting Started

### How to use decorators from capslock

Capslock defines different decorators that can be used out of the box for certain frequent tasks. E.g. getting the run time of certain function over the period of optimization in development phase.

#### Timing Decorator

To keep track of the execution time of a function in your project for optimizing it over the time, just put the "timing" decorator in your desired function. Capslock will keep track of different run of that function and will plot a well visualized graph for last five execution time of that function.

```python
from capslock import timing

@timing(plot=True)
def say_hello():
    print("Hello World")

if __name__ == '__main__':
    say_hello()
```
This will generate output like bellow: 

![Output of Capslock Timing Decorator](https://raw.githubusercontent.com/faruk-ahmad/capslock/main/docs/output_1.png)

And it will also keep track of runtime for different runs of the ```say_hello()``` function. and will plot a graph in the same directory of your python script if you set ```plot=True```, otherwise the plot flag is by default ```False```.

![Runtime tracking using Capslock Timing Decorator](https://raw.githubusercontent.com/faruk-ahmad/capslock/main/docs/say_hello.png)


#### Debug Decorator

To get debug information of anyof your function, follow the bellow instruction-

```python
from capslock import debug

@debug
def add(number1, number2):
    return number1 + number2

if __name__ == '__main__':
    print(add(20, 30))
```

will provide you the following output with some debug information-

![Debug Information using Capslock Debug Decorator](https://raw.githubusercontent.com/faruk-ahmad/capslock/main/docs/debug.png)


#### Run Multiple Times Decorator

To run a function multiple times, use the ```run_multiple_times``` decorator from capslock package.

```python
from datetime import datetime
from capslock import run_multiple_times

@run_multiple_times(times=10)
def current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S.%f")

if __name__ == '__main__':
    print(current_time())
```

will run the current time function 10 times.

## How to Contribute

You can contribute in different ways. You can add more decorators for frequently used tasks in day to day development works.
