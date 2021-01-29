from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from blog.sitemaps import ArticleSitemap

sitemaps = {
    'articles': ArticleSitemap,
}


urlpatterns = [
    path('sitemap/', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),

    path('', include('blog.urls', namespace='blog')),

]
