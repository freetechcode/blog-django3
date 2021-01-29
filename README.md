## GeeksBlog
This is a blog engine app for geeks writing tutorials like coding or anything.
I built this application project using Django 3, PostgreSQL and Bootstrap 4.0 
and this application is free for anyone with any purpose. 

> In the future, I will build a collection feature where each geek 
will post according to a certain tutorial article in sequence. 
The goal, to give readers premium access rights to read the tutorial.


### Quick Start
Clone this project and get into it. Then, create a virtual environment:
```
$ virtualenv .venv -p python3
$ source .venv/bin/activate
```

Change the `envexample.py` file to `env.py` 
and you can find it in the `mysite` directory. 
Then, fill in the settings that suit your needs:

```python
DEBUG = True
TIME_ZONE = 'UTC'

# Postgre Database config
DB_NAME = ''
DB_USER = ''
DB_PASSWORD = ''

# You can use mailtrap for testing or development
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = ''
EMAIL_USE_TLS = True
EMAIL_YOU = 'admin@geeksblog.com'
```

> Make sure you are running PostgreSQL.

Install the required packages and migrate to the database:

```
$ pip install -r requirements.txt
```

After that, try running the following command to load the initial data

```
$ python manage.py loaddata db.json
```

And finally, start up the development server and 
go to `http://localhost:8000` in the browser.

**Note**: to access the admin page, 
you can go to `http://localhost:8000/admin` and login with 
username `admin` and password `p@ssw0rd24`.

## Features
The following features are available:

- Admin Login and Logout 
- Adding a new user / author
- Create Articles
- Markdown support
- Tagging support
- Comment
- Share by email
- Full Text Search with PostgreSQL Search Vector
- Show latest articles
- Get most commented articles









