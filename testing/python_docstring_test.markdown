# Docstring Test


* [First Example](#first-example)
* [A (Slightly) More Complicated Example](#a-slightly-more-complicated-example)
* [Run the Test](#run-the-test)
* [Limit of DocTest](#limit-of-doctest)
* [More Powerful Option](#more-powerful-option)

## First Example

**Start the script with a docstring.**

That is not necessary for docstring test, but it's always a good idea to at least say what your script does.

Under the function you want to test, write a docstring test, like this:

```python
def build_cells(width, height):
    """Create and return a width * height grid of 2-tuples.

    >>> cells = build_cells(2, 2)
    >>> len(cells)
    4

    """
    cells = []
    for y in range(height):
        for x in range(width):
            cells.append((x, y))

    return cells
```

Make sure that you put your test after `>>>` *(think of it as a python shell input)*, and your expected output right after lines of `>>>`. If the actual output of the function matches the expect output, you've pass the test.

## A (Slightly) More Complicated Example
In the next docstring test example, we show that we can:

1. Call other functions in our doctest (we don't have to limit ourselves to the current function being tested)
2. Have more than 1 test

```python
def get_locations(cells):
    """Randomly pick starting locations for monster, the door, and the player.

    >>> cells = build_cells(2, 2)
    >>> m, d, p = get_locations(cells)
    >>> m != d and d != p
    True
    >>> d in cells
    True

    """
    monster = random.choice(cells)
    door = random.choice(cells)
    player = random.choice(cells)

    if monster == door or monster == player or door == player:
        monster, door, player = get_locations(cells)

    return monster, door, player
```

## Run the Test

In your terminal, type this:

```
python -m doctest file_name.py
```

If there is no output, you've passed all the tests.

If you do fail, you'll get a constructive error message about expected value and actual value.

## Limit of DocTest
Doctest is easy to implement, but it has 2 major shortcomings:

1. Each test is tightly associated with the function it test, so it's hardly reusable.
2. Test is done by string comparison. Floating point testing is usually really hard or impossible.

## More Powerful Option
For a more powerful module, use Python Unit Test Module.
