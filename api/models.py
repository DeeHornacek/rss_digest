from django.db import models


class NewsSource(models.Model):
    """
    Represents a news source with its name, RSS feed URL, and active status.
    """

    name = models.CharField(max_length=100)
    rss_url = models.URLField(unique=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    """
    Represents an article belonging to a news source.
    Stores metadata such as title, link, publication date, and summary.
    """

    source = models.ForeignKey(
        NewsSource,
        on_delete=models.CASCADE,
        related_name="articles",
    )
    title = models.CharField(max_length=200)
    link = models.URLField(unique=True)
    published = models.DateTimeField(null=True, blank=True)
    summary = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title


class Digest(models.Model):
    """
    Represents a digest, which is a named collection of articles.
    """

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class DigestArticle(models.Model):
    """
    Join model linking articles to digests.
    Each record associates a single article with a single digest.
    """

    digest = models.ForeignKey(
        Digest,
        on_delete=models.CASCADE,
        related_name="items",
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="digests",
    )

    def __str__(self) -> str:
        return f"{self.digest} • {self.article}"
