## Rest Api developed using Django , DRF

### Requirements

* Python 3
* pip


### Instructions :

[1] Clone this rep to local machine

[2] Go to the repo directory on local machine

### For Execution :

> pip install -r requirements.txt

> python manage.py makemigrations

> python manage.py migrate

### Create super user to access admin
> python manage.py createsuperuser

> python manage.py runserver

http://localhost:port/admin : access admin panel

## Api Endpoints

* http://localhost:port/newuser/              : Register New User
* http://localhost:port/authenticate/         : Get auth token
* http://localhost:port/photos/               : View Photos list (paginated)
* http://localhost:port/photos/{id}/          : View Photo by Id
* http://localhost:port/photos/add/           : Add New Photo
* http://localhost:port/photos/delete/{id}/   : Delete Photo


## Run test script

> python manage.py test
