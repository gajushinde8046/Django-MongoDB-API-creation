# Django-MongoDB-API-creation

Django

Make a django folder in that you want to install new project

	1.create virtual env
>>python -m venv env

	2. Set up environment activate For windows
>>env\Scripts\activate

	3.Install Django
>>pip install django

	4.Install Django Admin
>>django-admin startproject api(MainFolder with settings and urls)

	5.Now go to project
>> cd api

	6. Run manage.py
>>python manage.py runserver

	7.now creating application need to 
>>python manage.py startapp MyFirst(ProjectName)

	8. Go to setting in api and set MyFirst in INSTALLED_APPS

	9.And you have successfully run your first Django project
>>localhost:8000



Mongo to Django
Download MONGODB COMPASS
And add emplyeeDB database

Replace current database from settings.py to 
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
       'NAME': 'employeeDB',
    }
}

	10.activate virtual environment
>> env\Scripts\activate
	
	11.change the main project directory
>>cd api
	
	12.Install DJONGO
>>pip install djongo
	
	13.make migration
>>python manage.py makemigrations 
Or
>>manage.py makemigrations MyFirst
	
	14. now migrate the manage.py
>>python manage.py migrate
Or
>>manage.py migrate

	15. Create super user
>>python manage.py createsuperuser

	Set username and password
	16.run the server with \admin and put that username and password in the field
>>python manage.py runserver
	
	17. now you can check the mongo db compass you get data get added in employeeDB



					How django get called
	It always start with manage.py
	>>  api>>Settings.py
	
	Update the apps in INSTALLED_APP
	>> api>>Urls.py
	
	
In that set the path of url in url-patterns	
	
	urlpatterns = [
		path('MyFirst/',include('MyFirst.urls'))
	]

Now it goes to the urls.py in MyFirst app
	
	MyFirst>>urls.py
	urlpatterns = [
		path('post/', post),
	]

Here we can set another path with function post that can be set in

	>>MyFirst>>views.py

And also fetched data from models.py
>>models.py

Now you have already put the script download POSTMAN to check the rest api

 …………………………………………………………………………………………………………..

