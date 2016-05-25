# Model

	* [Define Database Tables Using Python Class](#define-database-tables-using-python-class)
	* [Use Python Shell to Test Model](#use-python-shell-to-test-model)
	* [Queries](#queries)
	* [Question: Simple Queries](#question-simple-queries)
	* [Choice: Using Foreign Key](#choice-using-foreign-key)
    * [notice since we create choices using a question, we don't specify a choice's question_id.](#notice-since-we-create-choices-using-a-question-we-dont-specify-a-choices-question_id)
    * [Use __ to go as deep as you want ](#use-__-to-go-as-deep-as-you-want-)

## Define Database Tables Using Python Class

As in [Tutorial 1, Part 2](https://docs.djangoproject.com/en/1.9/intro/tutorial02/), we need 2 database tables: question & choice.

Question table looks like this:

+--------------+---------------+
| QuestionText | DatePublished |
+--------------+---------------+
| Q1 text      | Q1 date_pub   |
| Q2 text      | Q2 date_pub   |
| Q3 text      | Q3 date_pub   |
+--------------+---------------+

Choice table looks like this:

+------------+------------+-------+
| QuestionID | ChoiceText | Votes |
+------------+------------+-------+
| 1          | very nice  | 0     |
| 1          | so-so      | 0     |
| 1          | not good   | 0     |
| 1          | horrible   | 0     |
+------------+------------+-------+

Notice that every entry in Choice table uses a foreign id (QuestionID) to refer to a question in Question table. And this makes sense: for each question in a poll, we need several choices to complete the poll, and every option created needs to belong to a question.

To use Django's `model` module to create those tables, we do this:

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

Notice how each class attribute reflects the column name of that table.

After finishing writing the model classes, do the following 2 things:

1. In shell, type: `python manage.py makemigrations polls`
2. In shell, type: `python manage.py sqlmigrate polls 0001`
3. In shell, type: `python manage.py migrate`

We never have to write SQL queries; we use Django's ORM to handle data.

## Use Python Shell to Test Model

In shell, type `python manage.py shell` to invoke Django's shell (basically a Python shell with Django loaded).

In the shell, we need to import the model we just wrote:

```python
>>> from polls.models import Question, Choice

# Use .objects to get all Question objects; use .all() to show all of them
>>> Question.objects.all()
[]
# No Questions created yet.

# use timezone for creating questions.
>>> from django.utils import timezone
# create a new Question object.  
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

>>> q.id
1

>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2016, 3, 25, ...)

>>> q.question_text = "What's up?"
>>> q.save()

>>> Question.objects.all()
[<Question: Question object>]
```

However, that last line was not helpful. To change that, add a `__str__(self)` method to your model class to return a string you want. For example:

```python
class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text
```

## Queries

We're using the Django interactive shell as an example, but the principle is the same in actual code.

There are mainly 2 query methods: `get()` and `filter()`. `get()` will return 1 object, while `filter()` returns an iterable object.

## Question: Simple Queries

```python
>>> from polls.models import Question, Choice

>>> Question.objects.all()
[<Question: What's up?>] # our __str(self)__ method worked

>>> Question.objects.filter(id=1)
[<Question: What's up?>]
>>> Question.objects.filter(question_text__startswith='What')
[<Question: What's up?>]

# Notice we use 2 underscores to indicate "go a deeper layer"

>>> Question.objects.get(pub_date__year=2016)
<Question: What's up>
# Notice when we use get, Django returns a single object; 
# When we use filter, Django returns a list containing 1 item.

>>> Question.objects.get(id=2)
Trackback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Since it's common to look up by primary key, Django provides a shortcut:
>>> Question.objects.get(pk=1) # same as id=1
<Question: What's up?>
```

## Choice: Using Foreign Key

You can't simply create a Choice and set its `id` to a question's `id`:

```python
>>> c = Choice(question=1, choice_text="Not much', votes=0)
>>> c.question
<Question: What's up?>
# Seems it works, right? but...
>>> q1 = Question.objects.get(pk=1)
>>> q1.choice_set()
[] # nothing!
```

You have you use `_set()` on `Question` to get 'reverse direction' of foreign key:

A foreign key points a choice to a question; a `_set()` from a question points to all its choices:

```python
>>> q = Question.objects.get(pk=1)
>>> q.choice_set.all()
[]
>>> q.choice_set.create(choice_text='Not much', votes=0)
>>> q.choice_set.create(choice_text='The sky', votes=0)
>>> q.choice_set.create(choice_text='Just hacking again', votes=0)
# notice since we create choices using a question, we don't specify a choice's question_id.

>>> c.question
<Question: What's up?>
>>> q.choice_set.all()
[<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]
>>> q.choice_set.count()
3

# Use __ to go as deep as you want  
>>> Choice.objects.filter(question__pub_date__year=current_year)
[<Choice: Not much>, ...]
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
