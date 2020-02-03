# URLShortner

A Django based task management application consisting of following features:

I) User authentication (Login, Signup, Logout, Forgot Password)
II) Task addition (title, reminder date, priority level)
III) Task deletion, changing completion status
IV) Addition of comments, file attachments(downloadable) for specific tasks

#### Setup and Installation

1. Create and acvirtual environment
```python
py -m venv my_env
# activate virtual environment
source my_env/bin/activate
```

2. Run requirements.txt file (install Python packages as req.)
```python
py -m pip install -r requirements.txt
```

3. Make database migrations
```python
# step 1
py manage.py migrate IEIPL_WebReputation
# step 2
py manage.py makemigrations
```

4. Add EMAIL_HOST_USER, EMAIL_HOST_PASSWORD values and make appropriate settings i.e. secure-access off in email settings (to enable forgot pwd functionality)
5. Create 'media' folder in root directory
6. Test application, url endpoints(based on @login_required decorator for certain endpoints)

#### Deployment

Since Task Manager is an elementary Django application, it would be suitable to deploy it on Free-of-cost platforms eg. Heroku
