from django.contrib import admin, messages

from .models import Article, Digest, DigestArticle, NewsSource


@admin.register(NewsSource)
class NewsSourceAdmin(admin.ModelAdmin):
    """
    Admin configuration for NewsSource:
    - Displays name, RSS URL, and active status
    - Provides filtering and search options
    - Includes custom action to trigger an immediate pull
    """

    list_display = ("name", "rss_url", "active")
    list_filter = ("active",)
    search_fields = ("name", "rss_url")
    actions = ["pull_now", "delete_selected"]

    @admin.action(description="Pull selected sources now", permissions=["change"])
    def pull_now(self, request, queryset):
        """
        Asynchronously queue selected sources for pulling via Celery.
        """
        try:
            from .tasks import pull_source  # local import to avoid overhead at startup
        except Exception as exc:
            self.message_user(
                request,
                f"Could not import tasks: {exc}",
                level=messages.ERROR,
            )
            return

        count = 0
        for src in queryset:
            try:
                pull_source.delay(src.id)
                count += 1
            except Exception as exc:
                self.message_user(
                    request,
                    f"Failed to enqueue '{src}': {exc}",
                    level=messages.WARNING,
                )

        self.message_user(
            request,
            f"Queued pull for {count} source(s).",
            level=messages.SUCCESS,
        )


admin.site.register(Article)
admin.site.register(Digest)
admin.site.register(DigestArticle)
