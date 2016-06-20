# Function

1. [Basic Usage](#basic-usage)
	1. [Sample](#sample)
	2. [Default Values](#default-values)
	3. [Return Values](#return-values)
	4. [Functions with Unknown Number of Parameters](#functions-with-unknown-number-of-parameters)
	5. [`**kwargs`](#`**kwargs`)
	6. [`*args`](#`*args`)
2. [Notes](#notes)
3. [Further Reading](#further-reading)
4. [Parameters: Bind by Value or Reference](#parameters:-bind-by-value-or-reference)

## Basic Usage

### Sample

```python
def sample_func(pram1, pram2):
    statement1
    statement2
    statement3
sample_func(a, b)
```

### Default Values

Python allows functions to set default values for parameters:

```python
def print_welcome(first, last, middle=''):
    ...
```

You must define default parameters as the **last** parameters, so this won't work:

```python
def print_welcome(first, middle='', last):
    ...
```

### Return Values

You don't have to return any value with `return` statement; it can be used alone to return to caller statement. This may come handy in conditional statements:

```python
if condition_1:
    do_something
    return
elif condition_2:
    return
else:
    do_something1
    return
```

### Functions with Unknown Number of Parameters

There are 2 ways of passing in unknown number of parameters:

1. by using `**kwargs` using keywords
1. by using `*args` using tuples

### `**kwargs`

```python
>>> def print_args(arg1, arg2, **kwargs):
...     print(arg1, arg2)
...     print(kwargs)
...
>>> print_args('hello', 'world', book_name='Harry Potter and the Goblet of Fire', author='JK Rowling')
('hello', 'world')
{'book_name': 'Harry Potter and the Goblet of Fire', 'author': 'JK Rowling'}
```

Notes:

1. `kwargs` are used with `**` in parameter, but not with `**` inside function body.
1. keyword cannot be wrapped in quotes.

### `*args`

Use `*args` when you don't want to worry about keywords. Notice the single `*`.

```python
>>> def print_args_2(arg1, arg2, *args):
...     print(arg1)
...     print(arg2)
...     print(args)
...
>>> print_args_2(1, 2, 3, 4, 5,)
1
2
(3, 4, 5)
```

## Notes

1. Don't forget to call your function.
1. It's a convention to create a `main()` function, and use that function as the main entry point. (Unlike C, the name of the function doesn't have to be "main")
1. Use `if __"name__" == "__main__"`

## Further Reading

### Parameters: Bind by Value or Reference

Python is quite special in this respect; read [this](http://stackoverflow.com/a/986145/5827766).


