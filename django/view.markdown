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


