**REQUIREMENTS**
```
Python 2.7.6
Django 1.8
Mysql 5.6
```
**CONFIGURATION**
```
Create tables in mysql
python manage.py makemigrations
python manage.py migrate

To start Django server:
python manage.py runserver
```
**API**
```
Download the data from weather website
http://{host}/getdata

Render Chart
http://{host}/renderCharts
```
