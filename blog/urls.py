from django.urls import path

from blog import views
from blog.feeds import LatestArticlesFeed

app_name = 'blog'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('search/', views.article_search, name='article_search'),
    path('<int:year>/<int:month>/<int:day>/<slug:article_slug>/',
         views.article_detail,
         name='article_detail'),
    path('<int:article_id>/share/',
         views.article_share,
         name='article_share'),
    path('<slug:article_slug>/comments/',
         views.comment_list,
         name='comment_list'),
    path('<slug:article_slug>/comments/new/',
         views.comment_create,
         name='comment_create'),
    path('tag/<slug:tag_slug>/',
         views.article_list, name='article_list_by_tag'),
    path('feed/', LatestArticlesFeed(), name='article_feed'),
]

