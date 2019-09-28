# video tube
Video tube application

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
