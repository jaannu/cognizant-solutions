# Hands-On 1 - Web Framework Foundations & Django Project Setup

## Python Backend Frameworks – Digital Nurture 5.0

### Objective

This hands-on introduces the fundamentals of web frameworks and the Django framework. It covers the request-response cycle, MVC/MVT architecture, WSGI vs ASGI, middleware, project setup, URL routing, and creating a basic Django application.

---

## Topics Covered

- Web Framework Concepts
- Request-Response Cycle
- MVC vs MVT Architecture
- WSGI vs ASGI
- Django Project Structure
- Django Apps
- URL Routing
- Middleware
- Function-Based Views

---

## Features Implemented

- Installed Django
- Created Django project (`coursemanager`)
- Created Django app (`courses`)
- Registered the app in `INSTALLED_APPS`
- Created a simple Function-Based View
- Configured URL routing
- Successfully ran the Django development server
- Verified the API endpoint in the browser

---

## Project Structure

```
hands_on_1/
│
├── README.md
├── notes.py
├── task1.md
├── task2.md
│
└── coursemanager/
    ├── manage.py
    ├── coursemanager/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    │
    └── courses/
        ├── views.py
        ├── urls.py
        └── apps.py
```

---

## Concepts Learned

### Request-Response Cycle

A client sends an HTTP request to the Django application.

The request passes through:

- URL Router
- Middleware
- View
- Model (Database)
- Response

Finally, the response is returned to the browser.

---

### Middleware

Middleware processes requests before they reach the view and processes responses before they are sent back to the client.

Examples:

- SecurityMiddleware
- AuthenticationMiddleware

---

### WSGI vs ASGI

**WSGI**

- Supports synchronous applications
- Suitable for traditional web applications
- Django uses WSGI by default

**ASGI**

- Supports asynchronous programming
- Handles WebSockets and long-lived connections
- Used for high-performance asynchronous applications

---

### MVC vs MVT

| MVC | Django MVT |
|------|------------|
| Model | Model |
| View | Template |
| Controller | View |

In Django, the View performs the role of the Controller.

---

## Commands Used

### Install Django

```bash
pip install django
```

### Create Project

```bash
django-admin startproject coursemanager
```

### Create App

```bash
python manage.py startapp courses
```

### Run Server

```bash
python manage.py runserver
```

---

## URL Implemented

| URL | Description |
|------|-------------|
| `/api/hello/` | Returns "Course Management API is running" |

---

## Expected Output

Opening

```
http://127.0.0.1:8000/api/hello/
```

returns

```
Course Management API is running
```

---

## Technologies Used

- Python 3.x
- Django
- SQLite
- VS Code

---

## Learning Outcomes

After completing this hands-on, I learned how to:

- Understand the request-response lifecycle in Django
- Differentiate between WSGI and ASGI
- Understand MVC and Django's MVT architecture
- Create Django projects and apps
- Configure URL routing
- Build a simple Function-Based View
- Run and test a Django application

---

## Author

**Name:** Jagadeeswari

**Program:** Digital Nurture 5.0 – Python Full Stack Engineer Track
