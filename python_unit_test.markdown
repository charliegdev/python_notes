# Python Unit Test

## A New File

Write your unit test inside another separate file. You don't add code to the file you want to test.

Assume you want to test a python file called `moves.py`, you can create a file called `tests.py` inside the same directory as `moves.py`, and at the top of `tests.py`, write this:

```python
import unittest
import moves.py
```

## Test Case
In unit test, we group all our test in a test case. In terms of actual coding, here is an example:

```python
class MoveTests(unittest.TestCase):
    def test_five_plus_five(self):
        assert 5 + 5 == 10

    def test_one_plus_one(self):
        assert not 1 + 1 == 3


if __name__ == '__main__'
    unittest.main()
``` 

You don't have to name your class with "Tests", but it's a convention.

The important thing is: **always start your test function with `test_`.**

## Run Test
Type this in your terminal:

```
python tests.py
```

However, if you don't include the last 2 lines in your `tests.py`, you can run your test like this:

```
python -m unittest tests.py
```
