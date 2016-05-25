# View

* [Request & Response Objects](#request--response-objects)
* [Map URL to a View Function](#map-url-to-a-view-function)

## Request & Response Objects

Django uses request and response objects to pass state through the system. 

That was directly from the [doc](https://docs.djangoproject.com/en/1.9/ref/request-response/); I don't understand it yet.

What needs to be remembered here, is that Django always passes an [HttpRequest](https://docs.djangoproject.com/en/1.9/ref/request-response/#django.http.HttpRequest) as the 1st parameter to any view function, and a view function always return an [HttpResponse](https://docs.djangoproject.com/en/1.9/ref/request-response/#django.http.HttpResponse) object:

```python
def results(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))
```

`HttpRequest` (the 1st parameter) is always created by Django automatically; however, `HttpResponse` objects are your responsibility. Each view you write is responsible for instantiating, populating and returning an `HttpResponse`.

However, creating an `HttpResponse` explicitly like the example above is usually no the best thing to do. We can use `render()`:

```python
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

## Map URL to a View Function

Let's say we have an app called "app_name", and here is the root URL of that app:

`http://here.is.some.ip/app_name/`

We want to map that URL (which is `app_name` followed by nothing; the ip address doesn't matter) to the `index(request)` function located in `app_name/views.py`. What do we do?

We go to `app_name/urls.py`, and edit it like this:

```python
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

That `r'^$'` is a regular expression that matches an empty string. We're saying: if we encounter an empty string after `app_name` in the URL, we invoke the `index(request)` function inside `./views`.

## Pass URL Parameters to View Functions

Let's say we have this URL:

```
http://192.168.6.19/polls/5
```

That means we go to the server at 192.168.6.19, go to "polls" app, and see details about question with id of 5.

First, Django goes to `mysite/urls.py`, and finds out that when `polls` is in URL, invoke polls app.

```python
urlpatterns = [
    # the first part r'^polls/' is the query url.
    # the second part is telling Django to look for the rest of the URL in
    # /polls/urls.py
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
```

To pass `5` as a parameter, we edit our polls/urls.py like this:

```python
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
```

Notice that we use `^(?P<question_id>[0-9])/$`. That regex does 2 things:

1. Map the `5/` part in URL
2. Use whatever it finds (in this case, `5/`), as `question_id`, and pass it to the function mentioned (`detail()` in `views.py`)

Similarly, the next line says:

```python
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
```

This says:

1. Map `^[0-9]+/results/$`.
2. Use whatever it finds, pass it as `question_id` to `results()` in `views.py`.

As a reminder, here is what `results()` method does:

```python
def results(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))
```

Notice that `results` takes `request` as its 1st parameter (as all view functions do), and `question_id` as its 2nd.

## Make View Functions Do Stuff

According to [tutorial Section 3](https://docs.djangoproject.com/en/1.9/intro/tutorial03/), view can do a lot of things:

> Your view can read records from a database, or not. It can use a template system such as Django’s – or a third-party Python template system – or not. It can generate a PDF file, output XML, create a ZIP file on the fly, anything you want, using whatever Python libraries you want.

Or not.

**All Django wants from a view function, is an HttpResponse, or an exception.**

Let's make `index()` do something useful: display the most recent 5 poll questions in the system. The database API here are also in model notes.

```python
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # crazy for loop in list
    output = ', '.join([q.question_text for q in latest_question_list]
    
    return HttpResponse(output)
```

## Create an HTML Page to Render View

### Temporary Solution

In the previous section, we wrapped a list inside an `HttpResponse`, and returned it to Django; our `polls/` page would simply display this list. No style. Ugly.

If you just want some simple style, say wrap the list in an `<h1></h1>`, it's simple: you just add that to whatever you're wrapping inside the `HttpResponse`.

However that would quickly get out of hand, for 2 reasons:

1. What if this function does more complicated stuff, and return much more information?
2. We are mixing HTML with Python, thus mixing UI with underlying logic. 

Luckily, we can write our HTML structure in another separate file, and we call it:
**template**.

### Dedicated HTML Template

Let's say this is the current file struction:

```
~/.../tutorial_1/polls/views.py
```

Create this template `index.html` in this position:

```
~/.../tutorial_1/polls/templates/polls/
```

And edit it to have this PHP-like code:

```html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
``` 

Back in our `views.py`, edit `index()` function so it uses this template:

```python
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
```

Notice we're not using `HttpResponse` anymore (we didn't even import it); instead we use [`render()`](https://docs.djangoproject.com/en/1.9/topics/http/shortcuts/#django.shortcuts.render):

**Render(request, template_name, context=None, ...)**

> Combines a given template with a given context dictionary and returns an `HttpResponse` object with that rendered text.

So we are still sending back an `HttpResponse`; we're just using a shortcut functon provided by Django. This is what we would have done if we don't use shortcut function:

```python
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    return HttpResponse(template.render(context, request))
```

### Raising a 404 Error

Sometimes the user requests something that does not exist. For example, use inputs:

```
http://192.168.9.50/polls/12345
```

But there is no question with id of "12345". In that case, we want to raise a 404 error. Then Django can do whatever it deems suitable according to that raised 404 error (say, display a 404 page).

Since the previous URL will invoke `detail()`, we'll modify it so it will raise 404 error when suitable.

```python
from django.http import Http404
from django.shortcuts import render

from .models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question':question})
```

**Shortcut function:** `get_object_or_404()`

Since it's very common to try `get()` and raise `Http404` if fails, Django provides a shortcut. To rewrite the `detail()` function, we do this:

```python
from django.shortcut import get_object_or_404, render

from .models import Question
# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question}
```

However pay attention to `get_object_or_404()`'s documentation:

> Calls get() on a given model manager, but it raises `Http404` instead of the odels' `DoesNotExist` exception.

A similar shortcut function is `get_list_or_404()`
