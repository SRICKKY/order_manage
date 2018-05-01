# Order Manager App

This app is built on top of Python Django Framework

  - User Authentication
  - Registered user can manage orders
  - It has RESTful services



Steps for deployment:
  - Put the project file on github by creating a repo and pushing it through cli or drag and drop functionality.
  - After successfully putting the project files on github.
  - Go to http://pythonanywhere.com and signup for an account.
  - Now log in to the website and choose 'create a begineer account'.
  - Enter the details as required and after that click Register.
  - After successful registration you'll be directed to dashboard.
  - Click on 'Web' tab and then add a new web app.
  - In the 'Create new webapp modal' cilck next button.
  - Then click 'Manual configuration > python 3.6 > next'
  - After few seconds you'll be presented with admin settings/configuration interface(web tab)
  - In web tab scroll down to 'Code' section and 'WSGI Configuration file' link. It'll open wsgi.py file.
  - Uncomment the code show below
  ```sh
  # +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/iamsrikant/mysite/mysite/settings.py'
# and your manage.py is is at '/home/iamsrikant/mysite/manage.py'
path = '/home/iamsrikant/mysite'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
  ```
  
  - Now modify some code here:
 ```sh
 # Set it according to your project name
 path = '/home/iamsrikant/mysite'
 
 os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
 ```
 - Save the file and head back to Web tab
 - Here put the path of virtual environment and path of static file of your project
  - In the Console tab > Start a new BASH Console
  - And in the console trigger few commands:
 
 ```sh
 $ makevirtualenv --python=/usr/bin/python/3.6 env
 $ pip install django
 $ git clone https://github.com/SRICKKY/order_manage.git
```
- Now go back to Files tab
- In the 'settings.py' file of project folder make some change
```sh
$ DEBUG = False
$ ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
$ STATIC_ROOT = '/home/yourusername/yourprojectname/static/'
```
- Save the file and go back to console
```sh
$ cd order_manage
$ python3 manage.py collectstatic
```
- Go to Web tab click the reload button
- After that click on the yourusername.pythonanywhere.com link above reload button
- Now you web app is up and running