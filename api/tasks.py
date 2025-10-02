from celery import shared_task
from .models import NewsSource, Article
import feedparser
from datetime import datetime, timezone

def _to_dt(struct_time):
    if not struct_time:
        return None
    return datetime(*struct_time[:6], tzinfo=timezone.utc)

@shared_task
def pull_source(source_id: int) -> int:
    src = NewsSource.objects.get(id=source_id)
    if not src.active:
        return 0

    parsed = feedparser.parse(src.rss_url)
    new_count = 0
    for entry in parsed.entries:
        link = entry.get("link")
        if not link:
            continue
        defaults = {
            "source": src,
            "title": (entry.get("title") or "").strip(),
            "published": _to_dt(entry.get("published_parsed") or entry.get("updated_parsed")),
            "summary": entry.get("summary", ""),
        }
        obj, created = Article.objects.update_or_create(link=link, defaults=defaults)
        if created:
            new_count += 1
    return new_count
