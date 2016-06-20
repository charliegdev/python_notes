# Dictionary

Dictionary is similar to lists, in that a dictionary also stores a group of item. The differences are:

1. If you view list items as key:value pairs, then each key is a number; however in a dictionary, keys can be anything; number, strings, variables, blah blah.
2. Items in lists have an order; dictionaries don't. 

## Sample Dictionary

```python
>>> user_emails = {'ada': 'adaxie@uvic.ca', 'bill': 'bsmith@uvic.ca', 'shaw': 'smendez@ubc.bc.ca'}
>>> user_emails['ada']
'adaxie@uvic.ca'
>>> user_emails.ada
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'ada'
```

## Add a New Value to A Key

```python
>>> user_emails["adam"] = "alavine@maroon5.com"
>>> user_emails
{'bill': 'bsmith@uvic.ca', 'shaw': 'smendez@ubc.bc.ca', 'adam': 'alavine@maroon5.com', 'ada': 'adaxie@uvic.ca'}
```

## Modify an Existing Value

```python
>>> user_emails['ada'] = "axie@ubc.ca"
>>> user_emails
{'bill': 'bsmith@uvic.ca', 'shaw': 'smendez@ubc.bc.ca', 'adam': 'alavine@maroon5.com', 'ada': 'axie@ubc.ca'}
```

If the key you specify doesn't exist yet, Python will create a new value for you. So be careful about your spelling; you won't get prompted if you spell your key wrong.

## Delete an Existing Value

```python
>>> shaw_email = user_emails.pop("shaw")
>>> shaw_email
'smendez@ubc.bc.ca'
>>> user_emails
{'bill': 'bsmith@uvic.ca', 'adam': 'alavine@maroon5.com', 'ada': 'axie@ubc.ca'}
```

`pop()` will delete the key:value pair in the dictionary, and return the value. You don't have to store returned value if you don't need it.

## Check If a Key Is in a Dictionary

```python
>>> 'adam' in user_emails
True
>>> 'avril' in user_emails
False
```

## Get All Keys Or All Values from a Dictionary

```python
>>> user_emails.keys()
['bill', 'adam', 'ada']
>>> user_emails.values()
['bsmith@uvic.ca', 'alavine@maroon5.com', 'axie@ubc.ca']
```

## Compare 2 Dictionaries

The 2 dictionaries being compared must have the exact same key:value pairs; however order doesn't matter, unlike lists.

## Dictionary in Python vs in Javascript

In Python (and most other languages), dictionaries are pretty simple. Some other languages call it "associate arrays", based on the fact that it uses strings instead of numbers as keys.

However in Javascript, dictionaries are much more powerful. Dictionaries are basically the Javascript way to define a singular object, with attribute / method names as keys, and attribute value / function content as values.

```javascript
cellphone1 = {
    name: 'iPhone 6s',
    date_of_release: 'Jan 15, 2015',
    call: function (number) {
            ...
    },
    answer: function () {
            ...
    },
    ...
}


