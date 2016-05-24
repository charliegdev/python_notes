# List

* [Lists Store by Value, Not Store by Reference](#lists-store-by-value-not-store-by-reference)
* [Convenient List Methods](#convenient-list-methods)
	* [`count()`](#count)
	* [`index()`](#index)
	* [`in`](#in)
* [List Manipulation](#list-manipulation)
	* [Add 1 Element to the End of List: `append(item_value)`](#add-1-element-to-the-end-of-list-appenditem_value)
	* [Extend the List with Another List: `extend(list)`](#extend-the-list-with-another-list-extendlist)
	* [Delete an Item by Value: `remove(item_value)`](#delete-an-item-by-value-removeitem_value)
	* [Insert an item at a Specific Spot: `insert(index)`](#insert-an-item-at-a-specific-spot-insertindex)
* [Using Math in Lists](#using-math-in-lists)
	* [Plus: list1 + list2](#plus-list1--list2)
	* [Multiply: list * 3](#multiply-list--3)
* [List Sorting](#list-sorting)
	* [`sort()`](#sort)
	* [`reverse()`](#reverse)
* [List Comparison](#list-comparison)
	* [`==` Takes Considerations of Ordering](#-takes-considerations-of-ordering)
* [Negative Index](#negative-index)

## Lists Store by Value, Not Store by Reference

You can use variable names as elements in a list; however, **Python makes a copy of the variables' values, instead of making a reference.** Example:

```python
>>> fruit1 = "apple"
>>> fruit2 = "pear"
>>>
>>> fruit_list = [fruit1, fruit2]
>>>
>>> fruit_list
['apple', 'pear']
>>>
>>> fruit1 = "orange"
>>> fruit_list
['apple', 'pear']
```

Notice how the list stays the same, even after we change the value of `fruit1`.

## Convenient List Methods

### `count()`

```python
>>> color_list = ['red', 'blue', 'magenta', 'red', 'yellow']
>>> color_list.count('red')
2
```

Notice that lists can have duplicated elements.

### `index()`

```python
>>> color_list.index('red')
0
>>> color_list.index('green')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'green' is not in list
```

Notice:

1. `index()` only returns the 1st occurance of an element.
2. when the queried item does not exist, `index()` returns a `ValueError`, instead of -1.

### `in`
Use the keyword (*not a function or method*) `in` to tell if an element is in a list:

```python
>>> 'pink' in color_list
False
>>> 'red' in color_list
True
```

## List Manipulation

### Add 1 Element to the End of List: `append(item_value)`

Remember: **the list has to exist before you try to change it.**

```python
>>> toppings = []
>>> toppings.append('pepperoni')
>>> toppings.append('mushrooms')
>>> toppings
['pepperoni', 'mushrooms']
```

### Extend the List with Another List: `extend(list)`

```python
>>> order1 = ['pizza', 'fries', 'baklava']
>>> order2 = ['soda', 'lasagna']
>>> order1.extend(order2)
>>> order1
['pizza', 'fries', 'baklava', 'soda', 'lasagna']
```

### Delete an Item by Value: `remove(item_value)`

```python
>>> color_list
['red', 'blue', 'magenta', 'red', 'yellow']
>>> color_list.remove('red')
>>> color_list
['blue', 'magenta', 'red', 'yellow']
```

Notice:

1. `remove(item_value)` accepts the **value** of the item, not its index.
2. `remove(item_value)` only removes the item's first occurance.

If the parameter is not found in the list, Python will throw an error:

```python
>>> color_list.remove('pink')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

When `remove(item_value)` is used, list indices are automatically handled.

### Insert an item at a Specific Spot: `insert(index)`

```python
>>> color_list
['blue', 'magenta', 'red', 'yellow']
>>> color_list.insert(1, 'orange')
>>> color_list
['blue', 'orange', 'magenta', 'red', 'yellow']
```

## Using Math in Lists

### Plus: list1 + list2

When you add 2 lists together, a new list with all the elements is returned; however, the 2 original lists are not changed, unlike `extend(list)` or `append(item_value)`.

```python
>>> color_list
['blue', 'orange', 'magenta', 'red', 'yellow']
>>> number_list = [1, 2, 3]
>>> color_list + number_list
['blue', 'orange', 'magenta', 'red', 'yellow', 1, 2, 3]
>>> color_list
['blue', 'orange', 'magenta', 'red', 'yellow']
```

Notice how Python lists can contain items with different data type.


### Multiply: list * 3

```python
>>> number_list
[1, 2, 3]
>>> number_list * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

## List Sorting

### `sort()`

Sort a list by ascending order:

```python
>>> names = ['Moe', 'Larry', 'Curly']
>>> names.sort()
>>> names
['Curly', 'Larry', 'Moe']
```

```python
>>> prices = [1, 20, 3.0, 4.7]
>>> prices.sort()
>>> prices
[1, 3.0, 4.7, 20]
```

Notice `sort()` will mutate the original list.

If the list contains some integers and strings mixing together, `sort()` will sort numbers first, then strings second, finally put numbers in front of strings.

```python
>>> mixed = [5, 1, 4.0, 'Harold', 'Carol', 7]
>>> mixed.sort()
>>> mixed
[1, 4.0, 5, 7, 'Carol', 'Harold']
```

### `reverse()`

Flip the order of the everthing in the list.

```python
>>> names
['Curly', 'Larry', 'Moe']
>>> names.reverse()
>>> names
['Moe', 'Larry', 'Curly']
```

## List Comparison

### `==` Takes Considerations of Ordering

You can use `==` to see if 2 lists are identical; but `==` will take ordering into consideration as well.

```python
>>> number_list_1 = [1, 2, 3, 4]
>>> number_list_2 = [1, 2, 3, 4]
>>> number_list_1 == number_list_2
True
>>> number_list_3 = [4, 3, 2, 1]
>>> number_list_1 == number_list_3
False
```

## Negative Index

Using negative index will make Python count from the end of the list, intead of the front.

```python
>>> number_list
[1, 2, 3]
>>> number_list[-1]
3
```
