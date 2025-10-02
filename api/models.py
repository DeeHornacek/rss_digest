from django.db import models


# Model representing an order
class NewsSource(models.Model):
    name = models.CharField(max_length=100)
    rss_url = models.URLField(unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Model representing a vehicle
class Article(models.Model):
    source = models.ForeignKey(
        NewsSource,
        on_delete=models.CASCADE,
        related_name="articles"
    )
    title = models.CharField(max_length=200)
    link = models.URLField(unique=True)
    published = models.DateTimeField(null=True, blank=True)
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.title



# Model representing a driver
class Digest(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



# Model representing a driver
class DigestArticle(models.Model):
    digest = models.ForeignKey(
        Digest,
        on_delete=models.CASCADE,
        related_name="items"
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="digests"
    )

    def __str__(self):
        return f"{self.digest} • {self.article}"

