# Flask GutX Setup Guide

1. Clone the repo:

`git clone https://github.com/gwilson253/flask_gutx`
2. Create virtual environment (assuming Python 3)

`$ python -m venv --without-pip venv`
3. Download the [get-pip.py file](https://bootstrap.pypa.io/get-pip.py)
4. Install requirements:

`$pip install -r requirements.txt`

5. Create development database:

`$ python manage.py db upgrade`

6. Create roles:

```
$ python manage.py shell
>>>Roles.insert_roles()
```

7. Generate fake data for development db:

```
$ python manage.py shell
>>>import app.fake
>>>>>>app.fake.users()
>>>app.fake.posts()
```