# Teach Yourself Python in 24 Hours Notes

## Formatting Output

### Style 1 (Minimalistic)
```python
greeting = "Good {}, {}. How are you doing?"

name = "Hannah"
time = "morning"

print greeting.format(time, name)
```

### Style 2 (Dictionary)
```python
specials_text = "Good {time}! Today's specials are: {special1} and {special2}."

time = "afternoon"
food1 = "spam with eggs"
food2 = "eggs with spam"

print specials_text.format(time=time, special1=food1, special2=food2)
```

### Style 3 (Index)
```python
line = "Cities with Python meet-ups: {0}, {1}, {2}"

print line.format("Victoria", "Vancouver", "Alberta")
```
## Python 2 VS 3: `input()` VS `raw_input()`

### Python 2: `input()` vs `raw_input()`

In Python 2, when `input()` is used to get a string, the string must be wrapped in quotes. So:

```python
>>> greeting = input()
"Hello"
>>> greeting
'Hello'
>>>
>>> greeting2 = input()
Hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1, in <module>
NameError: name 'Hello' is not defined
>>>
```

What really happened, is that `input()` tries to convert the input to the correct data type; so if user enters 5, python converts it to an integer; if user enters 5.5, python converts it to a float. However if user enters a string without quotation, python thinks you're asking for a variable name, instead of a string.

In contrast, `raw_input()` doesn't care what the user inputs; it just capture the input as raw string. As a result, when using `raw_input()`, you don't need to wrap strings inside quotes.

```python
>>> greeting_raw = raw_input()
Hello now!
>>> greeting_raw
'Hello now!'
```

### `input()` in Python 3
Unlike Python 2, there is no `raw_input()` function in Python 3. Instead, Python 3 only has `input()`, but **`input()` in Python 3 is the same thing as `raw_input()` in Python 2.**

## Other Tips in Input Handling

### Use `getpass` to Get Password

```python
from getpass import getpass

password = getpass()
```

### Use `strip()` to Strip Excess Spaces and More
Besides `strip()`, you can also use `lstrip()` and `rstrip()` to strip out characters from both sides. Those stripping functions also takes parameters, as the character to be stripped.

```python
>>> name = "****Catherine***"
>>> name
'****Catherine***'
>>> name.lstrip("*")
'Catherine***'
```

Note that those `strip()` functions (and most string manipulation functions, such as `upper()`) doesn't change the original string:

```python
>>> name = "****Catherine***"
>>> name
'****Catherine***'
>>> name.lstrip("*")
'Catherine***'
>>> name
'****Catherine***'
```

