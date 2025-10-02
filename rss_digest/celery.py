import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rss_digest.settings")

app = Celery("rss_digest")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
