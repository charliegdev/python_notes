# Object

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
                print("I'm sorry, but {} isn't valid.".format(grade)
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

Why does `__init__()` have 2 underscores before and after the function name? Because in Python, if a function is named this way, it won't be called directly.

You're never supposed to call `student4 = Student.__init__()`; instead, just call `student4 = Student()`, and Python is smart enough to call `__init__()` for you.
