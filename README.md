# UserAuth-Django
Basic user authentication using django

# Backend

It is built with [Python][0] using the [Django Web Framework][1].

This project has the following apps:

* accounts (main user authentication app)

it uses authentication library of django and django restframework for handeling permissions.


## Requirements

- Python 3.6 and above
- pip3 for Python 3.6 and above


---


## Setup

1. Run the Django server

```
pip install -r requirements.txt
python3 manage.py runserver
```

_Runs default on port 8000

Default User for Testing:-

* Username: "anuj" Password: "1234"

* Username: "serendeepia" Password: "1234"

=>Note: 
Users Can Be added by : python manage.py createsuperuser or by admin panel.

## Basic Usage:

http://127.0.0.1:8000/

It redirects to the Home page when user login credentials are correct.

http://127.0.0.1:8000/admin/

users can be added or removed from admin pannel as well.

## Api Usage:
 
 http://127.0.0.1:8000/api/?token=AuthToken
 
 It gives the response only when the user has a current active session , else it redirects to django-restframeworks "Access Denied" page.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
