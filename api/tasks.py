from datetime import datetime, timezone

import feedparser
from celery import shared_task

from .models import Article, NewsSource


def _to_dt(struct_time):
    """
    Convert a time.struct_time to a timezone-aware datetime in UTC.

    Args:
        struct_time: A time.struct_time or None.

    Returns:
        datetime | None: Converted datetime object, or None if input is None.
    """
    if not struct_time:
        return None
    return datetime(*struct_time[:6], tzinfo=timezone.utc)


@shared_task
def pull_source(source_id: int) -> int:
    """
    Celery task to fetch and store articles from a given RSS source.

    Args:
        source_id (int): Primary key of the NewsSource to process.

    Returns:
        int: Number of newly created articles.
    """
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
            "published": _to_dt(
                entry.get("published_parsed") or entry.get("updated_parsed")
            ),
            "summary": entry.get("summary", ""),
        }

        _, created = Article.objects.update_or_create(link=link, defaults=defaults)
        if created:
            new_count += 1

    return new_count
