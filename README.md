# RSS Digest

This project is a proof-of-concept Django application that allows admins to manage **news sources (RSS feeds)**, automatically pull articles, and curate them into **digests** for internal use.  

The system uses **Celery** and **feedparser** to periodically fetch RSS feeds, stores articles in the database, and provides full **Django admin** support to review and assemble curated digests.  

---

## Features

- **Manage News Sources**: Add/edit/remove RSS feeds in the Django admin.  
- **Automatic Article Fetching**: Periodic Celery tasks fetch and store new articles.  
- **Manual Trigger**: Admin action *Pull selected sources now* fetches articles on demand.  
- **View Articles**: Browse and search pulled articles directly in the admin.  
- **Curated Digests**: Create digests and select articles to include.  

---

## Tech Stack

- **Python 3.12+**  
- **Django 5.x** – web framework  
- **Django REST Framework** – API endpoints
- **Celery 5.x** – task queue for pulling articles  
- **Redis** – broker & result backend  
- **feedparser** – parsing RSS feeds  
- **Docker & Docker Compose** – containerized deployment  

---

## Project Structure

```
rss_digest/
├─ api/
│  ├─ admin.py         # Django admin customizations
│  ├─ models.py        # NewsSource, Article, Digest, DigestArticle
│  ├─ serializers.py   # DRF serializers
│  ├─ tasks.py         # Celery tasks (pull_source, pull_all_sources)
│  ├─ views.py         # DRF viewsets
│  └─ ...
├─ rss_digest/
│  ├─ settings.py      # Django + Celery configuration
│  ├─ celery.py        # Celery app definition
│  └─ urls.py          # API and admin routes
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
├─ .env
└─ manage.py
```

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/DeeHornacek/rss_digest
cd rss_digest
```

### 2. Environment variables
Create a `.env` file in the project root:

```
DEBUG=1
SECRET_KEY=dev-secret-key
ALLOWED_HOSTS=*

CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/1
```

### 3. Run with Docker Compose
```bash
docker compose up --build
```

Initialize database & create superuser:
```bash
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

Visit the admin at:  
👉 http://localhost:8000/admin/

---

## Usage

1. Log in to Django admin.  
2. Add a **NewsSource** with an RSS URL (e.g. `https://www.sme.sk/rss-title`).  
3. Select the source in the list → Actions → **Pull selected sources now**.  
4. Watch Celery worker logs:  
   ```bash
   docker compose logs -f worker
   ```  
5. Browse **Articles** in the admin – new articles should appear.  
6. Create a **Digest** and add selected articles via **DigestArticle**.  

---

## Example RSS Feeds

- SME Hlavné správy → https://www.sme.sk/rss-title  
- NY Times → https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml  
- BBC News → http://feeds.bbci.co.uk/news/rss.xml  
