# Video Tube

A small YouTube-style video sharing site built with Django. Anyone can browse and watch videos; signed-in users can upload and edit their own.

## Features

- Sign up and log in (Django auth)
- Upload videos (login required). The video's duration is read automatically with **MoviePy/FFmpeg**.
- Watch videos without logging in
- **Sort, search and filter** on the home page, including by length (short ≤ 4 min, long > 4 min)
- Edit your videos' details

## Tech stack

Python · Django 2.2 · MySQL · MoviePy / FFmpeg · django-crispy-forms · Bootstrap

## Setup

**1. System dependencies**

```bash
sudo apt install ffmpeg            # macOS: brew install ffmpeg
```

**2. Python packages**

```bash
cd myweb
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

**3. Database:** create a MySQL database, then set `MYSQL_DB`, `MYSQL_USER` and `MYSQL_PASSWORD` in `myweb/myweb/settings.py`.

**4. Migrate and run**

```bash
python manage.py makemigrations core
python manage.py migrate
python manage.py runserver          # http://localhost:8000
```

## Routes

| Path | Description |
|---|---|
| `/` | Video list (home) with sort, search and filter |
| `/signup/` | Register |
| `/accounts/login/` | Log in |
| `/videos/upload` | Upload a video |
| `/video_edit/<id>/` | Edit a video |
