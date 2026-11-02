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

**3. Database:** create a MySQL database, set `MYSQL_DB` and `MYSQL_USER` in `myweb/myweb/settings.py`, and export `MYSQL_PASSWORD` (see [Configuration](#configuration)).

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

## Configuration

Secrets are read from **environment variables**, so nothing sensitive lives in the code. Copy [`.env.example`](.env.example) to `.env` (it is git-ignored) or export the variables in your shell:

| Variable | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | Django `SECRET_KEY`. If unset, a random key is generated at startup (fine for local dev). |
| `MYSQL_PASSWORD` | MySQL password |

The same values are stored as **GitHub Actions secrets** on this repo (*Settings → Secrets and variables → Actions*), so CI/CD workflows can use them as `${{ secrets.NAME }}`.
