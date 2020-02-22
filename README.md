## Starnavi Test Task

This is a test task for Starnavi to build a simple REST API using Django and Django Rest Framework. This API represents a social network with basic user and post models. The API also has the following features: user signup/login, post creation, post like/unlike. For JWT authentication, a [Simple JWT](https://github.com/davesque/django-rest-framework-simplejwt) plugin was used. Unit tests were written for API endpoints using Django Test. To start using this API, run tests or look at API endpoints, see the corresponding paragraph below.

### Running locally
Clone the repository to your local machine. With virtualenv enviroment activated install requirements:
```
$ pip install -r requirements.txt
```
Apply the migrations:
```
python manage.py migrate
```
Use the following command to start the development server:
```
python manage.py runserver
```
### Testing
API endpoints To run tests, use the following command:
```
$ python manage.py test
```
### API endpoints
The full list of API endpoints is available at the following addresses:
> 127.0.0.1:8000/swagger-docs/  

> localhost:8000/swagger-docs/
