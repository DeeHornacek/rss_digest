# api/admin.py
from django.contrib import admin
from .models import NewsSource, Article, Digest, DigestArticle

@admin.register(NewsSource)
class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ("name", "rss_url", "active")
    list_filter = ("active",)
    search_fields = ("name", "rss_url")
    actions = ["pull_now", "delete_selected"]

    @admin.action(description="Pull selected sources now", permissions=["change"])
    def pull_now(self, request, queryset):
        from .tasks import pull_source
        for src in queryset:
            pull_source.delay(src.id)
        self.message_user(request, f"Queued pull for {queryset.count()} source(s).")

admin.site.register(Article)
admin.site.register(Digest)
admin.site.register(DigestArticle)
