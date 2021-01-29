from django.contrib.sitemaps import Sitemap

from blog.models import Article


class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Article.published.all()

    def lastmod(self, obj):
        return obj.updated
