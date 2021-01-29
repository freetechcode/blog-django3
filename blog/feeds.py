from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy

from blog.models import Article


class LatestArticlesFeed(Feed):
    title = 'Blog Lite'
    link = reverse_lazy('blog:article_list')
    description = 'New articles of my blog'

    def items(self):
        return Article.published.all()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)