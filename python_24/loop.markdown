# Loops

## `range()`

```python
# range() stops at parameter - 1
>>> range(7)
[0, 1, 2, 3, 4, 5, 6]

# range() can have a start value.
>>> range(1, 5)
[1, 2, 3, 4]

# range can start with a negative number
>>> range(-3, 2)
[-3, -2, -1, 0, 1]

# range can have a step value. In this case, we must provide all 3 parameters.
>>> range(1, 10, 3)
[1, 4, 7]

# decreasing
>>> range(10, 0, -2)
[10, 8, 6, 4, 2]
```

## A Pythonic `for` Loop

### Basic

```python
>>> for i in range(4):
...     print i
...
0
1
2
3
```

### Name Your Loop Variable
```python
>>> for year in range(2009, 2016):
...     print("I was in UVic in year {}.".format(year))
...
I was in UVic in year 2009.
I was in UVic in year 2010.
I was in UVic in year 2011.
I was in UVic in year 2012.
I was in UVic in year 2013.
I was in UVic in year 2014.
I was in UVic in year 2015.
```

### Loop Through a List

```python
>>> for cat in cats:
...     print("That's a nice {} you have there!".format(cat))
...
That's a nice manx you have there!
That's a nice tabby you have there!
That's a nice calico you have there!
```

In fact, when we use `for i in range(5)`, we're also iterating through a list. Python takes the result of `range(5)`, which is [0, 1, 2, 3, 4], and uses that.

> Often, the variable that's being set is a singular of whatever the list variable is called.

## Loop Convenient Statements and Functions

### Skip Current Iteration: `continue`

Use `continue` to skip any remaining code in this current iteration, and start a new iteration right away. Useful when you want to skip a certain item in a list.

### Stop the Loop Completely: `break`

Use `break` to terminate the loop completely, and ignore all remaining iterations. 

### `else`

```python
for item in items:
    A
    if condition:
        B
        break
else
    C
```

In the above code, code block B & C are mutually exclusive: if B runs, and we call `break`, we won't run code block C under else; otherwise, if B never runs, and `break` is never called, we run code block C.

### Loop Variable Residual Value

> The variable created by the `for` loop doesn't go away after the `for` loop is done. It will contain the last value used in the `for` loop. So, if you're looping over a list of dog breeds with a loop variable of `dog`, `dog` will contain the last item in the list once the loop is done.

## `while` Loop

### `while true` Loop

```python
while True:
    ...
    if condition:
        break
    ...
```
