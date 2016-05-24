#Python Unit Test


* [A New File](#a-new-file)
* [Test Case](#test-case)
* [Run Test](#run-test)
* [Assertions](#assertions)
	* [Assertions: Equal and NotEqual](#assertions-equal-and-notequal)
	* [setUp()](#setup)
	* [Assertions: Less Than, Greater Than, Less Than or Equal, Greater Than or Equal](#assertions-less-than-greater-than-less-than-or-equal-greater-than-or-equal)
	* [Assertions: In](#assertions-in)
	* [Assertions: IsInstance](#assertions-isinstance)
	* [Assertions: Raise](#assertions-raise)
	* [Assertions: General](#assertions-general)

## A New File

Write your unit test inside another separate file. You don't add code to the file you want to test.

We have a file called `moves.py`, which contains all 3 moves (rock, paper, scissors) in a rock, paper, scissors game. We want to do some unit tests on it to make sure each move gets created and works properly.

Assume you want to test a python file called `moves.py`, you can create a file called `tests.py` inside the same directory as `moves.py`, and at the top of `tests.py`, write this:

```python
import unittest
import moves.py
```

## Test Case
In unit test, we group all our tests in test cases. In terms of actual coding, here is an example:

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

## Assertions
Our unit tests utilize assertions. There are various assertions at our disposal.

### Assertions: Equal and NotEqual
Besides using `==` and `!=`, we can also use `assertEqual(obj1, obj2)`, and `assertNotEqual(obj1, obj2)`.

```python
class MoveTests(unittest.TestCase):
    def test_equal(self):
        rock1 = moves.Rock()
        rock2 = moves.Rock()
        self.assertEqual(rock1, rock2)

    def test_not_equal(self):
        rock = moves.Rock()
        paper = moves.Paper()
        self.assertNotEqual(rock, paper)

```

### setUp()
Before we talk about more assertions, let's talk about an important method:

```python
setUp()
```

Note that this method existed before PEP 8, so it uses camelCase, instead of underscores.

This method gets called everytime we run a test. This is a perfect place to setup anything for tests; hence the name `setUp()`.

Example:

```python
class MoveTests(unittest.TestCase):
    def setUp(self):
        self.rock = moves.Rock()
        self.paper = moves.Paper()
        self.scissors = moves.Scissors()

    def test_equal(self):
        self.assertEqual(self.rock, moves.Rock())

    def test_not_equal(self):
        self.assertNotEqual(self.rock, self.paper)

```

### Assertions: Less Than, Greater Than, Less Than or Equal, Greater Than or Equal

```python
    self.assertGreater(self.rock, self.scissors)
    self.assertLess(self.paper, self.scissors)
    self.assertGreaterEqual(4, 5) # will fail
```

### Assertions: In
Detect if a property/method is a member of a class, or if an element is in a list.

Example:

```python
    self.assertIn(self.someInteger, range(1, 7))
```

### Assertions: IsInstance
Detect if an object is an instance of a class.
Example:

```python
    self.assertIsInstance(self.someInteger, int)
```

### Assertions: Raise
Make sure that a certain exception is raised.

That's right. Making sure our program behaves correctly includes making sure it handles error correctly, and fails gracefully.

Example:

Assume we have a method called `accelerate_to_new_speed(new_speed)`, that ony takes integers as parameters. Ideally, if a non-integer *(say, a string)* is passed in, we want the program to raise a `ValueError`. the `Raise` assertion allows us to test that.

```python
def test_bad_acceleration(self):
    with self.assertRaises(ValueError):
        car.accelerate_to_new_speed("really fast")
```

Note the usage of keyword `with`. It's a [context manager](http://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for).

### Assertions: General

As shown in the beginning, we don't have to use a certain assertion, such as `assertEqual`. We can simply follow this syntax:

```python
assert Expression[, Arguments]
```

Example:

```python
    assert (kelvin_temperature >= 0)
```

Remember when you use a specific assertion, use it with `self`; when using `assert` like above, use it alone.

