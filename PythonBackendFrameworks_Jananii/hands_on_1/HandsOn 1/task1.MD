```
1. Draw or describe (in comments inside a new file notes.py) the journey of a GET /api/courses/ request 
through a Django application: URL router → View → Model (DB query) → Response.
"""
Request-Response Cycle in Django

1. User enters:
   http://127.0.0.1:8000/api/courses/

2. Browser sends HTTP GET request.

3. Django receives the request.

4. URL Router checks urls.py

5. Matching View function/class is called.

6. View communicates with Model.

7. Model queries the database.

8. Data is returned to the View.

9. View prepares an HTTP Response.

10. Browser receives and displays the response.
"""
```
```
2.Identify where middleware sits in this cycle. Name two built-in Django middleware classes and 
describe what each does.
"""
Middleware sits between the request and the view.

Example Middleware:

1. SecurityMiddleware
   - Adds security headers.
   - Protects against common attacks.

2. SessionMiddleware
   - Handles user sessions.
   - Stores logged-in user information.
"""
```

```
3.Explain the difference between WSGI and ASGI in comments. State which one Django uses by default 
and when you would switch to ASGI.
"""
WSGI
----
Used for synchronous applications.

Default in Django.

ASGI
----
Supports asynchronous applications,
WebSockets and real-time communication.

Use ASGI for chat applications,
live notifications,
streaming,
etc.
"""
```

```
4.Explain the MVC pattern, then map it to Django's MVT (Model-View-Template): what does each letter 
correspond to in Django?
"""
MVC

Model
View
Controller

Django uses MVT

Model -> Model
View (MVC) -> Template
Controller (MVC) -> Django View

Mapping

MVC            Django

Model      ->  Model
View       ->  Template
Controller ->  View
"""
```
