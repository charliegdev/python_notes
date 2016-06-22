# Object

1. [Basic Usage](#basic-usage)
	1. [Sample Object Creation and Instantiation](#sample-object-creation-and-instantiation)
	2. [Constructor](#constructor)
2. [Advanced](#advanced)
	1. [Underscore Functions](#underscore-functions)

## Basic Usage

### Sample Object Creation and Instantiation

```python
class Student(object):
    def __init__(self, name="None", grade="K", district="Orange Country"):
            self.name = 'name'
            self.grade = grade
            self.district = district
    
    def print_school(self):
        print(self.name)
        print(self.grade)
        print("District: " + self.district)

student1 = Student()
student2 = Student()
```

Each method must have `self` as its first parameter, to refer to the object itself. Notice in `class` statement, we passed in `object` as parameter. This tells Python that our object will extend Python's default `object` object. This is not mandatory, but it's highly recommended; it gives us some extra features that we don't need now, but may come handy in later.

### Constructor

A class can have a `__init__()` function, and it will be called each time a new instance is created. This is also a good place for checking input data.

```python
class Student(object):
    def __init__(self, name='', school='', grade=''):
        if not name:
            name = raw_input("What is the student's name? ") # Python 2 uses raw_input, same as input() in Python 3
        
        if not school:
            school = raw_input("What is the student's school? ")
        
        if not grade:
            grade = self.get_grade()  # we can all any function inside __init__(), since init is also just another function
            
        self.name = name
        self.school = school
        self.grade = grade
        self.print_student()
        
    def get_grade(self):
        while True:
            grade = raw_input("What is the students grade ?[K, 1-5] ")
            if grade.lower() not in ['k', '1', '2', '3', '4', '5']:
                print("I'm sorry, but {} isn't valid.".format(grade))
            else:
                return grade
    
    def print_student(self):
        print("Name: {}".format(self.name))
        print("School: {}".format(self.school))
        print("Grade: {}".format(self.grade))
        
        
def print_roster(students):
    print("Students in the system:")
    for student in students:
        print "*" * 15
        student.print_student()
        

def main():
    student1 = Student(name="Carrie Kale", grade="3", school="Marshall")
    student2 = Student(name="Byron Bale", grade="2", school="Minnieville")
    student3 = Student(name='Sarah Chandler', grade="K", school="Woodbridge")
    
    students = [student1, student2, student3]
    
    print_roster(students)
    

if __name__ == "__main__":
    main()
```

## Advanced

### Underscore Functions

Why does `__init__()` have 2 underscores before and after the function name? Because in Python, if a function is named this way, it won't be called directly. It's a private method.

You're never supposed to call `student4 = Student.__init__()`; instead, just call `student4 = Student()`, and Python is smart enough to call `__init__()` for you.

Python objects can have other private methods too.

#### `__eq__()`

When using `==` to compare 2 objects, by default Python checks if the 2 objects point to the same memory location. Depending on the situation, that may or may not be what you want. 

If you want to compare the content, instead of memory location, you can redefine how `==` works, by overriding `__eq__()` method of the class.

```python
class Test(object):
    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        if self.num == other.num:
            return True
        else:
            return False

a = Test(5)
b = Test(5)
c = Test(7)

print(a == b)       # True
print(a == c)       # False
```

However, Python only knows how to do `==` now; it doesn't know how to do `!=` yet, so we also need to define `__ne__()`.

```python
class Test(object):
    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        if self.num == other.num:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.num != other.num:
            return True
        else:
            return False
            
```

#### More Comparisons

Similar to equal / not equal, Python doesn't know how to do `>` or `<` on a custom object. Define `__gt__()`, `__gth()__`, `__lt()__`, `__lte()__` to enable comparisons; however before you do that, consider whether users should be allowed to have that function.

### Print

Without a custom defined `__str__()` function, use `print()` on an object will print out its memory location. `__str__()` is similar to `toString()` in Javascript and many other languages. It takes `self` as the only parameter, and always returns a string.

Unlike Javascript, Python has no implicit type casting, thus the following code won't work:

```python
class Test(object):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return self.num

a = Test(5)
print(a)
```

We'll get:

```
Traceback (most recent call last):
  File "hour_12.py", line 12, in <module>
    print(a)
TypeError: __str__ returned non-string (type int)
```

Instead, explicitly type cast:

```python
class Test(object):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

a = Test(5)
print(a)
```

This time you'll get 5.

Remember, `__str()__` defines what happens when you call `print()` on the object.

## Inheritance

Suppose you have a base class `ItemTemplate`, that represents an item in a store. You want to inherit it, and expend it, to create `Book`. This is the way to do it in Python:

```python
class InventoryTemplate(object):
    # Notice how the base class inherit 'object', the python generic object class.
    def __init__(self, arg1, arg2):
        self.title = arg1
        self.description = arg2

    def __str__(self):
        # some generic method
        pass

    def __eq__(self):
        pass


class Book(InventoryTemplate):
    def __init__(self, arg1, arg2, arg3, arg4):
        # call parent's constructor, pass in 2 arguments
        super(Book, self).__init__(arg1=arg1, arg2=arg2)
        # notice the rest 2 arguments are passed to current object, not parent
        self.format = arg3
        self.author = arg4

    def __str__(self):
        # override parent's __str()__ method
        book_line = "{title} by {author}".format(
            title=self.title,
            author=self.author
        )

        return book_line
```

