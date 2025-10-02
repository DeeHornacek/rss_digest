import os

from celery import Celery

# Set default Django settings module for the 'celery' command
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rss_digest.settings")

# Create Celery application instance
app = Celery("rss_digest")

# Load configuration from Django settings, using 'CELERY_' prefix
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks across installed Django apps
app.autodiscover_tasks()
