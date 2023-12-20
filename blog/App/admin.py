from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','short_content','publication_date')

    class Media:
        js = ('js/admin_valid.js',)

admin.site.register(Article, ArticleAdmin)
