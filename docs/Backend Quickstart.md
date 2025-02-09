# Developer Quickstart Guide - Tinychains
This **README** file provides a step-by-step guide for setting up the development environment for developers and contributors who intend to join in the development of tinychains.
<hr>

## Quickstart Guide for Backend Developers
### Prerequisites
Ensure you have the following installed:
1. Python 3.10+ 
2. pip (Python package manager)
3. virtualenv for managing virtual environments (optional)

### Clone the Repository
``` 
sh

$ git clone https://github.com/edwardpeter547/tinychains.git
```
a folder **tinychains** should exist in your local directory

### Setup a Virtual Environment
We recommend using a virtual environment to isolate dependencies and to ensure better versioning of dependencies.

**For macOS/Linux:**
```
sh

$ cd tinychains
$ python3 -m venv .venv
$ source .venv/bin/activate
```
**For Windows (Command Prompt/Powershell):**
```
sh
$ cd tinychains
$ python3 -m venv .venv
$ .venv\Scripts\activate
```
**NOTE:** You should see (venv) in your terminal, indicating that the virtual environment is active.

### Install Dependencies 
```
sh
$ cd tinychains/src/backend/
$ pip install -r requirements/development.txt
```

### Setup Environment Variables
Create a .env file in the root of the backend folder and set the environment variables as needed:

Create .env file in the root of your backend directory:
```
sh

$ cd tinychains/src/backend
$ touch .env
```
Generate a **SECRET_KEY** using custom django management command **create_secret_key** which you will paste into your .env file:
```
sh

$ cd tinychains/src/backend
$ python manage.py create_secret_key --settings=core.settings.development
```

Edit the environment file (.env) as follows
```
sh

DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Apply Database Migrations
Run the initial migrations using the **development settings:**
```
sh

$ cd tinychains/src/backend
$ python manage.py migrate  --settings=core.settings.development
```
### Create a superuser (Optional - for Admin Access)
To create a Tinychains superuser for admin access, run:
```
sh

$ cd tinychains/src/backend
$ python manage.py createsuperuser --settings=core.settings.development
```
### Run the Development Server
```
sh

$ cd tinychains/src/backend
$ python manage.py runserver --settings=core.settings.development
```
By default, the server runs on http://127.0.0.1:8000/

### Running Tests
To run unittests using the development settings, execute:
```
sh

$ cd tinychains/src/backend
$ python manage.py test --settings=core.settings.development
```




