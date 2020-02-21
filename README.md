# video tube
Video tube application
* User Registration is available.
* User needs to logIn before Uploading any video
* User can watch videos without login to the site.
* User have the option to * Sort, * Serch and * Filter on the Home Page.


## install required packages 
```
cd myweb
pip install -r requirements.txt
```

## install dependent libraries

```
sudo apt install ffmpeg
```

## Make migrations

```
python manage.py makemigrations
python manage.py makemigrations core
python manage.py migrate
```
## Run server

```
python manage.py runserver
```
