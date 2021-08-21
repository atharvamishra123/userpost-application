# user_posts_project
A Django based project to allow users to create and submit posts. Use of multiple databases and database routing is done.

## Technologies Used:
* Django = 3.2.3
  
## How to use:
  
#### Clone this project:
```
$ https://github.com/atharvamishra123/user_posts_project.git
``` 

#### Install dependencies:
```
$ pip install -r requirements.txt
```

#### Go to the directory in which you have manage.py:
```
$ python manage.py makemigrations
$ python manage.py migrate
```

#### Create superuser:
```
$ python manage.py createsuperuser
```

#### Run the server on local:
```
$ python manage.py runserver
```
 
#### On a browser, open:
```
$ http://127.0.0.1:8000/signup/
```

###### Now you can signup, login and create a post
###### You can go to django admin at http://127.0.0.1:8000/admin/ to view the models registered.
