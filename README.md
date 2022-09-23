# Django_Weather

### Weather application using API

## Requirements
1. Python
2. PIP

## Setup 
1. Navigate to the folder to create virtual environment 
2. Create virtual environment
```sh
   py -m venv <venv-name>
```
3. Activate virtual environment
```sh
  <venv-name>\Scripts\activate.bat
```
4. Install django
```sh
  py -m pip install Django
```
5. Create project
```sh
   django-admin startproject weatherapp 
```
   This will create a folder named weatherapp which contains a file manage.py and a folder named weatherapp
```
   weatherapp
   ├── manage.py
   ├── weatherapp
       ├── __init__.py
       ├── asgi.py
       ├── settings.py
       ├── urls.py
       ├── wsgi.py
```
6. Download the code. Replace the contents of the main folder blog, with the downloaded code
7. Generate an API key after signing in to https://home.openweathermap.org/
8. Replace <copy your api key here>, in the file views.py of weather folder, by the generated API key

## Run the project
```sh
cd blog
py manage.py runserver
```
